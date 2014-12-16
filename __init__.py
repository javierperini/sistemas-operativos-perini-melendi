from Cpu.Cpu import Cpu
from Kernel.Kernel import Kernel
from Kernel.Programa import Programa
from Memory.Memory import Memory
from Disc.FileSystem import FileSystem
from Cpu.Clock import Clock
from Disc.Instruccion import Instruccion
from Disc.Disc import Disc


class Init():

    def __init__(self):
        self.clock = Clock(2)
        self.clock.start()
        self.disc = Disc()
        self.program = Programa("a_program_name")
        self.program2 = Programa("another_program_name")
        self.program3 = Programa("yes_another_program_name")
        self.program4 = Programa("Hm.. blah")
        self.instruction1 = Instruccion("Instruccion 1")
        self.instruction2 = Instruccion("Instruccion 2")
        self.instruction3 = Instruccion("Instruccion 3")

        self.instruction4 = Instruccion("Instruccion 4")
        self.instruction5 = Instruccion("Instruccion 5")
        self.instruction6 = Instruccion("Instruccion 6")

        self.instruction7 = Instruccion("Instruccion 7")
        self.instruction8 = Instruccion("Instruccion 8")
        self.instruction9 = Instruccion("Instruccion 9")

        self.instruction10 = Instruccion("Instruccion 10")
        self.instruction11 = Instruccion("Instruccion 11")
        self.instruction12 = Instruccion("Instruccion 12")

        self.program.agregarInstruccion(self.instruction1)
        self.program.agregarInstruccion(self.instruction2)
        self.program.agregarInstruccion(self.instruction3)

        self.program2.agregarInstruccion(self.instruction4)
        self.program2.agregarInstruccion(self.instruction5)
        self.program2.agregarInstruccion(self.instruction6)

        self.program3.agregarInstruccion(self.instruction7)
        self.program3.agregarInstruccion(self.instruction8)
        self.program3.agregarInstruccion(self.instruction9)

        self.program4.agregarInstruccion(self.instruction10)
        self.program4.agregarInstruccion(self.instruction11)
        self.program4.agregarInstruccion(self.instruction12)

        self.memory = Memory()
        self.kernel = Kernel(self.memory, FileSystem(self.disc), self.clock)
        self.kernel.set_scheduler_policy()
        self.kernel.create_pcb(self.program, 0)
        self.kernel.create_pcb(self.program2, 1)
        self.kernel.create_pcb(self.program3, 2)
        self.kernel.create_pcb(self.program4, 3)
        self.cpu = Cpu(self.kernel)

    def main(self):
        self.cpu.run()

if __name__ == '__main__':
    Init().main()

