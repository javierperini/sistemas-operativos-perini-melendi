__author__ = 'javier'


class Page:

    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.instruction = []
        self.marcoAsociado = object

    def asociarMarco(self, marco):
        marco.tengoContenido()
        self.marcoAsociado = marco

    def getMarcoAsociado(self):
        return self.marcoAsociado

