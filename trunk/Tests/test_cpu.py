__author__ = 'memonono'

import unittest
from Scheduler.PCB import PCB
from Cpu.Cpu import *
from Kernel.Kernel import Kernel
from Kernel.Programa import Programa
from Memory.Memory import Memory
from Disc.FileSystem import FileSystem


class TestsCpu(unittest.TestCase):

    def setUp(self):
        self.pcb = PCB(100, 200, 40, 55, 5)
        self.kernel = Kernel(Memory(), FileSystem())
        self.kernel.create_pcb(Programa("a_program_name"), 1)
        self.cpu = Cpu(self.kernel)

    def test_cpu_run_instruction(self):
        result = "Aca va el resultado"
        self.assertEquals(result, (self.cpu.run()))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsCpu)
unittest.TextTestRunner(verbosity=2).run(suite)

