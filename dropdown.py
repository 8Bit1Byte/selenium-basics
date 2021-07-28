from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from driver_paths import *
import time

url = 'https://www.google.co/'
driver = webdriver.Chrome(executable_path = paths[0])
driver.get(url)

element = driver.find_element(By.CLASS_NAME, 'gb_Ve')
element.click()

# NOTE :  Select only works on <select> elements, not on <svg>
# sel = Select(element)
# sel.options => list all option in list format
# print(sel.select_by_index(0))
elements = driver.find_elements(By.CSS_SELECTOR, 'li[class=j1ei8c]')
print(elements)
print(len(elements))
time.sleep(5)
driver.quit()