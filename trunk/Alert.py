from PCBTable import PCBTable
from Estado import Estado

__author__ = 'memonono'


##En el alert_for(pcb) vamos a definir cada recetita que tenemos

class InstructionAlert:

        def __init__(self, cpu, scheduler):
            raise ReferenceError

        def condition_of_applicability(self, pcb):
            pass

        def alert_for(self , pcb):
            new_pcb = self.scheduler.nextPCB()
            self.cpu.pcb = new_pcb
            new_pcb.state = Estado.ready
            self.cpu.resetRoundRobin(pcb)


class KillAlert(InstructionAlert):

        def __init__(self, cpu):
            self.cpu = cpu

        def condition_of_applicability(self, pcb):
            return pcb.posicion_fin == pcb.posicion_ini

        def alert_for(self, pcb):
            super
            pcb.state = Estado.end
            self.cpu.memory.free(pcb)
            PCBTable.remove(pcb)


class TimeoutAlert(InstructionAlert):

        def condition_of_applicability(self, pcb):
            raise NotImplemented

        def alert_for(self, pcb):
            super
            pcb.state = Estado.ready


class IOAlert(InstructionAlert):

    def condition_of_applicability(self, pcb):
        return pcb.next_instruction().is_io_instruction()

    def alert_for(self, pcb):
        return NotImplemented


class NewAlert(InstructionAlert):

    def condition_of_applicability(self, pcb):
        raise NotImplemented

    def alert_for(self, pcb):
        return NotImplemented