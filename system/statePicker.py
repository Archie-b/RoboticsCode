from states.state import State
from typing import List,Any

class StatePicker():

    stateList:List[State]

    def __init__(self, states:List[State]):
        self.stateList = states

    def getValidState(self, sensorState) -> Any:
        for state in self.stateList:
            print(state)
        return None


