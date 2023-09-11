from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the web driver (in this example, we're using Chrome)
driver = webdriver.Chrome(executable_path='C:\\Users\\Ashley\\Downloads\\chromedriver_win32\\chromedriver.exe')


# Open the Amazon webpage
URL = "https://www.amazon.com/STGAubron-Desktop-i9-11900F-GeForce-Keyboard/dp/B0C6V15KVK/ref=sr_1_2_sspa?crid=2LXYMR9M1KJI1&keywords=GAMING%2BPC&qid=1694064609&sprefix=gaming%2Bpc%2Caps%2C206&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
driver.get(URL)

# Pause the script for manual CAPTCHA intervention
input("Solve the CAPTCHA and then press Enter to continue...")

# Once CAPTCHA is solved, you can continue with your scraping
# For example, to get the page source:
page_source = driver.page_source

# Don't forget to close the driver once done
driver.quit()
