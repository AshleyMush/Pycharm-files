from web_scraper import Web_scraper
from camelcamel_webscraper import CamelCamel_scraper
from Notification_manager import Notification_Manager

"""
Keep checking and inspecting the amazon website to make sure the elements in web scraper and camel camel are correct

"""

receiving_email = "tanaka.mush@gmail.com"
AMAZON_URL = "https://www.amazon.com/iPhone-13-Pro-256GB-Graphite/dp/B0BGYBX3LK/ref=sr_1_1?crid=2DA5GYPTFSPWT&keywords=iphone%2B14&qid=1694167126&sprefix=iphone%2B14%2Caps%2C224&sr=8-1&th=1"

web_scraper = Web_scraper()
Camel_Scraper = CamelCamel_scraper(AMAZON_URL)

#___________________________________________________
LOWEST_PRICE_camelcamelcamel = Camel_Scraper.get_lowest_camel_price()
AMAZON_product_price = web_scraper.get_product_price(AMAZON_URL)


price_diference = AMAZON_product_price - LOWEST_PRICE_camelcamelcamel


Notification_Manager = Notification_Manager(LOWEST_PRICE=LOWEST_PRICE_camelcamelcamel)

if AMAZON_product_price<= LOWEST_PRICE_camelcamelcamel:
    Notification_Manager.send_email(receiving_email=receiving_email)
else:
    print(f"The product is {price_diference} more expensive than it's lowest price.")




