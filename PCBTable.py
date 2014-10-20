__author__ = 'memonono'


class PCBTable:

    def __init__(self):
        self.pcbs = []

    def remove(self, pcb):
        self.pcbs.remove(pcb)

    def add(self, pcb):
        self.pcbs.add(pcb)
