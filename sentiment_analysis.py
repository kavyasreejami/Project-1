from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(article_text):
    """Analyze the sentiment of the given article text."""
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(article_text)
    
    # Classify sentiment based on compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, sentiment_scores