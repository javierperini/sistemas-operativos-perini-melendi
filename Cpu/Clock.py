import threading


class Clock:

    def __init__(self, interval):
        self.interval = interval

    def tick(self):
        threading.Timer(self.interval)

