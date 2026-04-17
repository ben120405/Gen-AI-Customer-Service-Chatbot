from src.vector_db import load_vector_db

def get_relevant_docs(query):
    db = load_vector_db()
    docs = db.similarity_search(query, k=3)
    return docs