from states.state import State
from typing import List

class StatePicker():

    stateList:List[State]

    def __init__(self, states:List[State]):
        self.stateList = states

    def getValidState(self, sensorState) -> State:
        for state in self.stateList:
            print(state)


