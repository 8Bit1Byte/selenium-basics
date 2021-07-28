import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver_paths import *

url = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'
driver = webdriver.Chrome(executable_path = paths[0])
driver.get(url)

# How many input box are there in webpage
elements = driver.find_elements(By.CSS_SELECTOR, 'input[class=whsOnd\\ zHQkBf]')
print(len(elements))
# How many way input box can be filled
fill_form = ['David', 'Miller', 'daviddddmillerrrr', 'thisispasss', 'thisispasss']
for i, j in zip(fill_form, elements):
    j.send_keys(i)
# How to get the status

filled_1 = elements[0]
print(filled_1.is_displayed(), filled_1.is_enabled(), filled_1.is_selected())
time.sleep(5)
driver.quit()
