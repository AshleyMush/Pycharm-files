from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
PASSWORD = os.environ.get("linkedin_password")
EMAIL = os.environ.get("email")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path='C:/Users/Ashley/Downloads/chromedriver-win64/chromedriver.exe', options=chrome_options)
driver.get(LINKEDIN_URL)

#3. Using the URL and what you know about Selenium, try to open the page
sign_in_button_FIRST_PAGE = driver.find_element_by_css_selector(".btn-md.btn-secondary-emphasis")
sign_in_button_FIRST_PAGE.click()

#use sleep() to wait for page loads.
time.sleep(3)


#Setting up the log in bars
username_button = driver.find_element(By.ID, "username")
password_button = driver.find_element_by_id("password")
sign_in_button_LOGIN_PAGE = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
#organic-div > form > div.login__form_action_container > button
# Automatically login
username_button.send_keys(EMAIL)
password_button.send_keys(PASSWORD)
time.sleep(3)
sign_in_button_LOGIN_PAGE.click()

# <input id="username" name="session_key" type="text" aria-describedby="error-for-username" required="" validation="email|tel" class="selectorgadget_selected" autofocus="" aria-label="Email or Phone">
