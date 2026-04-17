import os

def load_env_variable(key):
    value = os.getenv(key)
    if not value:
        raise ValueError(f"{key} not found in environment variables")
    return value


def clean_text(text):
    return text.strip().replace("\n", " ")