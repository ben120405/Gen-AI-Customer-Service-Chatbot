import os
from dotenv import load_dotenv
from google import genai

from src.language_detector import detect_language
from src.translator import translate_to_english, translate_from_english

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_response(user_input):

    # Detect language
    lang = detect_language(user_input)

    # Translate → English
    english_input = translate_to_english(user_input, lang)

    prompt = f"""
    You are a helpful AI assistant.
    Answer clearly and simply.

    User:
    {english_input}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        english_output = response.text

        # Translate back
        final_output = translate_from_english(english_output, lang)

        return final_output, lang

    except Exception as e:
        return f"❌ Error: {str(e)}", lang