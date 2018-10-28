import time
import unittest
from selenium.webdriver.support.ui import Select

class PageRegister():

    """
    Constructor: sobreescribe el metodo __init__()
    """
    def __init__(self,myDriver):
        # Pasamos por parametro el webdriver
        self.driver = myDriver
        self.countryDropDown = Select(self.driver.find_element_by_name("country"))
    def country_select_index(self,index):

        self.countryDropDown.select_by_index(index)
        time.sleep(2)

    def country_select_value(self,value):

        self.countryDropDown.select_by_value(value)
        time.sleep(2)

    def country_select_visibleText(self,text):

        self.countryDropDown.select_by_visible_text(text)
        time.sleep(2)

    def verify_country(self,name):

        testCase = unittest.TestCase('__init__')
        testCase.assertEqual(self.countryDropDown.first_selected_option.text.strip(), name)
        testCase.assertTrue(self.countryDropDown.first_selected_option.text.strip()==name)
        testCase.assertFalse(self.countryDropDown.first_selected_option.text.strip()==name)
