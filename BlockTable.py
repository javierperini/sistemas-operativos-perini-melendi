__author__ = 'javier'


class BlockTable:

    def __init__(self):
        self.diccionario = dict()

    def put(self, pid, block):
        self.diccionario.__setitem__(pid, block)
