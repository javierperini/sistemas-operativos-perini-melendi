from Block import Block
from Marco import *
from BlockTable import *
from Page import *

__author__ = 'javier matias camila'


class MemoryOrganize(object):

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
        super(AsignacionContinua).__init__(memory)
        self.bloques = []

    def __new__(cls, *args, **kwargs):
        raise ReferenceError

    def hayEspacioPara(self, tamanio):
        self.compactar()
        return self.memory.free_memory_to_save(tamanio)

    def saveProgram(self, pcb, program):
        posicion = self.nextPosition(pcb)
        size = program.size()
        block = Block(size, pcb.pid, posicion, posicion+size)
        self.guardarBloque(block)
        for instruction in program.getInstrucciones():
            self.memory.write(self.nextPosition(pcb), instruction)

    def nextPosition(self, pcb):
        block = self.getBloque(pcb)
        pcb.sum_pc()
        return block.next_pos()

    def getBloque(self, pcb):
        for i in self.bloques:
            if i.get_pid == pcb:
                return i

    def deleteMemory(self, indice):
        self.memory.delete(indice)

    def compactar(self):
        borrar = []
        for i in self.bloques:
            if i.get_usado:
                self.delete_block_memory(i)
                borrar.append(i)
        self.delete_blocks(borrar)

    def delete_blocks(self, list_delete):
        for i in list_delete:
            self.bloques.remove(i)

    def delete_block_memory(self, bloque):
        posicion_inicial = bloque.getPosicionInicial
        posicion_final = bloque.getPosicionFinal
        self.reasignar_block(bloque.get_pid, posicion_inicial, posicion_final)

    def asignar_posicion_block(self, con_final, con_ini, diferecia_fija, diferencia_block, i):
        if diferencia_block == diferecia_fija:
            i.setPosicionFinal(con_final)
            i.setPosicionInicial(con_ini)
        else:
            if diferencia_block > diferecia_fija:
                i.setPosicionInicial(con_ini)
                i.setPosicionFinal(con_final + 1)
            else:
                i.setPosicionInicial(con_ini)
                i.setPosicionFinal(con_final - 1)

    def reasignar_block(self, pid, posicion_ini, posicion_fin):
        con_ini = posicion_ini
        con_final = posicion_fin
        diferecia_fija = con_final - con_ini
        for i in self.bloques:
            if i.get_pid != pid:
                pos_final_actual = i.getPosicionFinal
                pos_inicial_actual = i.getPosicionInicial
                diferencia_block = pos_final_actual - pos_inicial_actual
                self.asignar_posicion_block(con_final, con_ini, diferecia_fija, diferencia_block, i)
                self.pasar_datos(i, pos_final_actual, pos_inicial_actual)
                con_ini = i.getPosicionInicial
                con_final = i.getPosicionFinal

    def pasar_datos(self, block, pos_final, pos_ini):
        count = pos_ini
        for i in range(block.posicionInicial, block.posicionFinal):
            if count >= pos_final:
                self.memory.write(self.memory.read(count), i)
                count += 1
            else:
                break

    def guardarBloque(self, bloque):
        self.bloques.append(bloque)


class Paginacion(MemoryOrganize):

    def __init__(self, memory):
        super(Paginacion).__init__(memory)
        self.tamanioDeMarco = 5
        self.numeroDeMarcos = memory.getTamanio/self.tamanioDeMarco
        self.marcos = []
        self.crearMarcos()

    def crearMarcos(self):
        contador = 0
        tamanio_ant = 0
        while self.numeroDeMarcos > contador:
            pos_final = tamanio_ant + self.tamanioDeMarco
            marco = Marco(contador+1, self.tamanioDeMarco, tamanio_ant, pos_final)
            self.marcos.append(marco)
            tamanio_ant = pos_final + 1

    def saveProgram(self, pcb, program):
        pages = []
        contador = 0
        marcoActual = self.getMarcoLibre()
        pageActual = Page(marcoActual)
        for instruction in program.getInstrucciones():
            if pageActual.getTamanio >= contador:
                pageActual.addNroInstruction(pcb.getPc())
                self.memory.write(self.nextPosition(pcb), instruction)
                contador += 1
            else:
                contador = 0
                pages.append(pageActual)
                marcoActual = self.getMarcoLibre()
                pageActual = Page(marcoActual)
        pages.append(pageActual)
        self.blockTable.put(pcb.getPid(), pages)

    def hayEspacioPara(self, tamanio):
        contador = 0
        tamanioNecesario = tamanio/self.tamanioDeMarco
        for marco in self.marcos:
            if marco.getEstoyLibre:
                contador += 1
        return tamanioNecesario <= contador

    def nextPosition(self, pcb):
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