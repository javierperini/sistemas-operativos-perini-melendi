from AlertHandler import Alerter

__author__ = 'memonono'


class CPU():

    def __init__(self, memory):
        self.alerter = Alerter()
        self.memory = memory

#Threadear aqui |||
    #           $$$
    def run(self, pcb):
        self.memory.instructions_for(pcb.posicion_ini)
        self.alerter.alert_for(pcb)



#Hacer algo
#Lo que va a hacer es ir a buscar a memoria las instrucciones
#cargadas del proximo proceso a ejecutar.

#El reloj tira un Tick cada x cantidad de tiempo
#puede ser un thread, un while, o usar time y tirar un notify cada x cantidad de tiempo