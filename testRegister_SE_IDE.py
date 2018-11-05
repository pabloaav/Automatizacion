# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestRegister(unittest.TestCase):
    """
    Esta clase fue generada por el metodo Record and Playback
    usando la herramienta Selenium IDE Katalon con Firefox
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_register(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        driver.find_element_by_link_text("REGISTER").click()
        driver.find_element_by_name("firstName").click()
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys("Juan")
        driver.find_element_by_name("lastName").click()
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys("Perez")
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("3794251245")
        driver.find_element_by_id("userName").click()
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("juanperez@hotmail.com")
        driver.find_element_by_name("country").click()
        Select(driver.find_element_by_name("country")).select_by_visible_text("ARGENTINA")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Country:'])[1]/following::option[9]").click()
        driver.find_element_by_name("address1").click()
        driver.find_element_by_name("address1").clear()
        driver.find_element_by_name("address1").send_keys("Salta 1250")
        driver.find_element_by_name("city").click()
        driver.find_element_by_name("city").clear()
        driver.find_element_by_name("city").send_keys("Corrientes")
        driver.find_element_by_name("state").click()
        driver.find_element_by_name("state").clear()
        driver.find_element_by_name("state").send_keys("Corrientes")
        driver.find_element_by_name("postalCode").click()
        driver.find_element_by_name("postalCode").clear()
        driver.find_element_by_name("postalCode").send_keys("3400")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("juan")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("juanperez")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::td[1]").click()
        driver.find_element_by_name("confirmPassword").click()
        driver.find_element_by_name("confirmPassword").clear()
        driver.find_element_by_name("confirmPassword").send_keys("juanperez")
        driver.find_element_by_name("register").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
