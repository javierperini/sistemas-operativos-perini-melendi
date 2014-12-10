import unittest
import Cpu
from PCB import *


class Scheduler:
    def __init__(self, cola_de_ready):
        self._policy = None
        self._cpu = Cpu()
        self._ready_queue = cola_de_ready

    def set_as_fifo(self):
        self._policy = FifoScheduler(self._ready_queue)

    def set_as_priority(self):
        self._policy = PriorityScheduler(self._ready_queue)

    def set_as_round_robin(self):
        self._policy = RoundRobinScheduler(self._ready_queue)

    def get_pcb(self):
        self._cpu.run(self._policy.get_pcb())

    def add_pcb(self, pcb):
        self._policy.add_pcb(pcb)


class FifoScheduler:
    def __init__(self, ready_queue):
        self._readyQueue = ready_queue

    def get_pcb(self):
        return self._readyQueue.pop(0)

    def add_pcb(self, pcb):
        self._readyQueue.append(pcb)


class PriorityScheduler():
    def __init__(self, ready_queue):
        self._readyQueue = ready_queue

    def get_pcb(self):
        return self._readyQueue.pop()

    def add_pcb(self, pcb):
        # el que tiene menor numero de priority es el de mas prioridad ????
        index = 0
        not_end = True
        if not_end & (pcb.get_priority() < self._readyQueue.pop(index)):
            self._readyQueue.insert(pcb)
            not_end = False
        else:
            index = index + 1


class RoundRobinScheduler():
    def __init__(self, quantum, ready_queue):
        self.readyQueue = ready_queue
        self.quantum = quantum

    def get_pcb(self):
        return self._readyQueue.pop(0)

    def add_pcb(self, pcb):
        self._readyQueue.append(pcb)

    def get_quantum(self):
        return self.quantum


# --------------------------------------------------------#
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