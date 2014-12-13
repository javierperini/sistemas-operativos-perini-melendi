from AlertHandler import Alerter
import thread
__author__ = 'memonono'


class Cpu():

    def __init__(self, kernel):
        self.kernel = kernel
        self.alerter = Alerter(self)
        self.memory_admin = kernel.memory_admin

    def read_burst_instruction(self, pcb, quantum):
        while quantum > 0:
                self.memory_admin.readMemory(pcb)
                quantum(quantum - 1)
        self.alerter.alert_for(pcb)

    def run(self):
        pcb = self.kernel.scheduler.get_pcb()
        thread.start_new_thread(self.read_burst_instruction, [pcb, self.memory_admin.quantum()])


from Scheduler.PCB import PCB
from Disc import FileSystem
from Kernel.Kernel import Kernel
from Kernel.Programa import Programa
import unittest
import Memory


class TestsCpu(unittest.TestCase):

    def setUp(self):
        self.pcb = PCB(100, 200, 40, 55, 5)
        self.kernel = Kernel(Memory, FileSystem)
        self.kernel.create_pcb(Programa("a_program_name"), 1)
        self.cpu = Cpu(self.kernel)

    def test_cpu_run_instruction(self):
        result = "Aca va el resultado"
        self.assertEquals(result, (self.cpu.run()))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsCpu)
unittest.TextTestRunner(verbosity=2).run(suite)