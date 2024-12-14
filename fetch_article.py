# fetch_article.py
import requests
from bs4 import BeautifulSoup

def fetch_article(url):
    """Fetch the article content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = soup.get_text()
        return article_text
    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL format. Please enter a valid URL.")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the URL. Please check your internet connection.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None