import threading

__author__ = 'memonono'


class Clock:

    def __init__(self, interval):
        self.interval = interval

    def tick(self):
        threading.Timer(self.interval)

