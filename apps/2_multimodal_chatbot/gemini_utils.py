from google import genai
import os
from dotenv import load_dotenv

# Load environment variables (force override)
load_dotenv(dotenv_path=".env", override=True)

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("❌ API KEY NOT FOUND. Check your .env file.")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def get_chat_response(messages):
    """
    Generate response using full conversation history
    """

    try:
        history = []

        for msg in messages:
            role = "user" if msg["role"] == "user" else "model"

            history.append({
                "role": role,
                "parts": [msg["content"]]
            })

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=history
        )

        return response.text

    except Exception as e:
        return f"❌ Error generating response: {str(e)}"