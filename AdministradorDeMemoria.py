class AdministradorDeMemoria:
    def __init__(self, memoria):
        self.memoria = memoria

    def almacenar(self, programa):
        if self.memoria.hayEspacioPara(programa.size()):
                self.safeAlmacenar(programa)

    def safeAlmacenar(self, programa):
        for instr in programa.instrucciones():
            self.memoria.write(self.siquientePosicion(), instr)

    def siguientePosicion(self):
        return self.memoria.siguientePosicion()

