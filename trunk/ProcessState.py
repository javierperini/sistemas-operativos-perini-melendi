from enum import Enum


class Estado(Enum):
    new = 1
    ready = 2
    running = 3
    waitng = 4
    terminated = 5


