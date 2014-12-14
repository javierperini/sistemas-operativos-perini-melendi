import unittest

from Memory.Memory import *


class TestsMemoria(unittest.TestCase):

    def setUp(self):
        self.memoria = Memory()
        self.memoria.write(0, "primeraInstruccion")
        self.memoria.write(1, "segundaInstruccion")

    def test_siguientePosicion(self):
        self.assertEquals(2, self.memoria.next_position)

    def test_hayEspacioParaGuardar(self):
        self.assertTrue(self.memoria.free_memory_to_save(10))

    def test_readMemoria(self):
        self.assertEqual("primeraInstruccion", self.memoria.read(0))

    def test_deleteMemoria(self):
        self.memoria.delete("primeraInstruccion")
        self.assertEquals(511, self.memoria.free_cells)

    def test_size(self):
        self.assertEqual(512, self.memoria.size)

suite = unittest.TestLoader().loadTestsFromTestCase(TestsMemoria)
unittest.TextTestRunner(verbosity=2).run(suite)