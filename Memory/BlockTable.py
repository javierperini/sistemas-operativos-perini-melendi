class BlockTable:

    def __init__(self):
        self.diccionario = {}

    def put(self, pid, block):
        self.diccionario[pid] = block

    def get(self, pid):
       return self.diccionario[pid]