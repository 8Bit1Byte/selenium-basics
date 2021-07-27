from selenium import webdriver
from driver_paths import *

drivers = [
    webdriver.Chrome(executable_path=paths[0]),
    webdriver.Edge(executable_path=paths[1]),
    webdriver.Firefox(executable_path=paths[2])
    ]