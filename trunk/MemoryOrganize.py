import Block
import BlockTable
__author__ = 'javier matias camila'


class MemoryOrganize:

    def __init__(self, memory):
        self.blockTable = BlockTable()
        self.memory = memory

    def hayEspacioPara(self, tamanio):
        pass

    def saveProgram(self, program):
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
        self.memory.compactar()
        return self.memory.hayEspacioParaGuardar(tamanio)


    def saveProgram(self, program):
        bloque = Block(program.size()).setPrograma(program)
        self.blockTable.put(program.nombre, [bloque])
        for instruction in program.getInstrucciones():
            self.memory.write(self.nextPosition(), instruction)

    def nextPosition(self):
        self.blockTable.nextPosition()

    def deleteMemory(self, indice):
        self.memory.delete(indice)


class Paginacion(MemoryOrganize):

    def __init__(self, memory):
        super.__init__(memory)

    def saveProgram(self, program):
        block = Block(4)
        contador= 0
        for instruction in program.getInstrucciones():
            if(block.getTamanio >= contador):
                self.memory.write(self.nextPosition(), instruction)
                contador += 1
            else:
               self.blockTable.put(block)

        self.blockTable.put(program, block)