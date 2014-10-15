import Programa
from Memoria import *
import unittest


class AdministradorDeMemoria:
    def __init__(self, memoria):
        self.memoria = memoria

    def almacenar(self, programa):
        if self.memoria.hayEspacioPara(programa.size()):
                self.safeAlmacenar(programa)

    def safeAlmacenar(self, programa):
        for instr in programa.instrucciones():
            self.memoria.write(self.siquientePosicion(), instr)

    def siguientePosicionAdm(self):
        return self.memoria.siguientePosicion()


class TestsAdmin(unittest.TestCase):

    def setUp(self):
        self.memoria = Memoria()
        self.admin = AdministradorDeMemoria(self.memoria)
        self.programa1 = Programa()
        self.instr = Instruccion('Instruccion 1')
        self.programa1.agregarInstruccion(self.instr)
        self.admin.almacenar(self.programa1)

    def test_siguientePosicionAdmin(self):
        self.assertEquals(1, self.admin.siguientePosicionAdm())


suite = unittest.TestLoader().loadTestsFromTestCase(TestsAdmin)
unittest.TextTestRunner(verbosity=2).run(suite)
