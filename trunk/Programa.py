from Kernel import *
from Output import *
from Instruccion import *
import unittest
import numpy as np


class Programa:

    def __init__(self):
        self.instrucciones = np.arange(1000000)
        self.output = Output()
        self.indice = 0

    def agregarInstruccion(self, instruccion):
        self.instrucciones[self.indice] = instruccion
        self.indice += 1

    def ejecutar(self):
        for instruccion in self.instrucciones:
            instruccion.run(self.output)

    def getInstrucciones(self):
        return self.instrucciones

    def getElemento(self,posicion):
        return self.instrucciones[posicion]

    def getInstruccionEjecutada(self,indice):
        return self.output.get(indice)


class ProgramaTest(unittest.TestCase):
    def setUp(self):

        self.progr = Programa()
        self.instr= Instruccion('Instruccion 1')
    #Action
        self.progr.agregarInstruccion(self.instr)

    def test_agregarInstruccionCompararTamanho(self):
    #Assert
        self.assertEquals(1, len(self.progr.getInstrucciones()))

    def test_agregarInstruccionCompararElementos(self):
    #Assert
        self.assertEquals(self.progr.getElemento(0), self.instr)

    def test_instruccionesOrdenadasEnOutput(self):
    #Assert
        self.assertEquals('Instruccion1', self.progr.getInstruccionEjecutada(0))

suite = unittest.TestLoader().loadTestsFromTestCase(ProgramaTest)
unittest.TextTestRunner(verbosity=2).run(suite)
