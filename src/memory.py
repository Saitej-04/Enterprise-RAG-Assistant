import streamlit as st


def initialize_memory():

    if "messages" not in st.session_state:
        st.session_state.messages = []


def add_user_message(message):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_ai_message(message):

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": message
        }
    )


def get_messages():

    return st.session_state.messages


def clear_chat():

    st.session_state.messages = []