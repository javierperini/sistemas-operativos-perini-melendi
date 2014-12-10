import ProcessState


class PCB:
    def __init__(self, init, fin, pc, pid, priority):
        self.init_position = init
        self.final_position = fin
        self.pc = pc
        self.state = ProcessState(1)
        self.pid = pid
        self._priority = priority

    def initial_position(self):
        return self.init_position

    def final_position(self):
        return self.final_position

    def get_pc(self):
        return self.pc

    def sum_pc(self):
        self.pc += 1

    def get_state(self):
        return self.state

    def get_pid(self):
        return self.pid

    def set_state(self, stateNew):
        self.state = stateNew

    def get_priority(self):
        return self._priority

    def __cmp__(self, otroPCB):
    #Para compararme a mi con otro pcb, por prioridad
        return cmp(self._priority, otroPCB.get_Priority())