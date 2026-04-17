from src.loader import load_data
from src.vector_db import create_vector_db

texts = load_data("data")

create_vector_db(texts)