
from os import stat
from sensors.sensor import Sensor
from system.statePicker import StatePicker
from typing import List
from states.state import State

import sys
import inspect

def getStates() -> List[State]:
    stateList : List[State] = []
    for name, obj in inspect.getmembers(sys.modules['states']):
        if inspect.isclass(obj):
            stateList.append(obj())
    return stateList

def getSensors() -> List[Sensor]:
    sensorList : List[Sensor] = []
    for name, obj in inspect.getmembers(sys.modules['sensors']):
        if inspect.isclass(obj):
            sensorList.append(obj())
    return sensorList

def main():
    #pull all our states into a single list so we know what we're working with
    stateList : List[State] = getStates()
    #pull all our sensors into a single list so we know what we're working with
    sensorList : List[Sensor] = getSensors()
    
    #make sure nothing has gone wrong
    if stateList.count != 0:
        #initiate our picker with the list
        statePicker : StatePicker = StatePicker(stateList)
        state : State

        #loop forever
        while 1 < 2:
            #pick our first state
            state = statePicker.getValidState(sensorList)


main()
