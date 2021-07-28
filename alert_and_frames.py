from selenium import webdriver
from selenium.webdriver.common.by import By
from driver_paths import *
import time

url = 'https://testautomationpractice.blogspot.com/'
driver = webdriver.Chrome(executable_path = paths[0])

def alert_box():    
    '''
    WE CAN SWITCH BETWEEN MAIN WINDOW AND ALERT BOX
    switch_to_alert().accept()
    switch_to_alert().dismiss()
    '''
    driver.get(url)
    element = driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button')
    element.click()
    time.sleep(3)
    # driver.switch_to_alert().accept()
    driver.switch_to_alert().dismiss()

def frame_swap():
    '''
    WE CAN SWITCH BETWEEN ONE FRAME AND OTHER
    switch_to.default_content()
    switch_to.frame(name)
    switch_to.frame(id)
    '''
    pass

time.sleep(5)
driver.quit()