from selenium import webdriver
from Helpers.data import TestData
from Helpers.xmlReader import xmlReader
from Pages.pageIndex import *
from Pages.pageRegister import *
import xmlrunner
import HtmlTestRunner
import unittest
import sys
"""
Se define una clase que hereda de unittes.TestCase
"""


class NewTours(unittest.TestCase):

    """
    El metodo setUp define e implementa las operaciones basicas
    inciailes para los casos de prueba, y que resultan repetitivas y generales.
    Método para configurar el dispositivo de prueba antes de ejercitarlo.
    """

    def setUp(self):
        # obtener datos a traves de un XML document
        self.configuracion = xmlReader()
        # Si el navegador que testeamos es chrome entonces...
        if self.configuracion.obtener_datos('browser') == 'chrome':
            self.driver = webdriver.Chrome('chromedriver.exe')
        else:
            self.driver = webdriver.PhantomJS()
        self.driver.get(self.configuracion.obtener_datos('url'))
        # self.driver = webdriver.Chrome('chromedriver.exe')
        # Hacemos uso de PhantomJS para acelerar las pruebas en cuanto a tiempo total de ejecucion
        # self.driver = webdriver.PhantomJS()
        # self.driver.get(self.url)
        # Instanciar objeto tipo PageIndex y un objeto PageRegister
        self.index_page = PageIndex(self.driver)
        self.register_page = PageRegister(self.driver)

    """
    Seccion de Test Cases: se colocan aqui los casos de prueba
    """

    def test_register(self):
        country_DataSet = TestData()
        self.index_page.clic_register()
        self.register_page.country_select_index(4)
        self.register_page.country_select_value("11")
        self.register_page.country_select_visibleText(country_DataSet.country)
        self.register_page.verify_country("CONGO")

    # @unittest.skip("Omitir por ahora")
    # @unittest.skipIf(5 > 4, "Si la expresion logica resulta verdadera, se omite el test")
    @unittest.skipUnless(sys.platform.startswith('linux'),"A menos que sea Linux")
    def test_login(self):
        self.index_page.login("test", "test")
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEqual(link_registration_form.text, "registration form")

    def test_login_by_tabs(self):
        self.index_page.login_by_tab("test", "test")

    """
    Finalizar el unti Test con tearDown()
    """

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))

    # """
    # Generar reporte XML de los Test corridos
    # Para ello hacemos un metodo main
    # """
# if __name__ == '__main__':
#     unittest.main(
#         testRunner=xmlrunner.XMLTestRunner(output='output'),
#     #     failfast se utiliza para controlar posibles errores en el reporte
#         failfast=False,
#         buffer=False,
#         catchbreak=False
#     )
