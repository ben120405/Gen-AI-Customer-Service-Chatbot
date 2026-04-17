from src.retriever import get_similar_docs

docs = get_similar_docs("What is diabetes?")
print(docs[0].page_content)