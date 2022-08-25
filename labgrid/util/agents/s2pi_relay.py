"""
This module implements switching for the 52pi Docker Pi 4 channel relay

Supported modules:

- Docker Pi 4 Channel Relay

Supported Functionality:

- Turn digital output on and off
"""
import smbus

ON = 0xff
OFF = 0x00

class S2PiRelay:
    def __init__(self, busnum, devnum):
        self.bus = smbus.SMBus(busnum)
        self.address = devnum

    def set_output(self, number, status):
        assert 1 <= number <= 8
        self.bus.write_byte_data(self.address, number, ON if status else OFF)

    def get_output(self, number):
        assert 1 <= number <= 4
        state = self.bus.read_byte_data(self.address, number)
        return False if (state == OFF) else True

def handle_set(busnum, devnum, number, status):
    relay = S2PiRelay(busnum, devnum)
    relay.set_output(number, status)


def handle_get(busnum, devnum, number):
    relay = S2PiRelay(busnum, devnum)
    return relay.get_output(number)


methods = {
    'set': handle_set,
    'get': handle_get,
}
