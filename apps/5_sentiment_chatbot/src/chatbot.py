import os
from dotenv import load_dotenv
from google import genai
from src.sentiment import analyze_sentiment

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_response(user_input):

    sentiment, score = analyze_sentiment(user_input)

    prompt = f"""
    You are an emotionally intelligent AI assistant.

    User sentiment: {sentiment} (score: {score})

    Instructions:
    - If negative → be supportive, empathetic
    - If positive → be encouraging
    - If neutral → be informative
    - Keep responses natural and human-like

    User:
    {user_input}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text, sentiment

    except Exception as e:
        return f"❌ Error: {str(e)}", sentiment