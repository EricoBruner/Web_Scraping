from selenium import webdriver

import json

url = "http://191.253.103.90"

drive = webdriver.Chrome()

drive.get(url)

drive.quit()