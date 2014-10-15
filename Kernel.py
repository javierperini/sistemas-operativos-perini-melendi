from AdministradorDeMemoria import *
from PCB import *
from Schelduler import *
import Queue


class Kernel:
    def __init__(self, memoria, disco):
        self.disco = disco
        self.memoria = memoria
        self.admin_memoria = AdministradorDeMemoria(self.memoria)
        self.colaDeReady = Queue()
        self.pid = 0
        self.schelduler = Schelduler(self.colaDeReady)

    def pid(self):
        return self.pid

    def creaProceso(self, nombre_programa):
        posInicial = self.admin_memoria.siguientePosicion()
        programa = self.disco.getProgram(nombre_programa)
        posFinal = (posInicial+programa.size())
        self.admin_memoria.almacenar(programa)
        self.colaDeReady.append(PCB(posInicial, posFinal, 0, self.pid()))
        self.pid += 1

    def getColaDeReady(self):
        return self.colaDeReady

    def ejecutar(self, nombre_programa):
        self.creaProceso(nombre_programa)
        self.schelduler.planifica()
        ## muere kernel



