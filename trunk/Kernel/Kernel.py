from Memory.AdministradorDeMemoria import *
from Scheduler.PCBTable import *
from Memory.MemoryOrganize import *
from Scheduler.Scheduler import *
from Cpu.Cpu import *


class Kernel:
    def __init__(self, memory, file_system):
        self.file_system = file_system
        self.memory = memory
        self.memory_admin = AdministradorDeMemoria(self.memory, AsignacionContinua(self.memory))
        self.ready_queue = []
        self.pid = 0
        self.scheduler = Scheduler(self.ready_queue, self.cpu)
        self.cpu = Cpu(self.memory_admin)
        self.pcb_table = PCBTable()

    def get_pid(self):
        return self.pid

    def set_scheduler_policy(self):
        self.scheduler.set_as_fifo()

    def create_pcb(self, program, priority):
        initial_pos = self.memory_admin.nextPost()
        final_pos = (initial_pos+program.size())
        pcb = PCB(initial_pos, final_pos, 0, self.get_pid(), priority)
        self.pid += 1
        return pcb

    def get_program(self, program_name, path):
        return self.file_system.find(path, program_name)

    def get_ready_queue(self):
        return self.ready_queue

    def execute(self, program_name, path, priority):
        program = self.get_program(program_name, path)
        if self.memory_admin.hayEspacioPara(program.size):
            pcb = self.create_pcb(program, priority)
            self.pcb_table.add(pcb)
            self.memory_admin.almacenar(pcb, program)
            self.scheduler.add_pcb(pcb)
            self.scheduler.get_pcb()

        else:
            print("No hay lugar en la memoria para ejecutar")






