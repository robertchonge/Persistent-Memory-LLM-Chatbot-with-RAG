import streamlit as st
import requests
from frontend.components import chat_input, chat_history_display, display_response

st.title("Persistent Memory Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_id = "demo_user"

message = chat_input()

if st.button("Send") and message:
    response = requests.post("http://localhost:8000/chat", json={"user_id": user_id, "message": message})
    response_data = response.json()

    st.session_state.chat_history.append(f"User: {message}")
    st.session_state.chat_history.append(f"AI: {response_data['response']}")

chat_history_display(st.session_state.chat_history)

if "response_data" in locals():
    display_response(response_data["response"])
