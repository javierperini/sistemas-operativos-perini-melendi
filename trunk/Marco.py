__author__ = 'javier'


class Marco:

    def __init__(self, id_marco, tamanioDeMarco, firstPosition, lastPosition):
        self.id_marco = id_marco
        self.tamanioDeMarco = tamanioDeMarco
        self.firstPosition = firstPosition
        self.lastPosition = lastPosition
        self.estoyLibre = True
        ##self.dirs_memory = [firstPosition .. lastPosition] ##crear rango

    def tengoContenido(self):
        self.estoyLibre = False

    def getEstoyLibre(self):
        return self.estoyLibre

    def getFirstPosition(self):
        return self.firstPosition

    def getLastPosition(self):
        return self.lastPosition

    def next_post(self, nro_instr):
    ##     self.dirs_memory[nro_instr]
        pass