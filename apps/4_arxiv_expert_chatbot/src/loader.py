import json
from langchain_core.documents import Document

def load_data(file_path, limit=2000):  # limit for testing
    docs = []

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):

            try:
                item = json.loads(line)

                title = item.get("title", "")
                abstract = item.get("abstract", "")

                if not title or not abstract:
                    continue

                text = f"Title: {title}\nAbstract: {abstract}"

                docs.append(Document(page_content=text))

            except Exception as e:
                print("Error:", e)
                continue

            # VERY IMPORTANT (avoid crashing your system)
            if i >= limit:
                break

    return docs