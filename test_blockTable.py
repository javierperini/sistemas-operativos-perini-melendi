import unittest
from BlockTable import *


class TestBlockTable(unittest.TestCase):

    def setUp(self):
        self.block_table = BlockTable()
        self.block_table.put(14, "Imagina que soy un bloque")
        self.block_table.put(15, "Imagina que soy otro bloque")

    def test_get(self):
        self.assertEqual("Imagina que soy un bloque", self.block_table.get(14))
        self.assertEqual("Imagina que soy otro bloque", self.block_table.get(15))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBlockTable)
unittest.TextTestRunner(verbosity=2).run(suite)