from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from driver_paths import *
import time

driver_path = paths[0]
path = 'https://www.techlistic.com/p/selenium-practice-form.html'

'''
    - is_selected \
                    => Both can be used with any kind of web element
    - is_enabled  /
    - is_displayed => Checkbox and radio buttons only
'''
driver = webdriver.Chrome(executable_path = driver_path)
driver.get(path)
button = driver.find_element_by_id('sex-0')

cond_1 = button.is_selected()
cond_2 = button.is_enabled()
cond_3 = button.is_displayed()
print('YES' if cond_1 else 'NO', ' (Selected)')
print('YES' if cond_1 else 'NO', ' (Enabled)')
print('YES' if cond_1 else 'NO', ' (Displayed)')


# FILL THE FORM USING (send_keys) function
def fill_form():
    input_box1 = driver.find_element_by_name('firstname')
    input_box2 = driver.find_element_by_name('lastname')

    input_box1.send_keys('First Name')
    input_box2.send_keys('Last Name')

# 
def css_selector():
    radio_button = driver.find_element_by_css_selector('input[name=lastnames]')
    print(radio_button.is_enabled())
    print(radio_button.is_selected())
    print(radio_button.is_displayed())


fill_form()
css_selector()
time.sleep(5)
driver.quit()