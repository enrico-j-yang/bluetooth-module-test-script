# -*- coding: utf-8 -*-
'''
human_input.py derives from test_input.py
It defines human input event class and methods 

'''
import logging
import sys
from time import sleep

sys.path.append("../..")

from common.test_input import TestInput


class UnknownResultError(Exception):
    pass


class HumanInput(TestInput):
    '''
    HumanInput derives from TestInput
    It implements mock result and actual result read from serial of result and bluetooth ports
    It uses a dictionary to store actual results 
    :static variable mode: e-bike signal mode, 1wire or GPIO
    :static variable period: control board signal period in mili-second
    :static variable control_board_serial_port: control board serial port handler
    :static variable bluetooth_serial_port: bluetooth serial port handler
    '''
    mode = "GPIO"
    period = 0
    control_board_serial_port = None
    bluetooth_serial_port = None

    def __init__(self, control_board_serial_port, bluetooth_serial_port, mock_enable=False):
        '''
        constructor of HumanInput
        :param control_board_serial_port: control board serial port handler
        :param bluetooth_serial_port: bluetooth serial port handler
        :param mock_enable: True for mock enable, otherwise disable
        '''
        super(HumanInput, self).__init__(mock_enable)
        self.control_board_serial_port = control_board_serial_port
        self.bluetooth_serial_port = bluetooth_serial_port

    def send(self, value):
        '''
        send human input event, send value to control board serial port
        :param value: human input event value
        :return: True for event accepted, False for event rejected by control board
        '''
        # write test command to serial port
        self.control_board_serial_port.write(value)

        out_bytes = ''
        # let's wait one second before reading output (let's give device time to answer)
        sleep(0.1)
        out_buffer_bytes = self.control_board_serial_port.inWaiting()
        while out_buffer_bytes > 0:
            out_bytes = self.control_board_serial_port.readline()
            if out_bytes != '':
                logging.info(out_bytes)
            out_buffer_bytes = self.control_board_serial_port.inWaiting()

        logging.debug("out_bytes:" + out_bytes)

        if self.mock_enable:
            if out_bytes == 'Result=OK':
                return True
            elif out_bytes == 'Result=Fail':
                return False
            else:
                raise UnknownResultError
        '''
        if str(out_bytes[0:len(out_bytes) - 2].decode('UTF-8')) == 'Result=OK':
            return True
        elif str(out_bytes[0:len(out_bytes) - 2].decode('UTF-8')) == 'Result=Fail':
            return False
        else:
            raise UnknownResultError
        '''

    def set_mode(self, mode):
        '''
        set e-bike signal mode, 1wire or GPIO
        :param mode: 1wire or GPIO
        :return: None
        '''
        self.mode = mode
        self.send("Mode=" + mode)

    def set_signal_period(self, period):
        '''
        set signal period for control board 
        :param period: control board signal period in mili-second
        :return: None
        '''
        self.send("SignalPeriod=" + str(period))
        self.period = period

    def start_generate_signal(self):
        '''
        start generate signal to control board
        :return: None
        '''
        self.send("Signal=Start")

    def stop_generate_signal(self):
        '''
        stop generate signal to control board
        :return: None
        '''
        self.send("Signal=Stop")

    def mock_prompt(self, prompt):
        '''
        prompt and get input when mock is disable. if mock is enable no prompt displays
        :param prompt: text that displays  
        :return: None
        '''
        if self.mock_enable:
            pass
        else:
            return input(prompt)
