from Memoria import *
import unittest

class TestsMemoria(unittest.TestCase):

    def setUp(self):
        self.memoria = Memoria()
        self.memoria.write(0, "primeraInstruccion")
        self.memoria.write(1, "segundaInstruccion")

    def test_siguientePosicion(self):
        self.assertEquals(2, self.memoria.siguientePosicion)

    def test_hayEspacioParaGuardar(self):
        self.assertTrue(self.memoria.hayEspacioParaGuardar(10))

    def test_readMemoria(self):
        self.assertEqual("primeraInstruccion", self.memoria.read(0))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsMemoria)
unittest.TextTestRunner(verbosity=2).run(suite)