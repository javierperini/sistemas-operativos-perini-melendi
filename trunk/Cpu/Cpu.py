from AlertHandler import Alerter
import thread
__author__ = 'memonono'


class Cpu:

    def __init__(self, kernel):
        self.kernel = kernel
        self.alerter = Alerter(self)
        self.memory_admin = kernel.memory_admin()

    def scheduler(self):
        return self.kernel.scheduler()

    def read_burst_instruction(self, pcb, quantum):
        while quantum > 0:
                self.memory_admin.readMemory(pcb)
                quantum(quantum - 1)
        self.alerter.alert_for(pcb)

    def run(self):
        pcb = self.kernel.scheduler.get_pcb()
        thread.start_new_thread(self.read_burst_instruction, [pcb, self.memory_admin.quantum()])
