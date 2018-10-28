import time
"""
Class Name: PageIndex
Objetivo: manejar y detectar elementos y funciones de la pagina principal
"""
class PageIndex():
    """
    Constructor: sobreescribe el metodo __init__()
    """
    def __init__(self,myDriver):
        # Pasamos por parametro el webdriver
        self.driver = myDriver
        self.register_link = self.driver.find_element_by_link_text("REGISTER")
        self.user_box = self.driver.find_element_by_name("userName")
        self.pass_box = self.driver.find_element_by_name("password")
        self.submit_button = self.driver.find_element_by_name("login")

    def clic_register(self):
        self.register_link.click()

    def login(self,user,passsword):

        self.user_box.send_keys(user)
        self.pass_box.send_keys(passsword)
        self.submit_button.click()
        time.sleep(3)