from enum import Enum


class Status(Enum):
    RUNNING = 1
    PAUSED = 2
    VIDEO = 3
    STOP = 0


class ObS(Enum):
    ALIVE = 1
    DEAD = 0
    RELOADING = 3
