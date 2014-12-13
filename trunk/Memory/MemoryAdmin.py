from Kernel.Programa import *
from Disc.Instruccion import *
from Memory import *
from MemoryOrganize import *
import unittest


class MemoryAdmin:

    def __init__(self, memory, strategy):
        self.memory = memory
        self.strategy = strategy

    def store(self, pcb, program):
        self.strategy.saveAlmacenar(pcb, program)

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
        self.admin = MemoryAdmin(self.memoria, AsignacionContinua(self.memoria))
        self.programa1 = Programa()
        self.instr = Instruccion('Instruccion 1')
        self.programa1.agregarInstruccion(self.instr)
        self.admin.store(self.programa1)

    def test_next_position_admin(self):
        self.assertEquals(1, self.admin.nextPost())


suite = unittest.TestLoader().loadTestsFromTestCase(TestsAdmin)
unittest.TextTestRunner(verbosity=2).run(suite)