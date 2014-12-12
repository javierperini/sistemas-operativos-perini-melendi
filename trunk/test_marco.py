import unittest
from Marco import *


class TestMarco(unittest.TestCase):

    def setUp(self):
        self.marco = Marco(1, 12, 1234, 1243)


    def test_next_post(self):
        self.assertEqual(1234, self.marco.next_post())

suite = unittest.TestLoader().loadTestsFromTestCase(TestMarco)
unittest.TextTestRunner(verbosity=2).run(suite)