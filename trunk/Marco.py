__author__ = 'javier'


class Marco:

    def __init__(self, tamanioDeMarco, firstPosition, lastPosition):
        self.tamanioDeMarco = tamanioDeMarco
        self.firstPosition = firstPosition
        self.lastPosition = lastPosition
        self.estoyLibre = True

    def tengoContenido(self,):
        self.estoyLibre = False

    def getEstoyLibre(self):
        return self.estoyLibre

    def getFirstPosition(self):
        return self.firstPosition

    def getLastPosition(self):
        return self.lastPosition
