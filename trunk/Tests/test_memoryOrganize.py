import unittest
from Memory.MemoryOrganize import Paginacion
from Memory.MemoryOrganize import AsignacionContinua
from Memory.Memory import Memory
from Scheduler.PCB import PCB
from Kernel.Programa import Programa
from Disc.Instruccion import Instruccion


class TestMemoryOrganize(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()
        self.asignacion_continua = AsignacionContinua(self.memory)
        self.paginacion = Paginacion(self.memory)
        self.pcb = PCB(2, 4, 6, 40, 4)

        self.progr = Programa("un_programa")
        self.instr = Instruccion('Instruccion 1')
        self.progr.agregarInstruccion(self.instr)

    def test_has_run_for_asignacion_continua(self):
        self.assertTrue(self.asignacion_continua.has_room_for(10))

    def test_save_asignacion_continua(self):
        self.asignacion_continua.save(self.pcb, self.progr)
        self.assertEqual(511, self.memory.free_cells)

    def test_next_position_asignacion_continua(self):
        self.asignacion_continua.save(self.pcb, self.progr)
        result = self.asignacion_continua.next_position(self.pcb)
        self.assertEqual(1, result)

    def test_next_post_free_asignacion_continua(self):
        self.assertEqual(0, self.asignacion_continua.next_post_free())

    def test_compact(self):
        self.asignacion_continua.save(self.pcb, self.progr)
        self.asignacion_continua.next_position(self.pcb)
        self.asignacion_continua.has_room_for(1)
        self.assertEqual(512, self.memory.free_cells)

    def test_has_run_for_paginacion(self):
        self.assertTrue(self.paginacion.has_room_for(12))

    def test_next_position_paginacion(self):
        self.assertEqual(0, self.paginacion.next_position(self.pcb))

    def test_next_post_free_paginacion(self):
        self.assertEqual(0, self.paginacion.next_post_free())

    def test_save_paginacion(self):
        self.paginacion.save(self.pcb, self.progr)
        self.assertEqual(511, self.memory.free_cells)


suite = unittest.TestLoader().loadTestsFromTestCase(TestMemoryOrganize)
unittest.TextTestRunner(verbosity=2).run(suite)