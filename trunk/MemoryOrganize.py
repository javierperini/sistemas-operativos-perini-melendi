from Block import *
from Marco import *
from BlockTable import *
from Page import *

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
        return self.memory.read(self.nextPosition())

    def deleteMemory(self, instruction):
        self.memory.delete(instruction)


class AsignacionContinua(MemoryOrganize):

    def __init__(self, memory):
        super.__init__(memory)
        self.bloques = []

    def hayEspacioPara(self, tamanio):
        self.memory.compactar()
        return self.memory.hayEspacioParaGuardar(tamanio)

    def saveProgram(self, program):
        bloque = Block(program.size(), program.nombre, self.nextPositionLibre(), self.nextPositionLibre()+program.size())
        self.guardarBloque(bloque)
        for instruction in program.getInstrucciones():
            self.memory.write(self.nextPositionLibre(), instruction)

    def nextPosition(self):
        return self.memory.nextPost() ##PREGUNTAR

    def deleteMemory(self, indice):
        self.memory.delete(indice)

    def compactar(self):
        self.memory.compactar ##MEMORIA COMPACTAR

    def guardarBloque(self, bloque):
        self.bloques.append(bloque)


class Paginacion(MemoryOrganize):

    def __init__(self, memory):
        super.__init__(memory)
        self.numeroDeMarcos = memory.getTamanio/5
        self.tamanioDeMarco = 5
        self.crearMarcos()
        self.marcos = []

    def crearMarcos(self):
        contador = 0
        tamanioAnt = 0
        while self.numeroDeMarcos > contador:
            marco = Marco(self.tamanioDeMarco, tamanioAnt, tamanioAnt + self.tamanioDeMarco)
            self.marcos.append(marco)
            tamanioAnt = tamanioAnt + self.tamanioDeMarco +1
            contador += 1
            #ASOCIAR LA POSICION INICIAL Y FINAL DE LA MEMORIA AL MARCO

    def saveProgram(self, pcb, program):
        pages = []
        pageActual = Page(self.tamanioDeMarco)
        contador = 0
        marcoActual = self.getMarcoLibre() ## DAME MARCOS LIBRES
        for instruction in program.getInstrucciones():
            if pageActual.getTamanio >= contador:
                pageActual.addNroInstruction(pcb.getPc())
                self.memory.write(self.nextPosition(), instruction)
                contador += 1
            else:
                pageActual.asociarMarco(marcoActual) #TENGO QUE MARCAR EL MARCO COMO QUE ESTA USADO
                pages.append(pageActual)
                marcoActual = self.getMarcoLibre()
                pageActual = Page(self.tamanioMarco)
        pages.append(pageActual)
        self.blockTable.put(pcb.getPid(), pages)

    def hayEspacioPara(self, tamanio):
        contador = 0
        tamanioNecesario = tamanio/self.tamanioDeMarco
        for marco in self.marcos:
            if marco.getEstoyLibre:
                contador += 1
        return tamanioNecesario <= contador

    def nextPosition(self):
        pass ## COMO HAGO PARA DEVOLVER DOS VALORES

    def getMarcoLibre(self):
        for marco in self.marcos:
            if marco.getEstoyLibre:
               return marco