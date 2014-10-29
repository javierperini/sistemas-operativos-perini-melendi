
import unittest


class Memoria:
    def __init__(self):
        self.registros = []
        self.siguientePosicion = 0
        self.tamaño = 512
        self.celdasLibres = 512

    def read(self, posicion):
        return self.registros[posicion]

    def write(self, posicion, instruccion):
        self.registros.insert(posicion, instruccion)
        self.siguientePosicion += 1
        self.celdasLibres -= 1

    def siquientePosicion(self):
        return self.siguientePosicion

    def hayEspacioParaGuardar(self, tamanhoDelPrograma):
        return self.celdasLibres >= tamanhoDelPrograma

    def compactar(self):
        pass
        #agarrar todas las instrucciones y ponerlas juntas
        #marcar las celdas para saber si están ocupadas o no.

    def delete(self, indice):
        self.registros.remove[indice]


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
