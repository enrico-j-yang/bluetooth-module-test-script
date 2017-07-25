# -*- coding: utf-8 -*-
'''
test_serial.py defines test serial and mock serial classes 

'''
import logging

import serial


class MockSerial:
    '''
    MockSerial is mock serial class
    :static variable instance_counter: Record instance amount for different port identification
    :static variable waiting_bytes: Default waiting bytes
    :static variable readline_data: Default readline data
    '''
    instance_counter = 0
    waiting_bytes = len("Result=OK")
    readline_data = ("Result=OK" + '\r\n').encode("utf-8")

    def __init__(self):
        '''
        Constructor of MockSerial
        '''
        logging.debug("MockSerial")
        MockSerial.instance_counter += 1
        self.instance_counter = MockSerial.instance_counter

    @staticmethod
    def isOpen():
        logging.debug("MockSerial isOpen")

    @staticmethod
    def open():
        logging.debug("MockSerial open")

    @staticmethod
    def close():
        logging.debug("MockSerial close")

    @staticmethod
    def read(size=1):
        logging.debug("MockSerial read")
        return size

    @staticmethod
    def write(data):
        logging.debug("MockSerial write")
        return len(data)

    @staticmethod
    def flush():
        logging.debug("MockSerial flush")

    def inWaiting(self):
        '''
        Mock inWaiting bytes amount
        :return: Return default bytes amount when odd, return 0 when even
        '''
        logging.debug("MockSerial inWaiting")
        if self.waiting_bytes == 0:
            self.waiting_bytes = len("Result=OK")
            return 0
        else:
            self.waiting_bytes = 0
            return len("Result=OK")

    @staticmethod
    def outWaiting():
        logging.debug("MockSerial outWaiting")
        return 0

    def readline(self):
        logging.debug("MockSerial readline")
        return self.readline_data

    @property
    def port(self):
        return 'mock_port' + str(self.instance_counter)

    def mock_waiting_bytes(self, waiting_bytes):
        '''
        Mock waiting bytes
        :param waiting_bytes: Waiting bytes amount 
        :return: None
        '''
        self.waiting_bytes = waiting_bytes

    def mock_readline_data(self, readline_data):
        '''
        Mock readline data
        :param readline_data: One line mocked data
        :return: One line mocked data
        '''
        self.readline_data = (readline_data + '\r\n').encode("utf-8")


