import pandas as pd
from langchain_core.documents import Document


def load_data(file_path):

    df = pd.read_csv(file_path)

    # normalize column names
    df.columns = df.columns.str.strip().str.lower()

    if df.empty:
        print(f"{file_path} is empty. Skipping.")
        return []

    if "question" not in df.columns or "answer" not in df.columns:
        raise ValueError(
            f"{file_path} must contain 'question' and 'answer' columns. Found: {df.columns}"
        )

    documents = []

    for _, row in df.iterrows():

        text = f"Question: {row['question']}\nAnswer: {row['answer']}"

        documents.append(
            Document(
                page_content=text,
                metadata={"source": file_path}
            )
        )

    return documents