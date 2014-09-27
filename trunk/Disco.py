import numpy as np


class Disco:
    def __init__(self):
        self.programas = np.arrange(10000000)
        self.indice = 0

    def agregarPrograma(self, programa):
        self.programas[self.indice] = programa
        self.indice += 1

    def getPrograma(self, indice):
        return self.programas[indice]


