import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from driver_paths import *
# from driver_obj import *

# driver = drivers[0]
driver = webdriver.Chrome(executable_path=paths[0])

# TO OPEN URL IN WEBBROWSER USE [webdriver.chrome().get] FUNCTION
driver.get('https://phptravels.com/demo/')
# TO GET TITLE OF THE PAGE
print(driver.title)
# TO GET THE CURRENT URL
print(driver.current_url)
# TO GET PAGE SOURCE
i = input('0 or 1')
if i == '1':
    print(driver.page_source)
# TO CLICK ON BUTTON AND FIND IT BY IN HTML

time.sleep(3)
button = driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/a')
button.click()

# TO CLOSE THE BROWSER
driver.close()