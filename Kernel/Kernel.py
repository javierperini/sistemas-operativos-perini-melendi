from Memory.MemoryAdmin import MemoryAdmin
from Scheduler.PCBTable import PCBTable
from Memory.MemoryOrganize import *
from Scheduler.Scheduler import Scheduler
from Cpu.Cpu import Cpu
from Scheduler.PCB import PCB
from Cpu.Alert import TimeoutAlert


class Kernel:

    def __init__(self, memory, file_system, clock):
        self.file_system = file_system
        self.memory_admin = MemoryAdmin(AsignacionContinua(memory))
        self.pid = 0
        self.scheduler = Scheduler()
        self.cpu = Cpu(self)
        self.pcb_table = PCBTable()
        self.clock = clock

    def memory_admin(self):
        return self.memory_admin

    def scheduler(self):
        return self.scheduler

    def get_pid(self):
        return self.pid

    def set_scheduler_policy(self):
        self.scheduler.set_as_fifo()

    def create_pcb(self, program, priority):
        initial_pos = self.memory_admin.next_post_free()
        final_pos = (initial_pos+program.size())
        pcb = PCB(initial_pos, final_pos, 0, self.get_pid(), priority)
        self.pid += 1
        self.scheduler.add_pcb(pcb)
        self.memory_admin.save(pcb, program)
        return pcb              #Esto no me gusta, pero es lo que hay por el momento

    def get_program(self, program_name, path):
        return self.file_system.find(path, program_name)

    def get_ready_queue(self):
        return self.scheduler.ready_queue

    def handle_signal(self, signal, pcb):
        #La senial deberia hacer que la ejecucion de un proceso cambie
        try:
            signal.alert_cpu(pcb, self.cpu, self.pcb_table)
        except Exception as e:
            print("Handle unexpected signal! details: " + e.message)
            TimeoutAlert().alert_cpu(pcb, self.cpu, self.pcb_table)

    def timing(self):
        self.clock.tick()

    def execute(self, program_name, path, priority):
        program = self.get_program(program_name, path)
        if self.memory_admin.has_room_for(program.size):
            pcb = self.create_pcb(program, priority)
            self.pcb_table.add(pcb)
            self.memory_admin.save(pcb, program)
            self.scheduler.add_pcb(pcb)
            self.scheduler.get_pcb()
        else:
            raise Exception("No hay lugar en la memoria para ejecutar")




