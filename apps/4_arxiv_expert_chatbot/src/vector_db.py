import os
from langchain_community.vectorstores import FAISS
from src.loader import load_data
from src.embeddings import get_embedding

VECTOR_PATH = "vector_db"
DATA_PATH = "data/arxiv_data.json"

def create_vector_db():
    docs = load_data(DATA_PATH)
    embeddings = get_embedding()

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(VECTOR_PATH)

    print("✅ Vector DB created!")

def load_vector_db():
    embeddings = get_embedding()
    return FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )