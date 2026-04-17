import streamlit as st
from src.chatbot import generate_response

st.set_page_config(page_title="Multilingual Chatbot")

st.title("🌍 Multilingual Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Type your message...")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response, lang = generate_response(user_input)

        st.write(f"🌐 Language: {lang}")
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })