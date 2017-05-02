from selenium import webdriver
from promise import Promise

driver = webdriver.Firefox()
driver.set_window_size(1500, 1000)
driver.maximize_window()

def setUp():
	return driver

def teardown():
	driver.quit()

