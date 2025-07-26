import streamlit as st
import random
import time
from utils.utils import display_messages


def initialize_session():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I'm here to help you generate email drafts.",
            }
        ]


def response_generator(prompt):
    """A simple rule-based response generator."""
    prompt = prompt.lower()

    # Pre-defined responses
    responses = {
        "hello": "Hello there! How are you?",
        "hi": "Hi! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! Thanks for asking.",
        "what is your name": "I am a simple Streamlit chatbot.",
        "bye": "Goodbye! Have a great day!",
        "what can you do": "I can have simple conversations. Try asking me 'how are you' or say 'hello'!",
    }

    if prompt in responses:
        response = responses[prompt]
    else:
        found = False
        for key, value in responses.items():
            if key in prompt:
                response = value
                found = True
                break
        # Default response if no match is found
        if not found:
            default_responses = [
                "I'm not sure how to respond to that. Can you try asking something else?",
                "That's an interesting question! I'll have to think about it.",
                "Sorry, my knowledge is limited. I am a simple bot.",
                "Could you please rephrase that?",
            ]
            response = random.choice(default_responses)

    # Simulate a "thinking" delay and stream the response
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def handle_user_input():
    """Handles user input and generates responses."""
    prompt = st.chat_input("What would you like to say?")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(prompt))

        st.session_state.messages.append({"role": "assistant", "content": response})


def main():
    st.set_page_config(
        page_title="Streamlit Email Draft", page_icon="📧", layout="centered"
    )
    st.title("📧 Email Draft Generator")
    st.caption(
        "A simple email draft generator using Streamlit's session state and chat elements."
    )
    initialize_session()
    display_messages(st.session_state)
    handle_user_input()


main()
