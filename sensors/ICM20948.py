from system.vector import Vector
from .sensor import Sensor
from typing import Tuple
from adafruit_icm20x import ICM20649
from busio import I2C

SensorData = Tuple[float, float, float]

class ICM20948(Sensor):

    i2c : I2C
    icm : ICM20649  

    def __init__(self, i2c) -> None:
        self.i2c = i2c
        self.icm = ICM20649(i2c)

    def getCurrentState(self) -> Tuple[Vector, Vector, Vector]:
        acceleration : SensorData = self.icm.acceleration
        gyro : SensorData = self.icm.gyro
        magnetic : SensorData = self.icm.magnetic

        return (self.convert(acceleration), self.convert(gyro), self.convert(magnetic))
    
    def getVectorFromSensorData(self, data:SensorData) -> Vector:
        return Vector(data[0],data[1],data[2],0)

    convert = getVectorFromSensorData 

