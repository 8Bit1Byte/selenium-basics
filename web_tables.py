from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from driver_paths import *
import time

url = 'https://www.techlistic.com/p/demo-selenium-practice.html'

driver = webdriver.Chrome(executable_path = paths[0])
driver.get(url)

elements = driver.find_elements_by_xpath('//*[@id="post-body-5867683659713562481"]/div/div[1]/table/tbody/tr')
print(len(elements))

time.sleep(5)
driver.quit()