__author__ = 'javier'


class Scheduling:
    def __init__(self):
        raise ReferenceError


class RoundRobin(Scheduling):
    def __init__(self, quantom):
        self.cola = []

    def dameUnPcb(self, cola):
        # que proceso le doy con round robin, si solo le agrega un tiempo al proceso

class