import streamlit as st
from src.chatbot import generate_answer
from src.vector_db import create_vector_db
import os

st.set_page_config(page_title="arXiv Expert Chatbot")

st.title("📚 arXiv Expert Chatbot")

# Create DB if not exists
if not os.path.exists("vector_db"):
    st.warning("Creating vector DB...")
    create_vector_db()
    st.success("Vector DB Ready!")

query = st.text_input("Ask a research question:")

if query:
    with st.spinner("Thinking..."):
        answer = generate_answer(query)

    st.write("### 🤖 Answer")
    st.write(answer)