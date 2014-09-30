from Output import *
import unittest


class Instruccion:
    def __init__(self, text):
        self.texto = text

    def run(self, output):
        output.agregarInstruccion(self.texto)


class TestsOutput(unittest.TestCase):

    def setUp(self):
        self.output2 = Output()
        self.instruccion = Instruccion("soy una instruccion")

    def test_correrUnaInstruccion(self):
        self.instruccion.run(self.output2)
        self.assertEquals("soy una instruccion", self.output2.get(0))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsOutput)
unittest.TextTestRunner(verbosity=2).run(suite)
