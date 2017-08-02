# -*- coding: utf-8 -*-
'''
bluetooth_module_test_serial.py defines test serial and mock serial classes

'''
from common.test_serial import TestSerial as CommonTestSerial

import logging


class TestSerial(CommonTestSerial):
    song_name = None
    author_name = None
    instruction = None
    class SerialException(Exception):
        pass

    def readline(self):
        '''
        Invoke readline method
        :return: Return one line data that read from serial port
        '''
        data = self.serial_port.readline()

        if 'MI' in str(data[0:len(data) - 2]):
            ba = bytearray(data[0:len(data) - 2])
            song_name_index = ba.find(b'\xff')
            self.song_name = ba[2:song_name_index].decode('utf-8')
            author_name_index = ba.find(b'\xff', song_name_index+1)
            self.author_name = ba[song_name_index+1:author_name_index].decode('utf-8')
            logging.info("Serial:" + self.serial_port.port + " song_name: "+self.song_name+"author_name: "+self.author_name)
        else:
            logging.info("Serial:" + self.serial_port.port + " Read:" + str(data[0:len(data) - 2].decode('utf-8')))
            self.instruction = str(data[0:len(data) - 2].decode('utf-8'))

        return self.instruction, self.author_name, self.song_name



