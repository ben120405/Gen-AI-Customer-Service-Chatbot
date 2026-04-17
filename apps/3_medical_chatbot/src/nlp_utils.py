def detect_intent(query):
    query = query.lower()

    if "symptom" in query:
        return "symptom"
    elif "treatment" in query:
        return "treatment"
    elif "disease" in query:
        return "disease"
    else:
        return "general"