# **NewsPulse: Web Scraping & Analysis System**


Project Description
This project is an end-to-end solution for extracting and analyzing news articles from the web. It combines web scraping, Named Entity Recognition (NER), and Sentiment Analysis to process textual data efficiently. The results are stored in a structured format for further analysis or reporting.

Key Features
Web Scraping:
Extracts the title and content from news articles using BeautifulSoup and HTTP requests.
Named Entity Recognition (NER):
Identifies important entities such as names, locations, and organizations from the extracted content.
Sentiment Analysis:
Analyzes the overall sentiment (positive, neutral, or negative) of the article content using VADER Sentiment Analyzer.
Data Storage:
Stores processed results (title, entities, sentiment) into an SQLite database for easy retrieval.
Results Display:
Outputs the extracted information and insights to the command line interface (CLI).
Tech Stack
Python
BeautifulSoup for web scraping
Natural Language Toolkit (NLTK) for NER and sentiment analysis
SQLite for storing results
How It Works
The user inputs a URL of a news article.
The system fetches the web page content.
HTML content is parsed using BeautifulSoup to extract:
Article title
Article body content
Named Entity Recognition (NER) is performed to identify relevant entities.
Sentiment Analysis is applied to determine the article's sentiment.
The results are stored in the SQLite database and displayed on the CLI.
![Screenshot 2024-12-15 231759](https://github.com/user-attachments/assets/95b45f65-a71a-453c-9081-b5a8d6d2da9a)
![Screenshot 2024-12-15 232005](https://github.com/user-attachments/assets/e9e3e8f9-9153-4efc-aa1c-a541f40f82db)



