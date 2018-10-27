from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com.ar/')

time.sleep(3)
search_box = driver.find_element_by_id("lst-ib")
#search_box = driver.find_element_by_name("q")
search_box.send_keys("testing")

time.sleep(3)
driver.quit()