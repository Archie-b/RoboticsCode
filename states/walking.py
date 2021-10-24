from state import State
from typing import List

class Walking(State):
    
    def entrance(self) -> bool:
        return True

    def exit(self) -> bool:
        return True

    def execute(self) -> bool:
        return True
        
    def interrupt(self) -> bool:
        return True
