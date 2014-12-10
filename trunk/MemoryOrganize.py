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

    def saveProgram(self, pcb, program):
        pass

    def nextPosition(self, pcb):
        pass

    def getNextInstruction(self, pcb):
        return self.memory.read(self.nextPosition(pcb))

    def deleteMemory(self, instruction):
        self.memory.delete(instruction)


class AsignacionContinua(MemoryOrganize):

    def __init__(self, memory):
        super.__init__(memory)
        self.bloques = []

    def hayEspacioPara(self, tamanio):
        self.compactar()
        return self.memory.hayEspacioParaGuardar(tamanio)

    def saveProgram(self, pcb, program):
        bloque = Block(program.size(), program.nombre, self.nextPosition(), self.nextPosition()+program.size())
        self.guardarBloque(bloque)
        for instruction in program.getInstrucciones():
            self.memory.write(self.nextPositionLibre(), instruction)

    def nextPosition(self, pcb):
        ## BLOQUE PROXIMA INSTRUCCION A LEER
        return self.meoro(pcb)

    def deleteMemory(self, indice):
        self.memory.delete(indice)

    def compactar(self):
        for i in

    def guardarBloque(self, bloque):
        self.bloques.append(bloque)


class Paginacion(MemoryOrganize):

    def __init__(self, memory):
        super.__init__(memory)
        self.tamanioDeMarco = 5
        self.numeroDeMarcos = memory.getTamanio/self.tamanioDeMarco
        self.marcos = self.crearMarcos

    def crearMarcos(self):
        contador = 0
        tamanio_ant = 0
        marquitos = []
        while self.numeroDeMarcos > contador:
            pos_final = tamanio_ant + self.tamanioDeMarco
            marco = Marco(contador+1, self.tamanioDeMarco, tamanio_ant, pos_final)
            self.marquitos.append(marco)
            tamanio_ant = pos_final + 1
            contador += 1

        return marquitos

    def saveProgram(self, pcb, program):
        pages = []
        contador = 0
        marcoActual = self.getMarcoLibre() ## DAME MARCO LIBRES
        pageActual = Page(marcoActual)
        for instruction in program.getInstrucciones():
            if pageActual.getTamanio >= contador:
                pageActual.addNroInstruction(pcb.getPc())
                self.memory.write(self.nextPosition(), instruction)
                contador += 1
            else:
                contador = 0
                pages.append(pageActual)
                marcoActual = self.getMarcoLibre()
                pageActual = Page(marcoActual)
        pages.append(pageActual)
        self.blockTable.put(pcb.getPid(), pages)
        #DEBERIA SER UN BLOQUE LA CONCHA DE TU MADRE

    def hayEspacioPara(self, tamanio):
        contador = 0
        tamanioNecesario = tamanio/self.tamanioDeMarco
        for marco in self.marcos:
            if marco.getEstoyLibre:
                contador += 1
        return tamanioNecesario <= contador

    def nextPosition(self, pcb):
        # TENGO QUE IR AL MARCO Y PEDIRLE  LA INSTRUCCION QUE ESTOY BUSCANDO
        numeroDeMarco = pcb.pid/self.tamanioDeMarco
        marco = self.getMarco(numeroDeMarco)
        numeroDeInstruccion = pcb.getPc % self.tamanioDeMarco
        return marco.next_post(numeroDeInstruccion)

    def getMarco(self, numeroDeMarcoBuscado):
            for marco in self.marcos:
                if marco.getNumero == numeroDeMarcoBuscado:
                    return marco

    def getMarcoLibre(self):
        for marco in self.marcos:
            if marco.getEstoyLibre:
               return marco