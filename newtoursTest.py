import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
"""
Se define una clase que hereda de unittes.TestCase
"""
class NewTours (unittest.TestCase):
    """
    El metodo setUp define e implementa las operaciones basicas
    inciailes para los casos de prueba, y que resultan repetitivas y generales
    """
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        time.sleep(3)
    """
    Seccion de Test Cases: se colocan aqui los casos de prueba
    """
    def test_dropdown(self):
        self.driver.find_element_by_link_text("REGISTER").click()
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(4)
        time.sleep(2)
        countryDropDown.select_by_value("11")
        time.sleep(2)
        countryDropDown.select_by_visible_text("CONGO")
        time.sleep(2)
        self.assertEquals(countryDropDown.first_selected_option.text.strip(),"CONGO")
    def test_register(self):
        user_box = self.driver.find_element_by_name("userName")
        pass_box = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_name("login")
        user_box.send_keys("test")
        pass_box.send_keys("test")
        submit_button.click()
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEqual(link_registration_form.text, "registration form")
    """
    Finalizar el unti Test con tearDown()
    """
    def tearDown(self):
        self.driver.quit()