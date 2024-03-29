import unittest
from Kernel.Programa import *
from Disc.Instruccion import *

import unittest
from Kernel.Programa import Programa
from Disc.Instruccion import Instruccion


class ProgramaTest(unittest.TestCase):
    def setUp(self):

        self.progr = Programa("un_programa")
        self.instr = Instruccion('Instruccion 1')
    #Action
        self.progr.agregarInstruccion(self.instr)

    def test_agregarInstruccionCompararTamanho(self):
    #Assert
        self.assertEquals(1, len(self.progr.getInstrucciones()))

    def test_agregarInstruccionCompararElementos(self):
    #Assert
        self.assertEquals(self.progr.getElemento(0), self.instr)

    def test_instruccionesOrdenadasEnOutput(self):
        self.progr.ejecutar()
     #Assert
        self.assertEquals('Instruccion 1', self.progr.getInstruccionEjecutada(0))

suite = unittest.TestLoader().loadTestsFromTestCase(ProgramaTest)
unittest.TextTestRunner(verbosity=2).run(suite)