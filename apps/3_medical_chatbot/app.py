import streamlit as st
from src.qa_chain import get_answer

st.title("🩺 Medical Chatbot")

query = st.text_input("Ask a medical question:")

if query:
    with st.spinner("Thinking..."):
        response = get_answer(query)

    st.write(response)