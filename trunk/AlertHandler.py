from Alert import KillAlert, TimeoutAlert, IOAlert, NewAlert

__author__ = 'memonono'


class Alerter:

    def __init__(self):
        self.alerts = [KillAlert(), TimeoutAlert(), IOAlert(), NewAlert()]

    def find(self, pcb):
        for alert in self.alerts:
            if alert.condition_of_applicability(pcb):
                return alert

    def alert_for(self, pcb):
        self.find(pcb)

