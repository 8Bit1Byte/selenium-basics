from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver_paths import *
import time
from selenium.webdriver.remote.webelement import WebElement
url = 'https://en.wikipedia.org/wiki/Carmen'
driver = webdriver.Chrome(executable_path = paths[0])
driver.get(url)

elements = driver.find_elements(By.TAG_NAME, 'a')
print(len(elements))
# for i in elements:
#     print(i.link)
elements = driver.find_elements(By.LINK_TEXT, 'Glenn Ford')
print(len(elements))
elements = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Geo')
print(len(elements))
time.sleep(5)
driver.quit()