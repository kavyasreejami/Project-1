from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    try:
        return sentiment_analyzer(text[:512])[0]['label'].lower()
    except Exception as e:
        return 'neutral'
