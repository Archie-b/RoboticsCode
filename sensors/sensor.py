from abc import abstractmethod
from busio import I2C


class Sensor:
    @abstractmethod
    def __init__(self, i2c: I2C) -> None: pass

    @abstractmethod
    def getCurrentState(self) -> object: pass

    @abstractmethod
    def sensorOK(self) -> bool: pass
