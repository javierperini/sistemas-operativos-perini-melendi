from Estado import *


class PCB:
    def __init__(self, ini, fin, pc, pid, priority):
        self.posicion_ini = ini
        self.posicion_fin = fin
        self.pc = pc
        self.state = New
        self.pid = pid
        self._priority = priority

    def posicionInicial(self):
        return self.posicion_ini

    def posicionFinal(self):
        return self.posicion_fin

    def getPc(self):
        return self.pc

    def getState(self):
        return self.state

    def getPid(self):
        return self.pid

    def setState(self, stateNew):
        self.state= stateNew

    def get_priority(self):
        return self._priority

    def __cmp__(self, otroPCB):
    #Para compararme a mi con otro pcb, por prioridad
        return cmp(self._priority, otroPCB.get_Priority())