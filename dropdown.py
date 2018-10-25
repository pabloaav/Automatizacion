from selenium import webdriver
import time
# Libreria de Selects de Selenium
from selenium.webdriver.support.ui import Select

"""
dropdown: lista desplegable o menu desplegable
"""

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(3)

"""
Buscamos un enlace (link) dentro de la web por su texto,
y a ese link le hacemos un clic
"""
driver.find_element_by_link_text("REGISTER").click()
"""
Formamos un selector, con el elemento country del dropdown de la web
"""
countryDropDown = Select(driver.find_element_by_name("country"))
# Con el objeto selector formado, automatizamos la busqueda
countryDropDown.select_by_index(4)
time.sleep(2)
countryDropDown.select_by_value("11")
time.sleep(2)
countryDropDown.select_by_visible_text("CONGO")
time.sleep(2)
driver.quit()
