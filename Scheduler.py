import Queue


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
            self.cola = []