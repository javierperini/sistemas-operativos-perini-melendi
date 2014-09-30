import numpy as np


class Memoria:
    def __init__(self):
        self.registros = []
        self.siguientePosicion = 0

    def read(self, posicion):
        return self.registros[posicion]

    def write(self, posicion, instruccion):
        self.registros[posicion] = instruccion

    def siquientePosicion(self):
        return self.siguientePosicion

    def hayEspacioPara(self, tamanhoDelPrograma):
        return (self.resgistros.size() - self.siguientePosicion()) > tamanhoDelPrograma


#prueba
#m=Memoria()
#m.write(0,1)
		
