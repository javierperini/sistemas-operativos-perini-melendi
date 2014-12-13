import unittest


class Memory:
    def __init__(self):
        self.records = []
        self.next_position = 0
        self.size = 512
        self.free_cells = 512

    def read(self, position):
        return self.records[position]

    def write(self, position, instruction):
        self.records.insert(position, instruction)
        self.next_position += 1
        self.free_cells -= 1

    def next_position(self):
        return self.next_position

    def free_memory_to_save(self, program_size):
        return self.free_cells >= program_size

    def delete(self, index):
        self.records.pop(index)
        self.free_cells += 1

    def free_cells(self):
        return self.free_cells


class TestsMemory(unittest.TestCase):

    def setUp(self):
        self.memory = Memory()
        self.memory.write(0, "primeraInstruccion")
        self.memory.write(1, "segundaInstruccion")

    def test_next_position(self):
        self.assertEquals(2, self.memory.next_position)

    def test_free_memory_to_save(self):
        self.assertTrue(self.memory.free_memory_to_save(10))

    def test_read_memory(self):
        self.assertEqual("primeraInstruccion", self.memory.read(0))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsMemory)
unittest.TextTestRunner(verbosity=2).run(suite)