from textblob import TextBlob

def analyze_sentiment(text):
    """
    Returns sentiment label + polarity
    """

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "positive", polarity
    elif polarity < -0.2:
        return "negative", polarity
    else:
        return "neutral", polarity