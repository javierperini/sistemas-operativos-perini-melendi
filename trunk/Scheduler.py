import Queue
from PCB import *
import unittest


class Scheduler:
    def __init__(self):
        self._policy = None

    def set_as_fifo(self):
        self._policy = FifoScheduler()

    def set_as_priority(self):
        self._policy = PriorityScheduler()

    def set_as_round_robin(self):
        self._policy = RoundRobinScheduler()

    def get_pcb(self):
        return self._policy.get_pcb()

    def add_pcb(self, pcb):
        self._policy.add_pcb(pcb)


class FifoScheduler:
    def __init__(self):
        self._readyQueue = Queue()

    def get_pcb(self):
        return self._readyQueue.get()

    def add_pcb(self, pcb):
        self._readyQueue.put(pcb)


class PriorityScheduler():
    def __init__(self):
        self._readyQueue = Queue.PriorityQueue()

    def get_pcb(self):
        return self._readyQueue.get()

    def add_pcb(self, pcb):
        self._readyQueue.put(pcb)


class RoundRobinScheduler():
        def __init__(self, quantum):
            self.readyQueue = Queue()


#--------------------------------------------------------#
class TestsAdmin(unittest.TestCase):
    def setUp(self):
        self.pcb1 = PCB(100, 200, 40, 55, 5)
        self.pcb2 = PCB(100, 200, 40, 55, 10)
        self.pcb3 = PCB(100, 200, 40, 55, 2)
        self.pcb4 = PCB(100, 200, 40, 55, 1)
        self.pcb5 = PCB(100, 200, 40, 55, 9)
        self._scheduler = Scheduler()

    def test_fifo_scheduler(self):
        self.fifo_policy = FifoScheduler()
        self._scheduler.set_as_fifo()
        self.fifo_policy.add_pcb(self.pcb1)
        self.fifo_policy.add_pcb(self.pcb2)
        self.fifo_policy.add_pcb(self.pcb3)

        self.assertEquals(self._scheduler.get_pcb(), self.pcb1)

    def test_priority_scheduler(self):
        self.priority_policy = PriorityScheduler()
        self._scheduler.set_as_priority()
        self.priority_policy.add_pcb(self.pcb1)
        self.priority_policy.add_pcb(self.pcb2)
        self.priority_policy.add_pcb(self.pcb3)
        self.priority_policy.add_pcb(self.pcb4)
        self.priority_policy.add_pcb(self.pcb5)

        self.assertEquals(self._scheduler.get_pcb(), 4)




suite = unittest.TestLoader().loadTestsFromTestCase(TestsAdmin)
unittest.TextTestRunner(verbosity=2).run(suite)