"""
This module contains the CamelCamel_scraper class, which is used to scrape product details, such as the lowest price, from an Amazon product page on the CamelCamelCamel website. It uses the selenium webdriver to navigate to the webpage and BeautifulSoup to parse the page's HTML to extract the necessary details.
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import re


class CamelCamel_scraper:
    """
    A web scraper class to fetch the lowest price of a product from the CamelCamelCamel website using an Amazon product URL.

    Attributes:
        path (str): The path to the chromedriver executable.
        driver (selenium.webdriver.Chrome): The webdriver object used to interact with the webpage.
        amazon_url (str): The URL of the Amazon product to fetch details for.
    """

    def __init__(self, URL):
        """
        Initializes the CamelCamel_scraper with the path to the chromedriver executable, creates a new webdriver object, and sets the Amazon product URL.

        Args:
            URL (str): The URL of the Amazon product to fetch details for.
        """
        self.path = "C:\\Users\\Ashley\\Downloads\\chromedriver-win64\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.amazon_url = URL

    def _get_camel_url(self):
        """
        (Private Method)
        Extracts the product ID from the Amazon URL and constructs the CamelCamelCamel URL for the product.

        Returns:
            str: The CamelCamelCamel URL for the product.
            or
            str: A message indicating that the product ID could not be found.
        """
        product_id = re.findall(r'/dp/(\w+)', self.amazon_url)
        if product_id:
            self.camel_url = f"https://camelcamelcamel.com/product/{product_id[0]}"
            return self.camel_url
        else:
            return "Product ID not found"

    def get_lowest_camel_price(self):
        """
        Gets the lowest price of the product from the CamelCamelCamel website.

        The method constructs the CamelCamelCamel URL for the product, navigates to the page, gets the page source, and uses BeautifulSoup to parse the HTML and extract the lowest price.

        Returns:
            float: The lowest price of the product.
        """
        camel_url = self._get_camel_url()  # Call the _get_camel_url method to get the camel URL
        self.driver.get(camel_url)  # Navigate to the camel URL using selenium
        page_source = self.driver.page_source  # Get the page source
        soup = BeautifulSoup(page_source, "html.parser")  # Parse the page source with Beautiful Soup

        # Find the lowest price element, get its text, remove the dollar sign and convert it to a float
        lowest_price = soup.select_one(".pricetype0+ div .lowest_price td:nth-child(2)").getText().strip('$')
        lowest_price = float(lowest_price)

        self.driver.quit()  # Quit the driver to close the browser
        return lowest_price
