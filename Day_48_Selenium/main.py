from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open afte program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# price_dollar = driver.find_element(By.CSS_SELECTOR, value="#corePrice_desktop span")
#
#
# print(f"The price is {price_dollar.text}")

bug_link = driver.find_element(By.XPATH, value= '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

print(bug_link.text)


# driver.close()

# driver.quit()