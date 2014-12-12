class Scheduler:
    def __init__(self, cola_de_ready, cpu):
        self._policy = None
        self._cpu = cpu
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
        pass


class RoundRobinScheduler():
    def __init__(self, quantum, ready_queue):
        self.readyQueue = ready_queue
        self.quantum = quantum

    def get_pcb(self):
        return self.readyQueue.pop(0)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def get_quantum(self):
        return self.quantum
