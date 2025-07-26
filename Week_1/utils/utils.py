import streamlit as st
import re

def initialize_session():
    pass


def display_messages(state: dict):
    for message in state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def split_think_content(text: str) -> tuple[str, str]:
    """
    Splits text into content inside and outside of <think> tags.

    This function uses a regular expression to find all occurrences of
    <think>...</think> tags and the text that follows them. It then
    reassembles these parts into two separate strings.

    Args:
        text: The input string containing a mix of regular content and
              content within <think> tags.

    Returns:
        A tuple containing two strings:
        - The first string is the concatenated content from *inside* all <think> tags.
        - The second string is the concatenated content from *outside* all <think> tags.
    """
    # Pattern to find:
    # 1. The content inside a <think> tag (non-greedy).
    # 2. The content outside the tags until the next <think> tag or end of string.
    # re.DOTALL allows '.' to match newlines.
    pattern = r"<think.*?>(.*?)</think>|(.*?)(?:<think.*?>|$)"
    
    matches = re.findall(pattern, text, re.DOTALL)
    
    think_content = []
    output_content = []
    
    for think_match, output_match in matches:
        if think_match:
            # This was content inside a <think> tag
            think_content.append(think_match.strip())
        if output_match:
            # This was regular content outside a tag
            output_content.append(output_match)
            
    # Join the parts into two separate strings
    # Use '\n---\n' to separate different thought blocks for clarity
    final_think = "\n---\n".join(think_content)
    final_output = "".join(output_content).strip()
    
    return final_think, final_output