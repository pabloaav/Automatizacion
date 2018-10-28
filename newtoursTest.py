import unittest
from selenium import webdriver
from Pages.pageIndex import *
from Pages.pageRegister import *

"""
Se define una clase que hereda de unittes.TestCase
"""
class NewTours (unittest.TestCase):
    """
    El metodo setUp define e implementa las operaciones basicas
    inciailes para los casos de prueba, y que resultan repetitivas y generales.
    Método para configurar el dispositivo de prueba antes de ejercitarlo.
    """
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        # Instanciar objeto tipo PageIndex y un objeto PageRegister
        self.index_page = PageIndex(self.driver)
        self.register_page = PageRegister(self.driver)
        time.sleep(3)
    """
    Seccion de Test Cases: se colocan aqui los casos de prueba
    """
    def test_register(self):
        self.index_page.clic_register()
        self.register_page.country_select_index(4)
        self.register_page.country_select_value("11")
        self.register_page.country_select_visibleText("CONGO")
        self.register_page.verify_country("ITALY")


    def test_login(self):
        self.index_page.login("test","test")
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEqual(link_registration_form.text, "registration form")

    """
    Finalizar el unti Test con tearDown()
    """
    def tearDown(self):
        self.driver.quit()