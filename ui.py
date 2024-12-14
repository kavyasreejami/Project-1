from flask import Flask, render_template, request
from fetch_article import fetch_article
from ner_extraction import extract_entities
from sentiment_analysis import analyze_sentiment
import sqlite3

app = Flask(__name__)

def save_to_database(article_text, entities, sentiment, sentiment_scores):
    """Save article data to the database."""
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    
    # Insert the data into the articles table
    cursor.execute('''
    INSERT INTO articles (article_text, entities, sentiment, sentiment_scores)
    VALUES (?, ?, ?, ?)
    ''', (article_text, entities, sentiment, sentiment_scores))
    
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    article_text = ""
    entities = ""
    sentiment_result = ""
    
    if request.method == 'POST':
        url = request.form['url']
        article_text = fetch_article(url)
        
        if article_text:
            # Extract entities
            entities_data = extract_entities(article_text)
            entities = "\n".join([f"{ent[0]} ({ent[1]})" for ent in entities_data])
            
            # Analyze sentiment
            sentiment, sentiment_scores = analyze_sentiment(article_text)
            sentiment_result = f"Sentiment: {sentiment}\nScores: {sentiment_scores}"
            
            # Save to database
            save_to_database(
                article_text=article_text,
                entities=str(entities_data),  # Store as a string or JSON
                sentiment=sentiment,
                sentiment_scores=str(sentiment_scores)  # Store as a string or JSON
            )
        else:
            article_text = "Failed to fetch article."

    return render_template('index.html', article_text=article_text, entities=entities, sentiment_result=sentiment_result)

@app.route('/articles')
def view_articles():
    """View stored articles from the database."""
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, article_text, entities, sentiment, sentiment_scores FROM articles')
    articles = cursor.fetchall()
    conn.close()
    
    return render_template('articles.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
