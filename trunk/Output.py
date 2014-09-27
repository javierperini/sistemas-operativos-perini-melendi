import numpy as np


class Output:
    def __init__(self):
        self.instrucciones = np.arange(10000)
        self.indice = 0

    def agregarInstruccion(self, instruccion):
        self.instrucciones[self.indice] = instruccion
        self.indice += 1

    def get(self, indice):
        return self.instrucciones[indice]

