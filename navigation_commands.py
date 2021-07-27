from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from driver_paths import *
import time

driver = webdriver.Chrome(executable_path = paths[0])
links = ['https://www.phptravels.net/', 'https://phptravels.com/demo/']

driver.get(links[0])
driver.get(links[1])

def for_back_testing():    
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.forward()

for_back_testing()
driver.quit()