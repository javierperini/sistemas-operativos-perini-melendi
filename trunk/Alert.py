from PCBTable import PCBTable
from ProcessState import ProcessState

__author__ = 'memonono'


class InstructionAlert:

    def __init__(self, cpu, scheduler):
        self.cpu = cpu
        self.scheduler = scheduler

    def __new__(cls, *args, **kwargs):
        raise ReferenceError

    def condition_of_applicability(self, pcb):
        pass

    def alert_cpu(self, pcb):
        new_pcb = self.scheduler.nextPCB()
        self.cpu.pcb = new_pcb
        new_pcb.state = ProcessState.ready
        self.cpu.resetRoundRobin(pcb)


class KillAlert(InstructionAlert):

    def __init__(self, cpu, scheduler):
        super.__init__(cpu, scheduler)

    def condition_of_applicability(self, pcb):
        return pcb.posicion_fin == pcb.posicion_ini

    def alert_cpu(self, pcb):
        super.alert_cpu(pcb)
        pcb.state = ProcessState.end
        self.cpu.memory.free(pcb)
        PCBTable.remove(pcb)


class TimeoutAlert(InstructionAlert):

    def __init__(self, cpu, scheduler):
        super.__init__(cpu, scheduler)

    def condition_of_applicability(self, pcb):
        raise NotImplemented

    def alert_cpu(self, pcb):
        super.alert_cpu(pcb)
        pcb.state = ProcessState.ready


class IOAlert(InstructionAlert):

    def __init__(self, cpu, scheduler):
        super.__init__(cpu, scheduler)

    def condition_of_applicability(self, pcb):
        return pcb.next_instruction().is_io_instruction()

    def alert_cpu(self, pcb):
        super.alert_cpu(pcb)
        pcb.state = ProcessState.waiting
        #Podriamos hacer algo en el medio, como procesar la IOInstruction
        pcb.state = ProcessState.ready


class NewAlert(InstructionAlert):

    def __init__(self, cpu, scheduler):
        super.__init__(cpu, scheduler)

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.new)

    def alert_cpu(self, pcb):
        super.alert_cpu(pcb)
        PCBTable.add(pcb)
        pcb.state = ProcessState.ready