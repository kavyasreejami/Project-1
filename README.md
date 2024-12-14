# **Project-1**

## **Overview**

This project is an end-to-end pipeline designed to analyze news articles. It provides a comprehensive interface to:
- Fetch article content from URLs.
- Extract Named Entities (e.g., `PERSON`, `ORG`) using spaCy.
- Perform sentiment analysis using the VADER sentiment analysis tool.
- Store the processed data in an SQLite database for future reference.

The application is modular, built with Python and Flask, offering an efficient and user-friendly way to interact with the pipeline.

---

## **Features**

- Fetch and parse article text from URLs.
- Perform **Named Entity Recognition (NER)** to identify key entities:
  - `PERSON`
  - `ORG`
- Analyze sentiment to classify articles as:
  - `Positive`
  - `Neutral`
  - `Negative`
- Save the fetched article, extracted entities, and sentiment results in an SQLite database.
- Provide a web interface for:
  - Entering article URLs.
  - Viewing processed articles and their metadata.

---

## **Technologies Used**

- **Programming Language:** Python
- **Frameworks & Libraries:**
  - Flask: Backend framework for the web application.
  - spaCy: For Named Entity Recognition (NER).
  - VADER: For sentiment analysis.
  - SQLite: Lightweight database for storing data.
  - BeautifulSoup: For web scraping and content extraction.
  - Requests: For fetching data from URLs.
- **Frontend:**
  - HTML/CSS for a basic user interface.

---

## **Directory Structure**

```plaintext
project/
│   create_db.py         # Initialize SQLite database
│   fetch_article.py     # Fetch article content from URLs
│   ner_extraction.py    # Perform Named Entity Recognition
│   sentiment_analysis.py # Perform sentiment analysis
│   ui.py                # Flask application for user interaction
│   requirements.txt     # Python dependencies
│
├───static/
│   └───css/
│           style.css    # Frontend styling
│
├───templates/
│       index.html       # HTML template for the Flask app
│
└───.dockerignore        # Ignore unnecessary files during builds
