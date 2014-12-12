from AdministradorDeMemoria import *
from PCB import *
from Process import *
from Scheduler import *
from PCBTable import *
from MemoryOrganize import *
from Cpu import *
import Queue


class Kernel:
    def __init__(self, memoria, file_system):
        self.file_system = file_system
        self.memoria = memoria
        self.admin_memoria = AdministradorDeMemoria(self.memoria, AsignacionContinua(self.memoria))
        self.colaDeReady = []
        self.pid = 0
        self.cpu = Cpu(self.admin_memoria)
        self.schelduler = Scheduler(self.colaDeReady, self.cpu)
        self.pcb_table = PCBTable()


    def get_pid(self):
        return self.pid

    def set_scheduler_policy(self):
        self.schelduler.set_as_fifo()

    def crear_pcb(self, nombre_programa, path, priorty):
        pos_inicial = self.admin_memoria.nextPost()
        programa = self.getPrograma(nombre_programa, path)
        pos_final = (pos_inicial+programa.size())
        pcb = PCB(pos_inicial, pos_final, 0, self.get_pid(), priorty)
        self.pid += 1
        return pcb

    def getPrograma(self, nombrePrograma, path):
        return self.file_system.find(path, nombrePrograma)

    def getColaDeReady(self):
        return self.colaDeReady

    def ejecutar(self, nombre_programa, path, priority):
        programa = self.getPrograma(nombre_programa, path)
        if self.admin_memoria.hayEspacioPara(programa.size):
            pcb = self.crear_pcb(nombre_programa, path, priority)
            self.pcb_table.add(pcb)
            self.admin_memoria.almacenar(pcb, programa)
            self.scheduler.add_pcb(pcb)
            self.schelduler.get_pcb()

        else:
            self.imprimir_error("No hay lugar en la memoria para ejecutar")

    def imprimir_error(self, mensaje):
        print mensaje




