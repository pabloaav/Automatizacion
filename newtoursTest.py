from selenium import webdriver
from Pages.pageIndex import *
from Pages.pageRegister import *
import xmlrunner

"""
Se define una clase que hereda de unittes.TestCase
"""
class NewTours (unittest.TestCase):
    url = 'http://newtours.demoaut.com/'

    """
    El metodo setUp define e implementa las operaciones basicas
    inciailes para los casos de prueba, y que resultan repetitivas y generales.
    Método para configurar el dispositivo de prueba antes de ejercitarlo.
    """
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get(self.url)
        # Instanciar objeto tipo PageIndex y un objeto PageRegister
        self.index_page = PageIndex(self.driver)
        self.register_page = PageRegister(self.driver)
    """
    Seccion de Test Cases: se colocan aqui los casos de prueba
    """
    def test_register(self):
        self.index_page.clic_register()
        self.register_page.country_select_index(4)
        self.register_page.country_select_value("11")
        self.register_page.country_select_visibleText("CONGO")
        self.register_page.verify_country("CONGO")


    def test_login(self):
        self.index_page.login("test","test")
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEqual(link_registration_form.text, "registration form")

    def test_login_by_tabs(self):
        self.index_page.login_by_tab("test","test")

    """
    Finalizar el unti Test con tearDown()
    """
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    """
    Generar reporte XML de los Test corridos
    Para ello hacemos un metodo main 
    """
if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='output'),
    #     failfast se utiliza para controlar posibles errores en el reporte
        failfast=False,
        buffer=False,
        catchbreak=False
    )