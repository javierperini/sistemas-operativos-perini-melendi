from Programa import *
from Instruccion import *
import unittest


class Disco:
    def __init__(self):
        self.programas = []
        self.indice = 0

    def agregarPrograma(self, programa):
        self.programas.append(programa)
        self.indice += 1

    def getPrograma(self, indice):
        return self.programas[indice]

    def tamanioOcupado(self ):
        return len(self.programas)


class TestsDisco(unittest.TestCase):

    def setUp(self):
        self.disco = Disco()
        self.programa = Programa()
        self.programa2 = Programa()

    def test_agregarUnPrograma(self):
        self.disco.agregarPrograma(self.programa)
        self.assertEquals(self.programa, self.disco.getPrograma(0))

    def test_tamanioOcupadoEnDisco(self):
         self.disco.agregarPrograma(self.programa)
         self.disco.agregarPrograma(self.programa2)
         self.assertEquals(2, self.disco.tamanioOcupado())


suite = unittest.TestLoader().loadTestsFromTestCase(TestsDisco)
unittest.TextTestRunner(verbosity=2).run(suite)

