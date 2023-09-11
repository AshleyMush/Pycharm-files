from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "http://secure-retreat-92358.herokuapp.com/"

first_name_TEXT = "Ashley"
last_name_TEXT = "Mush"
email_TEXT = "tanaka.mush@gmail.com"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Selecting the elements
first_name_bar = driver.find_element(By.CSS_SELECTOR, ".form-control.top")
last_name_bar = driver.find_element(By.CSS_SELECTOR, ".form-control.middle")
email_bar = driver.find_element(By.CSS_SELECTOR, ".form-control.bottom")
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")

# Sending keys
first_name_bar.send_keys(first_name_TEXT)
last_name_bar.send_keys(last_name_TEXT)
email_bar.send_keys(email_TEXT)
button.click()
