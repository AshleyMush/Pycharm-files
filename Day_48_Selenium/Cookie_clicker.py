from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#Get cookie and money
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
money = int(driver.find_element(By.CSS_SELECTOR, "#money").text)

#Get store items
items  = driver.find_elements(By.CSS_SELECTOR, "div #store")

upgrade_list  = []

item_ids = [item.find_elements(By.CSS_SELECTOR, "b") for item in items]

print(item_ids)



timeout = time.time() + 5   # 5 sec from now
five_min = time.time() + 60*5 # 5minutes

# for store_item in item_ids:
#     upgrade_price = int(store_item.text.split('-')[1].replace(',', ''))
#     upgrade_list.append(upgrade_price)


while True:
    """
    2. Create a bot using Selenium and Python to click on the cookie as fast as possible.
    """
    cookie.click()


    """
    3. Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one. You'll need to check how much money (cookies) you have against the price of each upgrade.
                                                                        more money                      
    """
    if time.time() > timeout:
    for upgrade in upgrade_list:
        if money > upgrade:


"""
get cookie element
click on cookie 
get my score
get cursor score 
get grand ma score 


while score is < cursor:
    Click cookie button for (price_of_cursor) times
    if score == cursor:
    click on cursor
    
    if score == grandma:
    click on grandma
    
click cursor button


"""
