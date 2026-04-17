import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_client():
    return genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_response(prompt):
    client = get_gemini_client()

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text