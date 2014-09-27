from Programa import *
from AdministradorDeMemoria import *
from PCB import *
import numpy as np


class Kernel:
    def __init__(self, memoria, disco):
        self.disco = disco
        self.memoria = memoria
        self.admin_memoria = AdministradorDeMemoria(self.memoria)
        self.colaDeReady = np.arrange(10000000)
        self.pid = 0

    def pid(self):
        return self.pid

    def ejecutar(self, nombre_programa):
        posInicial = self.admin_memoria.siguientePosicion()
        programa = self.disco.getProgram(nombre_programa)
        posFinal = (posInicial+programa.size())
        self.admin_memoria.almacenar(programa)
        self.colaDeReady.append(PCB(posInicial, posFinal, 0, self.pid()))
        self.pid += 1


