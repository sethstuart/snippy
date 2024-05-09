import requests
from bs4 import BeautifulSoup
import re

def scrape_product_titles(url):
    # Fetch the page content
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define a regex pattern to match the specific span IDs
    pattern = re.compile(r'product-title-[A-Za-z0-9]{10}')

    # Find all span tags with an ID that matches the pattern
    spans = soup.find_all('span', id=pattern)

    # Extract the text and ID of each matching span
    products = [(span.get_text().strip(), span['id']) for span in spans]

    return products

# URL of the webpage to scrape
with open("urlSecret", "r") as file:
    url = file.read().strip()

print(f"Thank you for choosing Snippy! Now scraping for URL: {url}!\n\n")

# Scrape the product titles and print the results
product_titles = scrape_product_titles(url)
print(product_titles)
