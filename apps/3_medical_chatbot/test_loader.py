from src.loader import load_data

texts = load_data("data")

print("Total QAs:", len(texts))
print(texts[0])