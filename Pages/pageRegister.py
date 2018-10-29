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
        Select(self.driver.find_element(*self.countryDropDown)).select_by_index(index)
        time.sleep(2)

    def country_select_value(self,value):
        Select(self.driver.find_element(*self.countryDropDown)).select_by_value(value)
        time.sleep(2)

    def country_select_visibleText(self,text):

        Select(self.driver.find_element(*self.countryDropDown)).select_by_visible_text(text)
        time.sleep(2)

    def verify_country(self,country):

        testCase = unittest.TestCase('__init__')
        testCase.assertEqual(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip(),country)
        testCase.assertTrue(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip()==country)
        testCase.assertFalse(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip()!=country)

