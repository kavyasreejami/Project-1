import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    return {
        'title': _extract_title(soup),
        'text': _extract_content(soup)
    }

def _extract_title(soup):
    title_options = [soup.find('meta', property='og:title'), soup.find('title'), soup.find('h1')]
    for title_tag in title_options:
        if title_tag:
            return title_tag.get('content', title_tag.text).strip()
    return 'No Title Found'

def _extract_content(soup):
    selectors = ['article', 'div.article-body', 'div.content', 'div.main-content', 'body']
    for selector in selectors:
        content_div = soup.select_one(selector)
        if content_div:
            paragraphs = content_div.find_all(['p', 'div'])
            content = ' '.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
            if content:
                return content
    return 'No Content Found'
