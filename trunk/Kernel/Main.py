from Kernel import *
from Memory.Memory import *
from Disc.FileSystem import *


class Main:

    def main(self):
        memoria = Memory()
        file_system = FileSystem()
        kernel = Kernel(memoria, file_system)
        kernel.execute()

    if __name__ == "__main__":
                main()

