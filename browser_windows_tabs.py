'''
driver.current_window_handle
driver.window_handle
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver_paths import *
import time

url = 'http://demo.automationtesting.in/Windows.html'
driver = webdriver.Chrome(executable_path = paths[0])
driver.get(url)
handle_main = driver.current_window_handle
print(handle_main)

elements = driver.find_elements(By.CLASS_NAME, 'analystic')
element = elements[-1]
element.click()
time.sleep(3)
button = driver.find_element(By.XPATH, '//*[@id="Multiple"]/button')
button.click()

handles = driver.window_handles
for i in handles:
# for i in range(20):
#     driver.switch_to.window(handles[i%3])
    if driver.title == 'SeleniumHQ Browser Automation':
        print('Yes')
        driver.close()
    driver.switch_to.window(i)
    print(driver.title)
    time.sleep(0.5)

time.sleep(5)
driver.quit()