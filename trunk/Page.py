__author__ = 'javier'


class Page:

    def __init__(self, marco):
        self.tamanio = marco.tamanioDeMarco
        self.instruction = []
        self.marcoAsociado = marco
        self.asociarMarco(marco)

    def asociarMarco(self, marco):
        marco.tengoContenido()

    def getMarcoAsociado(self):
        return self.marcoAsociado

    def getTamanio(self):
        return self.tamanio

    def addNroInstruction(self, instrution):
        self.instruction = instrution

