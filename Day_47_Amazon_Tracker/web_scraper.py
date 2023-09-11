"""
This module contains the Web_scraper class which can be used to scrape product details, such as price, from an Amazon product page.
It uses the selenium webdriver to interact with the webpage and BeautifulSoup to parse the page's HTML and extract the necessary details.
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time


class Web_scraper:
    """
    A web scraper for fetching product details from an Amazon product page.

    Attributes:
        path (str): The path to the chromedriver executable.
        driver (selenium.webdriver.Chrome): The webdriver object used to interact with the webpage.
    """

    def __init__(self):
        """
        Initializes the Web_scraper with the path to the chromedriver executable and creates a new webdriver object.
        """
        self.path = "C:\\Users\\Ashley\\Downloads\\chromedriver-win64\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def get_product_price(self, URL):
        """
        Fetches the product price from the Amazon product page at the specified URL.

        The method navigates to the page, gets the page source and uses BeautifulSoup to parse the HTML and extract
        the product price, which is calculated as the sum of the whole price and the fractional price.

        Args:
            URL (str): The URL of the Amazon product page to scrape.

        Returns:
            float: The product price.

        Raises:
            ValueError: If the price elements cannot be found on the page.
        """
        # Navigate to the URL
        self.driver.get(URL)
        time.sleep(30)  # Wait for the page to load

        # Get the page source and parse it with BeautifulSoup
        amazon_webpage = self.driver.page_source
        soup = BeautifulSoup(amazon_webpage, "lxml")

        # Get the whole and fractional parts of the price and calculate the total price
        try:
            whole_price = float((soup.select_one("span.a-price-whole").getText().strip(".")).replace(',', ''))
            price_fraction = float(soup.select_one("span.a-price-fraction").getText()) / 100
            Product_Price = whole_price + price_fraction
        except AttributeError:
            self.driver.quit()
            raise ValueError("Could not find price elements on the page.")

        self.driver.quit()  # Close the browser
        return Product_Price
