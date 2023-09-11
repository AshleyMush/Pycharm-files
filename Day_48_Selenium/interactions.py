from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

URL = 'https://www.python.org/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a:nth-child(1)")
#
# print(article_count.text)

search= driver.find_element(By.CSS_SELECTOR, "#id-search-field")
# search_button = driver.find_element(By.CSS_SELECTOR, ".vector-search-box-button")

search.send_keys("Python")
search.send_keys(Keys.ENTER)
# search_button.click()


