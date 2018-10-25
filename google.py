from selenium import webdriver
import time
# Libreria de Selects de Selenium
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(3)
