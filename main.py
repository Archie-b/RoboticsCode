
from sensors.sensor import Sensor
from system.statePicker import StatePicker
from typing import List
from states.state import State
from adafruit_blinka import board
from busio import I2C
from system.management import Management

def main():
    i2c: I2C = board.I2C()
    management : Management = Management()

    # pull all our states into a single list so we know what we're working with
    stateList: List[State] = management.getStates()
    # pull all our sensors into a single list so we know what we're working with
    sensorList: List[Sensor] = management.getSensors(i2c)

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
