from typing import List
from states.state import State
import inspect
import sys
from sensors.sensor import Sensor
from busio import I2C

class Management:
    def getStates(self) -> List[State]:
        stateList: List[State] = []
        for name, obj in inspect.getmembers(sys.modules['states']):
            if inspect.isclass(obj):
                stateList.append(obj())
        return stateList


    def getSensors(self, i2c: I2C) -> List[Sensor]:
        sensorList: List[Sensor] = []
        for name, obj in inspect.getmembers(sys.modules['sensors']):
            if inspect.isclass(obj):
                sensorList.append(obj(i2c))
        return sensorList