import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://191.253.103.90');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()