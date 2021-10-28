
from os import stat
from sensors.sensor import Sensor
from system.statePicker import StatePicker
from typing import List
from states.state import State
from adafruit_blinka import board
from busio import I2C

import sys
import inspect


def getStates() -> List[State]:
    stateList: List[State] = []
    for name, obj in inspect.getmembers(sys.modules['states']):
        if inspect.isclass(obj):
            stateList.append(obj())
    return stateList


def getSensors(i2c: I2C) -> List[Sensor]:
    sensorList: List[Sensor] = []
    for name, obj in inspect.getmembers(sys.modules['sensors']):
        if inspect.isclass(obj):
            sensorList.append(obj(i2c))
    return sensorList


def main():
    i2c: I2C = board.I2C()

    # pull all our states into a single list so we know what we're working with
    stateList: List[State] = getStates()
    # pull all our sensors into a single list so we know what we're working with
    sensorList: List[Sensor] = getSensors(i2c)

    # make sure nothing has gone wrong
    if stateList.count != 0:
        # initiate our picker with the list
        statePicker: StatePicker = StatePicker(stateList)
        state: State

        # loop forever
        while 1 < 2:
            # pick our first state
            state = statePicker.getValidState(sensorList)


main()
