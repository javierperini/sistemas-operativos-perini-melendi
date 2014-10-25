__author__ = 'javier'


class MemoryOrganize:

    def __init__(self, memory):
        self.blockTable = BlockTable()
        self.memory = memory

    def hayEspacioPara(self, tamanio):
        pass

    def savePrograma(self, programa):
        pass

    def nextPosition(self):
        pass

    def getNextInstruction(self, programa):
        self.memory.read(self.nextPosition())

    def deleteMemory(self, instruction):
        self.memory.delete(instruction)


class AsignacionContinua(MemoryOrganize):

    def __init__(self, memory):
        super.__init__(memory)

    def hayEspacioPara(self, tamanio):
        self.memory.hayEspacioParaGuardar(tamanio)

    def savePrograma(self, programa):
        bloque = Block(programa.size()).setPrograma(programa)
        self.blockTable.put(programa.nombre, [bloque])
        for instruction in programa.getInstrucciones():
            self.memory.write(self.nextPosition(), instruction)

    def nextPosition(self):
        self.blockTable.nextPosition()

    def deleteMemory(self, indice):
        self.memory.delete(indice)
        self.compactacion(indice)
 #FALTA HACER COMPACTACION


class Paginacion(MemoryOrganize):

    def __init__(self, memory):
        super.__init__(memory)

    def savePrograma(self, programa):
        bloque = Block(4)
        contador= 0
        for instruction in programa.getInstrucciones():
            if(block.getTamanio >= contador):
                self.memory.write(self.nextPosition(), instruction)
                contador += 1
            else:
               self.blockTable.put(bloque)

        self.blockTable.put(programa, bloque)