class AdministradorDeMemoria:
    def __init__(self, memoria, strategy):
        self.memoria = memoria
        self.strategy = strategy

    def almacenar(self, pcb, programa):
        self.strategy.saveAlmacenar(pcb, programa)

    def hayEspacioPara(self, tamanio):
        self.strategy.hayEspacioPara(tamanio)

    def nextPost(self):
        return self.strategy.getNextInstruction()

    def readMemory(self, programa):
        return self.strategy.getNextInstruction(programa)

    def deleteMemory(self, programa):
        self.strategy.deleteMemory(programa)
