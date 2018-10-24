from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
"""
Loads a web page in the current browser session.
El metodo get de web driver implementa el metodo GET HTTP,
obteniendo o trayendo la url pasada como parametro
"""
driver.get('http://newtours.demoaut.com/')
