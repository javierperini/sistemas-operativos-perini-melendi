__author__ = 'javier'


class Page:

    def __init__(self, marco):
        self.tamanio = marco.tamanioDeMarco
        self.instruction = marco.instructions
        self.marcoAsociado = marco
        self.asociarMarco(marco)

    def asociarMarco(self, marco):
        marco.tengoContenido()

    def getMarcoAsociado(self):
        return self.marcoAsociado

