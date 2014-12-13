from Scheduler.ProcessState import *


class InstructionAlert(object):

    def __init__(self, cpu):
        self.cpu = cpu
        self.scheduler = self.cpu.scheduler
        self.pcb_table = self.scheduler.pcb_table

    def __new__(cls, *args, **kwargs):
        raise ReferenceError

    def condition_of_applicability(self, pcb):
        pass

    def alert_cpu(self, pcb):
        new_pcb = self.scheduler.nextPCB
        self.cpu.pcb = new_pcb
        new_pcb.state = ProcessState.ready


class KillAlert(InstructionAlert):
    def __init__(self, cpu):
        super(KillAlert).__init__(cpu)

    def condition_of_applicability(self, pcb):
        return pcb.posicion_fin == pcb.posicion_ini

    def alert_cpu(self, pcb):
        super(KillAlert).alert_cpu(pcb)
        pcb.state = ProcessState.end
        self.cpu.memory_admin.free(pcb) ## NO EXISTE CREALO
        self.pcb_table.remove(pcb)


class TimeoutAlert(InstructionAlert):
    def __init__(self, cpu):
        super(TimeoutAlert).__init__(cpu)

    def condition_of_applicability(self, pcb):
        raise NotImplemented

    def alert_cpu(self, pcb):
        super(TimeoutAlert).alert_cpu(pcb)
        pcb.state = ProcessState.ready


class IOAlert(InstructionAlert):
    def __init__(self, cpu):
        super(IOAlert).__init__(cpu)

    def condition_of_applicability(self, pcb):
        return pcb.next_instruction().is_io_instruction()

    def alert_cpu(self, pcb):
        super(IOAlert).alert_cpu(pcb)
        pcb.state = ProcessState.waiting
        #Podriamos hacer algo en el medio, como procesar la IOInstruction
        pcb.state = ProcessState.ready


class NewAlert(InstructionAlert):
    def __init__(self, cpu):
        super(NewAlert).__init__(cpu)

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.new)

    def alert_cpu(self, pcb):
        super(NewAlert).alert_cpu(pcb)
        self.pcb_table.add(pcb)
        pcb.state = ProcessState.ready