from typing import NoReturn


class Vector:
    x : float
    y : float
    z : float
    mag : float

    def __init__(self, x:float,y:float,z:float,mag:float)->None :
        self.x = x
        self.y = y
        self.z = z
        self.mag = mag
