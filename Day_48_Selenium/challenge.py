from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.python.org"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
#
# print(event_times)
# for time in event_times:
#     print(time.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".last time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name": event_names[n].text

    }

print(events)


# new_dictionary = {new_key, new_val for key, value in dictionary }


#
# driver.quit()