# Snippy Scraper

## Overview

The Snippy Scraper is a Python script designed to extract product titles from dynamically generated web pages using Selenium. This project addresses the challenge of scraping content loaded via JavaScript, which traditional scraping tools like BeautifulSoup cannot handle. The output is saved in a neatly formatted YAML file.

## Features

Dynamic Web Page Handling: Uses Selenium to interact with and extract data from JavaScript-heavy web pages.
Automatic WebDriver Management: Utilizes webdriver-manager to handle browser driver requirements automatically.
YAML Output: Structures the extracted data into a YAML file for easy use and integration with other systems.

## Installation
### Prerequisites
Python 3.x
pip
Chrome Browser (or any other browser of your choice but ensure you have the corresponding WebDriver)

### Setup
Clone the Repository:
    git clone https://github.com/your-username/snippy-scraper.git
    cd snippy-scraper

### Install Dependencies:
```pip install selenium pyyaml webdriver-manager```

### Set Up URL Secret:
Edit the file named `urlSecret.txt` in the project root.
Add the URL of the page you want to scrape to this file.

### (Optional) ChromeDriver Setup:
If you prefer not to use webdriver-manager, manually download ChromeDriver and specify the path in `chromedriverPath.txt`.

## Usage
Run the script using Python from the command line:

```python snappy.py```

The script will scrape the web page specified in `urlSecret.txt` and output the results in `output.yaml`.

### Output
The output will be a YAML file named `output.yaml` containing the extracted product details structured as follows:

    snappyGifts:
      - name: Product Name
        productTitleID: ID1234567890

## Licensing

### Non-Commercial Use: 
This project is available under the CC0 v1.0 Universal license for individuals, non-profits, educational institutions, and for other non-commercial purposes. See the LICENSE file for more details.

### Commercial Use: 
Commercial use is restricted and requires a license. Please see the LICENSECOMMERCIAL.md for details on obtaining a commercial license.

## Contributing
Contributions to the Snippy Scraper are welcome. Please ensure you adhere to the provided coding and commit guidelines. For major changes, please open an issue first to discuss what you would like to change.

For more information on contributing to this project, please read CONTRIBUTING.md.

## Support
For support and queries, please open an issue in the repository, and we will try to address it as soon as possible.