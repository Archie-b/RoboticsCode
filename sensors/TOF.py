from typing import List
from sensors.sensor import Sensor
from serial import Serial

from system.TOFData import TOFData


class TOF(Sensor):
    TOF_length: int = 16
    TOF_header: tuple = (87, 0, 255)
    data: TOFData
    ser: Serial

    def __init__(self):
        ser = Serial('/dev/ttyS0', 115200)
        ser.flushInput()

    def verifyCheckSum(self, data, len) -> bool:
        TOF_check = 0
        for k in range(0, len-1):
            TOF_check += data[k]
        TOF_check = TOF_check % 256

        return TOF_check == data[len-1]

    def getCurrentState(self) -> TOFData:
        TOF_data: List[int]
        if self.ser.inWaiting() >= 32:
            for i in range(0, 16):
                TOF_data.append(ord(self.ser.read(1)))
            for j in range(0, 16):
                if((TOF_data[j] == self.TOF_header[0] and TOF_data[j+1] == self.TOF_header[1]
                        and TOF_data[j+2] == self.TOF_header[2])
                        and (self.verifyCheckSum(TOF_data[j:self.TOF_length], self.TOF_length))):
                    if(((TOF_data[j+12]) | (TOF_data[j+13] << 8)) == 0):
                        return TOFData()
                    else:
                        self.TOF_system_time = TOF_data[j+4] | TOF_data[j +
                                                                        5] << 8 | TOF_data[j+6] << 16 | TOF_data[j+7] << 24
                        self.TOF_distance = (
                            TOF_data[j+8]) | (TOF_data[j+9] << 8) | (TOF_data[j+10] << 16)
                        self.TOF_status = TOF_data[j+11]
                        self.TOF_signal = TOF_data[j+12] | TOF_data[j+13] << 8

        return self.data
