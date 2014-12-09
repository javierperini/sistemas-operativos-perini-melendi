from Alert import KillAlert, TimeoutAlert, IOAlert, NewAlert

__author__ = 'memonono'


class Alerter:

    def __init__(self, cpu):
        self.alerts = [KillAlert(cpu), TimeoutAlert(cpu), IOAlert(cpu), NewAlert(cpu)]
        self.cpu = cpu

    def find(self, pcb):
        for alert in self.alerts:
            if alert.condition_of_applicability(pcb):
                return alert

    def alert_for(self, pcb):
        self.find(pcb).alert_cpu(self.cpu)

