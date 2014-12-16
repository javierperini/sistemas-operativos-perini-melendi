import unittest

from Memory.Block import *


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(111, 2, 13, 16)

    def test_next_pos(self):
        self.assertEqual(14, self.block.next_pos())
        self.assertNotEqual(14, self.block.next_pos())

suite = unittest.TestLoader().loadTestsFromTestCase(TestBlock)
unittest.TextTestRunner(verbosity=2).run(suite)