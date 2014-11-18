from PCBTable import PCBTable
from ProcessState import ProcessState

__author__ = 'memonono'


class InstructionAlert:

        def __init__(self, cpu, scheduler):
            raise ReferenceError

        def condition_of_applicability(self, pcb):
            pass

        def alert_for(self , pcb):
            new_pcb = self.scheduler.nextPCB()
            self.cpu.pcb = new_pcb
            new_pcb.state = ProcessState.ready
            self.cpu.resetRoundRobin(pcb)


class KillAlert(InstructionAlert):

        def __init__(self, cpu):
            self.cpu = cpu

        def condition_of_applicability(self, pcb):
            return pcb.posicion_fin == pcb.posicion_ini

        def alert_for(self, pcb):
            super
            pcb.state = ProcessState.end
            self.cpu.memory.free(pcb)
            PCBTable.remove(pcb)


class TimeoutAlert(InstructionAlert):

        def condition_of_applicability(self, pcb):
            raise NotImplemented

        def alert_for(self, pcb):
            super
            pcb.state = ProcessState.ready


class IOAlert(InstructionAlert):

    def condition_of_applicability(self, pcb):
        return pcb.next_instruction().is_io_instruction()

    def alert_for(self, pcb):
        pcb.state = ProcessState.waiting
        #Podriamos hacer algo en el medio, como procesar la IOInstruction
        pcb.state = ProcessState.ready


class NewAlert(InstructionAlert):

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.new)

    def alert_for(self, pcb):
        PCBTable.add(pcb)
        pcb.state = ProcessState.ready