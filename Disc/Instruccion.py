class Instruccion:

    def __init__(self, text):
        self.texto = text

    def run(self, output):
        output.agregarInstruccion(self.texto)

