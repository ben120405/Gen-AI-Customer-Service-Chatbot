from src.translator import translate_to_english, translate_from_english

# Test 1: Hindi → English
print("Hindi → English:")
print(translate_to_english("नमस्ते", "hi"))

# Test 2: English → Hindi
print("\nEnglish → Hindi:")
print(translate_from_english("Hello", "hi"))

# Test 3: French → English
print("\nFrench → English:")
print(translate_to_english("Bonjour", "fr"))

# Test 4: English → French
print("\nEnglish → French:")
print(translate_from_english("How are you?", "fr"))