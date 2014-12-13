from Scheduler.ProcessState import *
from Scheduler.PCBTable import PCBTable


class InstructionAlert(object):

    def __init__(self, cpu):
        self.cpu = cpu
        self.scheduler = self.cpu.scheduler()
        self.pcb_table = PCBTable()

    def condition_of_applicability(self, pcb):
        pass

    def alert_cpu(self, pcb):
        new_pcb = self.scheduler.nextPCB
        self.cpu.pcb = new_pcb
        new_pcb.state = ProcessState.ready


class KillAlert(InstructionAlert):
    def __init__(self, cpu):
        super(KillAlert, self).__init__(cpu)

    def condition_of_applicability(self, pcb):
        return pcb.posicion_fin == pcb.posicion_ini

    def alert_cpu(self, pcb):
        super(KillAlert, self).alert_cpu(pcb)
        pcb.state = ProcessState.end
        self.cpu.memory_admin.free(pcb) ## NO EXISTE CREALO
        self.pcb_table.remove(pcb)


class TimeoutAlert(InstructionAlert):
    def __init__(self, cpu):
        super(TimeoutAlert, self).__init__(cpu)

    def condition_of_applicability(self, pcb):
        raise NotImplemented

    def alert_cpu(self, pcb):
        super(TimeoutAlert, self).alert_cpu(pcb)
        pcb.state = ProcessState.ready


class IOAlert(InstructionAlert):
    def __init__(self, cpu):
        super(IOAlert, self).__init__(cpu)

    def condition_of_applicability(self, pcb):
        return pcb.next_instruction().is_io_instruction()

    def alert_cpu(self, pcb):
        super(IOAlert, self).alert_cpu(pcb)
        pcb.state = ProcessState.waiting
        #Podriamos hacer algo en el medio, como procesar la IOInstruction
        pcb.state = ProcessState.ready


class NewAlert(InstructionAlert):
    def __init__(self, cpu):
        super(NewAlert, self).__init__(cpu)

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.new)

    def alert_cpu(self, pcb):
        super(NewAlert, self).alert_cpu(pcb)
        self.pcb_table.add(pcb)
        pcb.state = ProcessState.ready