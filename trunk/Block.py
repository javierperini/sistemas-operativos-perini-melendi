__author__ = 'javier'


class Block:

    def __init__(self, tamanio, nombrePrograma, posicionInicial, posicionFinal):
        self.tamanio = tamanio
        self.nombrePrograma = nombrePrograma
        self.posicionInicial = posicionInicial
        self.posicionFinal = posicionFinal

    def getTamanio(self):
        return self.tamanio

    def getPrograma(self):
        return self.nombrePrograma

    def getPosicionInicial(self):
        return self.posicionInicial

    def getPosicionFinal(self):
        return self.posicionFinal