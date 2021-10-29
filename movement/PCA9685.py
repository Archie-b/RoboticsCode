from busio import I2C
from adafruit_pca9685 import PCA9685 as pcaX
from adafruit_servokit import ServoKit

# SERVO TABLE
# Pin 0 : right front ankle
# Pin 1 : left front ankle
# Pin 2 : left rear ankle
# Pin 3 : right rear ankle

# Pin 4 : right front shoulder f/b
# Pin 5 : left front shoulder f/b
# Pin 6 : left rear shoulder f/b
# Pin 7 : right rear shoulder f/b

# Pin 8 : right front shoulder u/d
# Pin 9 : left front shoulder u/d
# Pin 10 : left rear shoulder u/d
# Pin 11 : right rear shoulder u/d


class PCA9685:
    i2c: I2C
    pca: pcaX
    kit : ServoKit

    def __init__(self, i2c: I2C) -> None:
        self.i2c = i2c
        self.pca = pcaX(i2c)
        self.pca.frequency = 60
        self.kit = ServoKit(channels=16)


    def initMovementRanges(self):
        for x in range(12):
            self.pca.channel[x].duty_cycle = 0

    def moveServo(self, servo: int, distance: float) -> bool:
        return False

    def setServoPosition(self, servo: int, distance: float) -> bool:
        return False

