class Disco:
    def __init__(self):
        self.programas = []
        self.indice = 0

    def agregarPrograma(self, programa):
        self.programas.append(programa)
        self.indice += 1

    def getPrograma(self, indice):
        return self.programas[indice]

    def tamanioOcupado(self):
        return len(self.programas)



