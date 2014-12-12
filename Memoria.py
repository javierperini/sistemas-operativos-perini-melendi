class Memoria:
    def __init__(self):
        self.registros = []
        self.siguientePosicion = 0
        self.tamanio = 512
        self.celdasLibres = 512

    def read(self, posicion):
        return self.registros[posicion]

    def write(self, posicion, instruccion):
        self.registros.insert(posicion, instruccion)
        self.siguientePosicion += 1
        self.celdasLibres -= 1

    def siquientePosicion(self):
        return self.siguientePosicion

    def hayEspacioParaGuardar(self, tamanhoDelPrograma):
        return self.celdasLibres >= tamanhoDelPrograma

    def delete(self, indice):
        self.registros.pop(indice)
        self.celdasLibres += 1

    def getCeldasLibres(self):
        return self.celdasLibres
