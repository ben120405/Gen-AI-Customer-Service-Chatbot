import streamlit as st
from gemini_utils import get_chat_response

# Page configuration
st.set_page_config(
    page_title=" Gemini Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖  Chatbot with Memory")
st.write("Ask questions — the bot remembers your conversation.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_prompt = st.chat_input("Ask something...")

if user_prompt:

    # USER MESSAGE
    with st.chat_message("user"):
        st.write(user_prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # ASSISTANT RESPONSE
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                # Limit memory to last 6 messages (avoid token overflow)
                recent_messages = st.session_state.messages[-6:]

                response = get_chat_response(recent_messages)

            except Exception as e:
                response = f"❌ Error: {str(e)}"

        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# Optional: Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()