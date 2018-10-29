import time

from selenium.webdriver.common.by import By

"""
Class Name: PageIndex
Objetivo: manejar y detectar elementos y funciones de la pagina principal
"""
class PageIndex():
    """
    Constructor: sobreescribe el metodo __init__()
    """
    def __init__(self,myDriver):
        """
        :param myDriver: el objeto tipo webdriver o manejador de pagina web
        Este metodo instancia el pageIndex object y define las variables de busqueda de elementos
        """
        self.driver = myDriver
        self.user_box = (By.NAME,"userName")
        self.pass_box = (By.NAME,"password")
        self.register_link = (By.LINK_TEXT,"REGISTER")
        self.submit_button = (By.NAME,"login")

    def clic_register(self):
        """
        :return: un link de tipo registro de usuario, y la accion asociada a el
        """
        # Implicit Wait para esperar solo lo necesario para que cargue el objeto y no más
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.register_link).click()

    def login(self,user,password):
        """
        :param user: texto del campo de usuario
        :param passsword: clave
        :return: acciones asociadas a los elementos encontrados en el formulario de autenticacion
        """
        # Implicit Wait para esperar solo lo necesario para que cargue el objeto y no más
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.user_box).send_keys(user)
        self.driver.find_element(*self.pass_box).send_keys(password)
        self.driver.find_element(*self.submit_button).click()


        time.sleep(3)