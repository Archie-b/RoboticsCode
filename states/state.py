from abc import ABCMeta, abstractmethod
from typing import List

class State(metaclass=ABCMeta):

    requiredSensors: List[str]

    @abstractmethod
    def entrance(self) -> bool: pass

    @abstractmethod
    def exit(self) -> bool: pass

    @abstractmethod
    def execute(self) -> bool: pass

    @abstractmethod
    def interrupt(self) -> bool: pass
