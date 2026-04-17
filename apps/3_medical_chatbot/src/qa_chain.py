from src.retriever import get_similar_docs
from google import genai
import os
from dotenv import load_dotenv

load_dotenv(override=True)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def get_answer(query):

    docs = get_similar_docs(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a medical assistant.

    Answer ONLY from the context below.
    If not found, say "I don't know".

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