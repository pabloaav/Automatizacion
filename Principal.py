from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
"""
Loads a web page in the current browser session.
El metodo get de web driver implementa el metodo GET HTTP,
obteniendo o trayendo la url pasada como parametro
"""
driver.get('http://newtours.demoaut.com/')

"""
Por medio del objeto driver que manipula la API de comunicacion con el browser,
hacemos uso de metodos predefinidos en el webdriver de Selenium para Chrome.
"""
user_box = driver.find_element_by_name("userName")
pass_box = driver.find_element_by_name("password")
submit_button = driver.find_element_by_name("login")

"""
Una vez cargados los elementos, podemos interactuar con ellos, por medio de las variables definidas
indicandole acciones, a traves de metodos de prueba 
"""
user_box.send_keys("test")
pass_box.send_keys("test")
submit_button.click()