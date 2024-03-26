import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_article(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the request with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main content div
        content = soup.find(id='mw-content-text')

        # Extract and return the text
        return content.get_text()
    else:
        return "Failed to retrieve the content"

# Example URL (replace with any Wikipedia article URL)
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Scrape and print the article
article_content = scrape_wikipedia_article(url)
print(article_content)
