from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from driver_paths import *
import time

'''
IMPLICIT WAIT ==>
def fill_details(firstname, lastname, username, password, confirmpassword):
    first_name.send_keys(firstname)
    last_name.send_keys(lastname)
    user_name.send_keys(username)
    passwd.send_keys(password)
    confirmpasswd.send_keys(confirmpassword)

url = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'
driver = webdriver.Chrome(executable_path = paths[0])
driver.get(url)

driver.implicitly_wait(10)
# assert 'Welcome to here' in driver.title
first_name = driver.find_element_by_id('firstName')
last_name = driver.find_element_by_id('lastName')
user_name = driver.find_element_by_id('username')
passwd = driver.find_element_by_name('Passwd')
confirmpasswd = driver.find_element_by_name('ConfirmPasswd')

# fill_details(first_name, last_name, user_name, passwd, confirmpasswd)
button_signup = driver.find_element_by_class_name('VfPpkd-vQzf8d')
button_signup.click()
'''
url = 'https://www.expedia.co.in/'
driver = webdriver.Chrome(executable_path = paths[0])
# driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)
# button_fight = driver.find_element_by_css_selector('a[aria-controls=wizard-flight-pwa]')
driver.find_element(By.CSS_SELECTOR, 'a[aria-controls=wizard-flight-pwa]').click()
driver.find_element(By.CSS_SELECTOR, 'button[data-stid=location-field-leg1-origin-menu-trigger]').click()
driver.find_element(By.ID, 'location-field-leg1-origin').send_keys('Delhi')
driver.find_elements(By.CSS_SELECTOR, 'button[data-stid=location-field-leg1-origin-result-item-button]')[0].click()
driver.find_element(By.CSS_SELECTOR, 'button[data-stid=location-field-leg1-destination-menu-trigger]').click()
driver.find_element(By.ID, 'location-field-leg1-destination').send_keys('Dubai')
driver.find_elements(By.CSS_SELECTOR, 'button[data-stid=location-field-leg1-destination-result-item-button]')[0].click()

driver.find_element(By.CSS_SELECTOR, 'button[data-testid=submit-button]').click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'preferred-airline-6E')))
element.click()
time.sleep(5)
driver.quit()