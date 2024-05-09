from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_product_titles(url):
    logging.info("Starting to scrape the website with Selenium")

    # Set up the Selenium WebDriver
    options = Options()
    options.headless = True  # Enable headless mode for automation

    # Set the driver manually here:
    # with open("chromedriverPath", "r") as file:
    #   driverPath = file.read().strip()
    #   logging.info(f"Attempting to use driver at specified path: {driverPath}")
    # service = Service(driverPath)  # Path to Chromedriver
    # driver = webdriver.Chrome(service=service, options=options)

    # Or set it automatiicaly here:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        logging.info("Web page loaded successfully")

        # Wait for JavaScript to load (adjust time as necessary)
        driver.implicitly_wait(10)

        # Find all span tags with an ID that contains 'product-title-'
        spans = driver.find_elements(By.XPATH, "//span[contains(@id, 'product-title-')]")
        logging.info(f"Found {len(spans)} spans with matching IDs")

        # Extract the text and ID of each matching span
        products = [{'name': span.text.strip(), 'productTitleID': span.get_attribute('id').split('-')[-1]} for span in spans]
        logging.info("Data extraction complete")

        return products

    finally:
        # Clean up: close the browser window
        driver.quit()

def write_to_yaml(data, filename="output.yaml"):
    # Constructing the desired YAML structure
    yaml_data = {'snappyGifts': data}
    with open(filename, 'w') as file:
        yaml.dump(yaml_data, file, default_flow_style=False, sort_keys=False)
    logging.info(f"Data written to {filename}")

# Read URL from the urlSecret file
with open("urlSecret", "r") as file:
    url = file.read().strip()

print(f"Thank you for choosing Snippy! Now scraping for URL: {url}!\n\n")

# Scrape the product titles and write the results to YAML
product_titles = scrape_product_titles(url)
write_to_yaml(product_titles)