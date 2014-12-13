from Cpu.Alert import KillAlert, TimeoutAlert, IOAlert, NewAlert


class Alerter:

    def __init__(self, cpu, scheduler, pcb_table):
        self.alerts = [KillAlert(cpu, scheduler, pcb_table), TimeoutAlert(cpu, scheduler, pcb_table), IOAlert(cpu, scheduler, pcb_table), NewAlert(cpu, scheduler, pcb_table)]
        self.cpu = cpu

    def find(self, pcb):
        for alert in self.alerts:
            if alert.condition_of_applicability(pcb):
                return alert

    def alert_for(self, pcb):
        self.find(pcb).alert_cpu(self.cpu)

