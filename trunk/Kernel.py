from AdministradorDeMemoria import *
from PCB import *
from Scheduler import *
import Queue


class Kernel:
    def __init__(self, memoria, disco):
        self.disco = disco
        self.memoria = memoria
        self.admin_memoria = AdministradorDeMemoria(self.memoria)
        self.colaDeReady = []
        self.pid = 0
        self.schelduler = Scheduler()
'''HACER UN KERNEL STARTUP!!!!!!!!!!!!!1'''
    def pid(self):
        return self.pid

    def creaProceso(self, nombre_programa):
        posInicial = self.admin_memoria.siguientePosicion()
        programa = self.getPrograma(nombre_programa)   ##CAMBIO TODO
        posFinal = (posInicial+programa.size())   ##CAMBIO
        self.admin_memoria.almacenar(programa)
        pcb = PCB(posInicial, posFinal, 0, self.pid())
        self.colaDeReady.append(pcb)
        self.pid += 1
        return pcb

    def getPrograma(self ,nombrePrograma):
        return self.disco.getProgram(nombrePrograma)

    def getColaDeReady(self):
        return self.colaDeReady

    def ejecutar(self, nombre_programa):
        programa = self.getPrograma(nombre_programa)
        if self.admin_memoria.hayEspacioPara(programa.size):
            pcb = self.creaProceso(nombre_programa)
            self.admin_memoria.almacenar(pcb, programa)
            self.schelduler.get_pcb(self.colaDeReady) #el scheduler mismo le manda run al pcb obtenido!
            ## muere kernel
        else:
            self.imprimirError("NO HAY LUGAR")

    def imprimirError(self, mensaje):
        pass
        ##PARA LA SHELL




