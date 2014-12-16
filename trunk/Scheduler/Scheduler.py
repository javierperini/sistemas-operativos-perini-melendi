class Scheduler:

    def __init__(self):
        self.policy = None
        self.ready_queue = []

    def __call__(self, *args, **kwargs):
        return self

    def set_as_fifo(self):
        self.policy = FifoScheduler(self.ready_queue)

    def set_as_priority(self):
        self.policy = PriorityScheduler(self.ready_queue)

    def set_as_round_robin(self, quantum):
        self.policy = RoundRobinScheduler(quantum, self.ready_queue)

    def get_pcb(self):
        return self.policy.get_pcb()

    def add_pcb(self, pcb):
        self.policy.add_pcb(pcb)

    def quantum(self):
        return self.policy.get_quantum


class FifoScheduler:
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    def get_pcb(self):
        if not len(self.readyQueue) == 0:
            return self.readyQueue.pop(0)
        else:
            raise Exception("No processes available!")

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def get_quantum(self):
        return 1


class PriorityScheduler():
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    def get_pcb(self):
        return self.readyQueue.pop()

    def add_pcb(self, pcb):
        aux = self.readyQueue
        self.readyQueue = []
        for i in range(len(aux)-1):
            if i > pcb.priority() & pcb.priority() < i+1:
                self.readyQueue.append(aux[i])
                self.readyQueue.append(pcb)
            else:
                self.readyQueue.append(aux[i])

    def get_quantum(self):
        return 1


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
