import OutPut


class Programa:

    def __init__(self):
        self.instrucciones = []
        self.output = Output()
        self.indice = 0

    def agregarInstruccion(self, instruccion):
        self.instrucciones.append(instruccion)
        self.indice += 1

    def ejecutar(self):
        for instr in self.instrucciones:
            instr.run(self.output)

    def getInstrucciones(self):
        return self.instrucciones

    def getElemento(self, posicion):
        return self.instrucciones[posicion]

    def getInstruccionEjecutada(self, indice):
        return self.output.get(indice)



