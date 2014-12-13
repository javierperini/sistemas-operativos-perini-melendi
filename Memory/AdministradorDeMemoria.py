import Programa
from Disc import Instruccion
import Memory
import unittest


class AdministradorDeMemoria:
    def __init__(self, memoria, strategy):
        self.memoria = memoria
        self.strategy = strategy

    def almacenar(self, pcb, programa):
        self.strategy.saveAlmacenar(pcb, programa)

    def hayEspacioPara(self, tamanio):
        self.strategy.hayEspacioPara(tamanio)

    def nextPost(self):
        return self.strategy.getNextInstruction()

    def readMemory(self, programa):
        return self.strategy.getNextInstruction(programa)

    def deleteMemory(self, programa):
        self.strategy.deleteMemory(programa)


class TestsAdmin(unittest.TestCase):

    def setUp(self):
        self.memoria = Memory()
        self.admin = AdministradorDeMemoria(self.memoria)
        self.programa1 = Programa()
        self.instr = Instruccion('Instruccion 1')
        self.programa1.agregarInstruccion(self.instr)
        self.admin.store(self.programa1)

    def test_next_position_admin(self):
        self.assertEquals(1, self.admin.nextPost())


suite = unittest.TestLoader().loadTestsFromTestCase(TestsAdmin)
unittest.TextTestRunner(verbosity=2).run(suite)