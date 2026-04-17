import os
import json
from langchain_community.vectorstores import FAISS
from ingestion.embeddings import get_embedding
from ingestion.loader import load_data

VECTOR_PATH = "vector_db"
PROCESSED_FILE = "metadata/processed_files.json"


def get_processed_files():

    if not os.path.exists(PROCESSED_FILE):
        return []

    with open(PROCESSED_FILE, "r") as f:
        return json.load(f)


def save_processed_files(files):

    with open(PROCESSED_FILE, "w") as f:
        json.dump(files, f)


def update_db(file_path):

    processed = get_processed_files()

    file_name = os.path.basename(file_path)

    if file_name in processed:
        print(f"Skipping {file_name} (already processed)")
        return

    print(f"Processing new file: {file_name}")

    docs = load_data(file_path)
    embeddings = get_embedding()

    if not os.path.exists(VECTOR_PATH):

        print("Creating new vector database")

        db = FAISS.from_documents(docs, embeddings)

    else:

        print("Updating existing vector database")

        db = FAISS.load_local(
            VECTOR_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        db.add_documents(docs)

    db.save_local(VECTOR_PATH)

    processed.append(file_name)

    save_processed_files(processed)

    print(f"{file_name} added to knowledge base")