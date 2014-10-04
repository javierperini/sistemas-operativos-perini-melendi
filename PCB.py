from Estado import *


class PCB:
    def __init__(self, ini, fin, pc, pid):
        self.posicion_ini = ini
        self.posicion_fin = fin
        self.pc = pc
        self.state = New
        self.pid = pid

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