from Kernel import *
from Memory.Memoria import *
from Disc.FileSystem import *


class Main:

    def main(self):
        memoria = Memoria()
        file_system = FileSystem()
        kernel = Kernel(memoria, file_system)
        kernel.ejecutar()

    if __name__ == "__main__":
                main()

