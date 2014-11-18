import ProcessState


class PCB:
    def __init__(self, init, fin, pc, pid, priority):
        self.init_position = init
        self.final_position = fin
        self.pc = pc
        self.state = ProcessState(1)
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
        self.state = stateNew

    def get_priority(self):
        return self._priority

    def __cmp__(self, otroPCB):
    #Para compararme a mi con otro pcb, por prioridad
        return cmp(self._priority, otroPCB.get_Priority())