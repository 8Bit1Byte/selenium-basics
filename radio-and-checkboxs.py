from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver_paths import *
import time


driver = webdriver.Chrome(executable_path = paths[0])
url = 'https://www.techlistic.com/p/selenium-practice-form.html'
driver.get(url)

# For checkbox
element = driver.find_element(By.ID, 'tool-0')
element.click()
print(element.is_selected(), element.is_enabled(), element.is_displayed())

# For radio-button
element = driver.find_element(By.ID, 'exp-0')
element.click()
print(element.is_selected(), element.is_enabled(), element.is_displayed())


time.sleep(5)
driver.quit()