from AdministradorDeMemoria import *
from PCB import *
from Process import *
from Scheduler import *
from PCBTable import *

import Queue


class Kernel:
    def __init__(self, memoria, disco):
        self.disco = disco
        self.memoria = memoria
        self.admin_memoria = AdministradorDeMemoria(self.memoria)
        self.colaDeReady = []
        self.pid = 0
        self.schelduler = Scheduler()
        self.pcb_table = PCBTable()
        #HACER UN KERNEL STARTUP!!!!!!!!!!!!!

    def pid(self):
        return self.pid

    def crear_pcb(self, nombre_programa):
        posInicial = self.admin_memoria.siguientePosicion()
        programa = self.getPrograma(nombre_programa)   ##CAMBIO TODO
        posFinal = (posInicial+programa.size())   ##CAMBIO
        pcb = PCB(posInicial, posFinal, 0, self.pid())
        self.pid += 1
        return pcb

    def getPrograma(self, nombrePrograma):
        return self.disco.getProgram(nombrePrograma)

    def getColaDeReady(self):
        return self.colaDeReady

    def ejecutar(self, nombre_programa):
        programa = self.getPrograma(nombre_programa)
        if self.admin_memoria.hayEspacioPara(programa.size):
            pcb = self.crear_pcb(nombre_programa)
            proceso = self.crear_proceso(programa, pcb)
            self.pcb_table.add(pcb)
            self.admin_memoria.almacenar(programa)
            self.colaDeReady.add(proceso)
            self.schelduler.get_pcb(self.colaDeReady)

        else:
            self.imprimirError("NO HAY LUGAR ss")

    def crear_proceso(self, programa, pcb):
        return Process(programa, pcb)

    def imprimirError(self, mensaje):
        pass
        ##PARA LA SHELL