class TestSerial:
    '''
    TestSerial is test serial class
    :static variable serial_port: record instance amount for different port identification
    :static variable mock_enable: True for mock enable, otherwise disable
    :static constance: serial constance for serial open
    
    # serial byte size
    FIVEBITS = serial.FIVEBITS
    SIXBITS = serial.FIVEBITS
    SEVENBITS = serial.FIVEBITS
    EIGHTBITS = serial.FIVEBITS
    # serial parity
    PARITY_NONE = serial.PARITY_NONE
    PARITY_EVEN = serial.PARITY_EVEN
    PARITY_ODD = serial.PARITY_ODD
    PARITY_MARK = serial.PARITY_MARK
    PARITY_SPACE = serial.PARITY_SPACE
    # serial stopbits
    STOPBITS_ONE = serial.STOPBITS_ONE
    STOPBITS_ONE_POINT_FIVE = serial.STOPBITS_ONE_POINT_FIVE
    STOPBITS_TWO = serial.STOPBITS_TWO
    '''
    serial_port = None
    mock_enable = True

    # serial byte size
    FIVEBITS = serial.FIVEBITS
    SIXBITS = serial.SIXBITS
    SEVENBITS = serial.SEVENBITS
    EIGHTBITS = serial.EIGHTBITS
    # serial parity
    PARITY_NONE = serial.PARITY_NONE
    PARITY_EVEN = serial.PARITY_EVEN
    PARITY_ODD = serial.PARITY_ODD
    PARITY_MARK = serial.PARITY_MARK
    PARITY_SPACE = serial.PARITY_SPACE
    # serial stopbits
    STOPBITS_ONE = serial.STOPBITS_ONE
    STOPBITS_ONE_POINT_FIVE = serial.STOPBITS_ONE_POINT_FIVE
    STOPBITS_TWO = serial.STOPBITS_TWO

    class SerialException(Exception):
        pass

    def __init__(self,
                 port=None,
                 baudrate=9600,
                 bytesize=EIGHTBITS,
                 parity=PARITY_NONE,
                 stopbits=STOPBITS_ONE,
                 timeout=None,
                 xonxoff=False,
                 rtscts=False,
                 write_timeout=None,
                 dsrdtr=False,
                 inter_byte_timeout=None,
                 exclusive=None,
                 mock_enable=False):
        '''
        Constructor of TestSerial
        :param port: COM1 COM2 for windows, /dev/ttyUSB0 /dev/ttyUSB1 for linux, /dev/tty.wchusbserial14140 for Mac OS
        :param baudrate: Please refer to pyserial class serial.Serial
        :param bytesize: Please refer to pyserial class serial.Serial
        :param parity: Please refer to pyserial class serial.Serial
        :param stopbits: Please refer to pyserial class serial.Serial
        :param timeout: Please refer to pyserial class serial.Serial
        :param xonxoff: Please refer to pyserial class serial.Serial
        :param rtscts: Please refer to pyserial class serial.Serial
        :param write_timeout: Please refer to pyserial class serial.Serial
        :param dsrdtr: Please refer to pyserial class serial.Serial
        :param inter_byte_timeout: Please refer to pyserial class serial.Serial
        :param exclusive: Please refer to pyserial class serial.Serial
        :param mock_enable: True for mock enable, otherwise disable
        '''
        if mock_enable:
            self.mock_enable = mock_enable
            self.serial_port = MockSerial()
        else:
            self.serial_port = serial.Serial()
            self.serial_port.port = port
            self.serial_port.baudrate = baudrate
            self.serial_port.bytesize = bytesize
            self.serial_port.parity = parity
            self.serial_port.stopbits = stopbits
            self.serial_port.timeout = timeout
            self.serial_port.xonxoff = xonxoff
            self.serial_port.rtscts = rtscts
            self.serial_port.write_timeout = write_timeout
            self.serial_port.dsrdtr = dsrdtr
            self.serial_port.inter_byte_timeout = inter_byte_timeout
            self.serial_port.exclusive = exclusive
            self.serial_port.enable = mock_enable

        try:
            self.serial_port.open()
        except Exception as e:
            logging.error("error open serial port: " + str(e))

        logging.info("TestSerial port " + self.serial_port.port + " opened")

    def enable(self):
        '''
        Enable mock mode
        :return: None
        '''
        self.mock_enable = True

    def disable(self):
        '''
        Disable mock mode
        :return: None
        '''
        self.mock_enable = False

    def is_enable(self):
        '''
        Check mock mode
        :return: mock mode, True for enable, False for disable
        '''
        return self.mock_enable

    def isOpen(self):
        '''
        Invoke serial flush method
        :return: None
        '''
        self.serial_port.isOpen()

    def close(self):
        '''
        Invoke serial close method
        :return: None
        '''
        self.serial_port.close()

    def read(self, size=1):
        '''
        Invoke serial read method
        :param size: Read data size
        :return: Data returned by serial port
        '''
        return self.serial_port.read(size)

    def write(self, data):
        '''
        Invoke serial write method
        :param data: Write data to serial port
        :return: Number of bytes written.
        '''
        logging.info("Serial:" + self.serial_port.port + " Send:" + data)
        return self.serial_port.write((data + "\r\n").encode("utf-8"))

    def flush(self):
        '''
        Invoke serial flush method
        :return: None
        '''
        self.serial_port.flush()

    def inWaiting(self):
        '''
        Invoke inWaiting method
        :return: in waiting amount
        '''
        return self.serial_port.inWaiting()

    def outWaiting(self):
        '''
        Invoke outWaiting method
        :return: out waiting amount
        '''
        return self.serial_port.outWaiting()

    def readline(self):
        '''
        Invoke readline method
        :return: Return one line data that read from serial port
        '''
        data = self.serial_port.readline()
        logging.info("Serial:" + self.serial_port.port + " Read:" + str(data[0:len(data) - 2].decode('utf-8')))
        return str(data[0:len(data) - 2].decode('utf-8'))

    def mock_waiting_bytes(self, waiting_bytes):
        '''
        Mock waiting bytes
        :param waiting_bytes: Waiting bytes amount if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.serial_port.mock_waiting_bytes(waiting_bytes)

    def mock_readline_data(self, readline_data):
        '''
        Mock readline data
        :param readline_data: One line mocked data if mock enable
        :return: One line mocked data
        '''
        if self.mock_enable:
            self.serial_port.mock_readline_data(readline_data)
