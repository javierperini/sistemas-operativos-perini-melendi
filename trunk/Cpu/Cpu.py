from AlertHandler import Alerter
import thread
__author__ = 'memonono'


class Cpu():

    def __init__(self, kernel):
        self.kernel = kernel
        self.alerter = Alerter(self, self.kernel.scheduler)
        self.memory_admin = kernel.memory_admin

    def read_burst_instruction(self, pcb, quantum):
        while quantum > 0:
                self.memory_admin.readMemory(pcb.posicion_ini)
                quantum(quantum - 1)
        self.alerter.alert_for(pcb)

    def run(self):
        pcb = self.kernel.scheduler.get_pcb()
        thread.start_new_thread(self.read_burst_instruction, [pcb, self.memory_admin.quantum()])


from Scheduler import PCB
from Disc import FileSystem
from Kernel import Kernel
import unittest
import Memory


class TestsCpu(unittest.TestCase):

    def setUp(self):
        self.pcb = PCB(100, 200, 40, 55, 5)
        self.kernel = Kernel(Memory, FileSystem)
        self.cpu = Cpu(self.kernel)

    def test_cpu_run_instruction(self):
        result = "Acá va el resultado"
        self.assertEquals(result, (self.cpu.run(self.pcb)))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsCpu)
unittest.TextTestRunner(verbosity=2).run(suite)