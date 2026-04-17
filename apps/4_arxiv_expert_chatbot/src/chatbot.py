import os
from dotenv import load_dotenv
from google import genai
from src.retriever import get_relevant_docs

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(query):
    try:
        docs = get_relevant_docs(query)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        You are an expert AI research assistant.

        Instructions:
        - Answer only from context
        - Explain clearly
        - Be structured
        - If not found, say "I don't know"

        Context:
        {context}

        Question:
        {query}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"