import streamlit as st

def chat_input():
    return st.text_input("Enter your message:", key="user_message")

def chat_history_display(history):
    st.subheader("Chat History")
    for msg in history:
        st.write(msg)

def display_response(response):
    st.subheader("AI Response")
    st.write(response)
