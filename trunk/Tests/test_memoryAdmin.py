import unittest
from Memory.MemoryAdmin import MemoryAdmin
from Memory.Memory import Memory
from Memory.MemoryOrganize import AsignacionContinua
from Kernel.Programa import Programa
from Disc.Instruccion import Instruccion
from Scheduler.PCB import PCB


class TestMemoryAdmin(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()
        self.strategy = AsignacionContinua(self.memory)
        self.admin = MemoryAdmin(self.strategy)
        self.pcb = PCB(3, 5, 20, 40, 4)
        self.progr = Programa("un_programa")
        self.instr = Instruccion('Instruccion 1')
        self.progr.agregarInstruccion(self.instr)

    def test_save(self):
        self.admin.save(self.pcb, self.progr)
        self.assertEqual(511, self.memory.free_cells)

    def test_has_room_for(self):
        self.assertTrue(self.admin.has_room_for(12))

    def test_next_post_free(self):
        self.assertEqual(0, self.admin.next_post_free())

    def test_next_post(self):
        self.admin.save(self.pcb, self.progr)
        self.assertEqual(1, self.admin.next_post(self.pcb))

    def test_read_memory(self):
        self.admin.save(self.pcb, self.progr)
        self.assertEqual(self.instr, self.admin.read_memory(self.pcb))

    def test_delete_memory(self):
        self.admin.save(self.pcb, self.progr)
        self.admin.delete_memory(self.progr)
        self.assertEqual(512, self.memory.free_cells)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMemoryAdmin)
unittest.TextTestRunner(verbosity=2).run(suite)