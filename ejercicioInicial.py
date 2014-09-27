class Instruccion :

    def __init__(self,texto):
        self.texto =texto

	def run(sf):
	    print self.texto

class Programa:

	def __init__(self):
		self.instrucciones=[]

	def agregarInstruccion(self,instruccion):
		self.instrucciones.append(instruccion)
	
	def ejecutar(self):
		for instruccion in self.instrucciones:
			instruccion.run()

	def getInstrucciones(self):
		return self.instrucciones

		
class Kernel:

	def ejecutar(self,programa):
		programa.ejecutar()
'''
class Main:

	def main():
		instr1=Instruccion('Primera instruccion')
		instr2=Instruccion('Segunda instruccion')
		program=Programa()
		program.agregarInstruccion(instr1)
		program.agregarInstruccion(instr2)
		print(len(program.getInstrucciones()))
		kernel=Kernel()		
		kernel.ejecutar(program)

	if __name__ == "__main__":
		main()	'''
	

import unittest

class ProgramaTest(unittest.TestCase):
	
	def agregarInstruccion_test(self):
		programa= Programa()
		instr= Instruccion('Algo')
		programa.agregarInstruccion(instr)
		self.assertEquals(len(programa.getInstrucciones()),1)

	
if __name__ == "__main__":
     unittest.main()
			


