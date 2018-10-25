from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')
"""
Loads a web page in the current browser session.
El metodo get de web driver implementa el metodo GET HTTP,
obteniendo o trayendo la url pasada como parametro
"""
driver.get('http://newtours.demoaut.com/')

#damos tiempo a que cargue la pagina
time.sleep(3)

"""
El XPath es la ruta o camino de un arbol, donde cada rama es una etiqueta HTML
Permite identificar elementos cuando no tienen otro atributo mas oportuno
"""
user_box = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[2]/td[3]/form[1]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")
# pass_box = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[2]/td[3]/form[1]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[3]/td[2]/input[1]")
# Tambien se puede usar el CSS selector como Path
pass_box = driver.find_element_by_css_selector("table:nth-child(1) tbody:nth-child(1) tr:nth-child(3) td:nth-child(2) > input:nth-child(1)")
submit_button = driver.find_element_by_name("login")

"""
Una vez cargados los elementos, podemos interactuar con ellos, por medio de las variables definidas
indicandole acciones, a traves de metodos de prueba 
"""
user_box.send_keys("test")
pass_box.send_keys("test")
submit_button.click()
# Tiempo de carga
time.sleep(3)
# Cerramos el browser
driver.quit()