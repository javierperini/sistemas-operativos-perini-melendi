from Output import Output


class Programa:

    def __init__(self, name):
        self.name = name
        self.instrucciones = []
        self.output = Output()

    def agregarInstruccion(self, instruccion):
        self.instrucciones.append(instruccion)

    def ejecutar(self):
        for instr in self.instrucciones:
            instr.run(self.output)

    def getInstrucciones(self):
        return self.instrucciones

    def getElemento(self, posicion):
        return self.instrucciones[posicion]

    def getInstruccionEjecutada(self, indice):
        return self.output.get(indice)



