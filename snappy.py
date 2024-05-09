from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_product_titles(url):
    logging.info("Starting to scrape the website with Selenium")

    # Set up the Selenium WebDriver
    options = Options()
    options.headless = True  # Enable headless mode for automation
    with open("chromedriverPath", "r") as file:
      driverPath = file.read().strip()
    service = Service(driverPath)  # Path to Chromedriver
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        logging.info("Web page loaded successfully")

        # Wait for JavaScript to load (adjust time as necessary)
        driver.implicitly_wait(10)

        # Define a regex pattern to match the specific span IDs
        pattern = re.compile(r'product-title-[A-Za-z0-9]{10}')
        logging.debug("Regex pattern compiled")

        # Find all span tags with an ID that matches the pattern
        spans = driver.find_elements(By.XPATH, "//span[contains(@id, 'product-title-')]")
        logging.info(f"Found {len(spans)} spans with matching IDs")

        # Extract the text and ID of each matching span
        products = [(span.text.strip(), span.get_attribute('id')) for span in spans]
        logging.info(f"Extracted data from spans: {products}")

        return products

    finally:
        # Clean up: close the browser window
        driver.quit()

# Read URL from the urlSecret file
with open("urlSecret", "r") as file:
    url = file.read().strip()

print(f"Thank you for choosing Snippy! Now scraping for URL: {url}!\n\n")

# Scrape the product titles and print the results
product_titles = scrape_product_titles(url)
print(product_titles)
