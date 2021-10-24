from abc import ABCMeta, abstractmethod

class Sensor:
    @abstractmethod
    def getCurrentState(self) -> object: pass

    @abstractmethod
    def sensorOK(self) -> bool: pass