class Block:

    def __init__(self, tamanio, pid, posicionInicial, posicionFinal):
        self.tamanio = tamanio
        self.pid = pid
        self.posicionInicial = posicionInicial
        self.posicionFinal = posicionFinal
        self.posicion_read = posicionInicial
        self.usado = False

    def getTamanio(self):
        return self.tamanio

    def get_usado(self):
        return self.usado

    def next_pos(self):
        position = self.posicion_read
        self.posicion_read += 1
        if position == self.getPosicionFinal():
            self.usado = True
        return position

    def get_pid(self):
        return self.pid

    def getPosicionInicial(self):
        return self.posicionInicial

    def getPosicionFinal(self):
        return self.posicionFinal

    def setPosicionFinal(self, posicion):
        self.posicionFinal = posicion

    def setPosicionInicial(self, posicion):
        self.posicionInicial = posicion
