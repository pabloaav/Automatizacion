#from xml.etree import ElementTree
from xml.dom import minidom
class xmlReader:
    # se levanta un archivo xml
    def __init__(self):
        self.documento = minidom.parse('./Config/configuration.xml')


    def obtener_datos(self,dato):
        """
        Retorna un string con el valor del parametro dato
        :param dato: etiqueta HTML que se busca conocer su dato
        :return: un string con el valor del parametro dato
        """
        # El valor [0] se refiere a la primer coincidencia que encuentra. Puede haber muchas
        item = self.documento.getElementsByTagName(dato)[0].firstChild.nodeValue
        return item
