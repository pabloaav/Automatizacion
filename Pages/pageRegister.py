import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class PageRegister():

    """
    Constructor: sobreescribe el metodo __init__()
    """
    def __init__(self,myDriver):
        # Pasamos por parametro el webdriver
        self.driver = myDriver
        self.countryDropDown = (By.NAME,"country")


    def country_select_index(self,index):
        """
        :param index: indice del dropdown
        :return: accion asociada al elemento obtenido Pais
        """
        # Implicit Wait para esperar solo lo necesario para que cargue el objeto y no más
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element(*self.countryDropDown)).select_by_index(index)
    #     tomamos un screenshot de esta seccion de codigo, guardandola como archivo:
        self.driver.get_screenshot_as_file('capturaCountryIndex.png')

    def country_select_value(self,value):
        # Implicit Wait para esperar solo lo necesario para que cargue el objeto y no más
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element(*self.countryDropDown)).select_by_value(value)
        #     tomamos un screenshot de esta seccion de codigo, guardandola como archivo, con save_screenshot:
        self.driver.save_screenshot('capturaCountryValue.jpg')

    def country_select_visibleText(self,text):
        # Implicit Wait para esperar solo lo necesario para que cargue el objeto y no más
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element(*self.countryDropDown)).select_by_visible_text(text)

    def verify_country(self,country):

        testCase = unittest.TestCase('__init__')
        testCase.assertEqual(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip(),country)
        testCase.assertTrue(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip()==country)
        testCase.assertFalse(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip()!=country)

