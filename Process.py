__author__ = 'memonono'


class Process:
    def __init__(self, program, pcb):
        self.pc = 0
        self.stack = []
        self.heap = []
        self.texto = []
        self.datos = []
        self.program = program
        self.pcb = pcb
