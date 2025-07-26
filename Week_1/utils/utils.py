import streamlit as st


def initialize_session():
    pass


def display_messages(state: dict):
    for message in state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
