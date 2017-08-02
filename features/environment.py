# -*- coding: utf-8 -*-
'''
environment.py is pre-process and post-process for all step implementation files

'''
import logging
import platform
import sys
from time import sleep

from common.test_input import TestInput
from common.human_input import HumanInput
from common.system_internal_event import SystemInternalEvent
from common.system_external_event import SystemExternalEvent
from common.expected_result import ExpectedResult
from bluetooth_module.bluetooth_module_actual_result import ActualResult
from bluetooth_module.bluetooth_module_test_serial import TestSerial

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='bluetooth_module_test.log',
                    filemode='w')


class PlatformNotSupportedError(Exception):
    pass


def before_all(context):
    '''
    Initial serial ports, test input, test result. Set mock_enable to True to enable mock mode.
    :param context: behave global variable
    :return: None
    '''
    if platform.system() == 'Windows':
        try:
            context.bluetooth_serial_port = TestSerial(port='COM4',
                                                       baudrate=9600,
                                                       timeout=0,
                                                       parity=TestSerial.PARITY_NONE,
                                                       stopbits=TestSerial.STOPBITS_ONE,
                                                       bytesize=TestSerial.EIGHTBITS,
                                                       mock_enable=False)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")

    elif platform.system() == 'Darwin':
        context.bluetooth_serial_port = None
        try:
            context.bluetooth_serial_port = TestSerial(port='/dev/tty.wchusbserial14140',
                                                       baudrate=9600,
                                                       timeout=0,
                                                       parity=TestSerial.PARITY_NONE,
                                                       stopbits=TestSerial.STOPBITS_ONE,
                                                       bytesize=TestSerial.EIGHTBITS,
                                                       mock_enable=False)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")
    else:
        logging.error("platform:" + platform.system() + "not supported")
        raise PlatformNotSupportedError

    context.florenceTestInput = TestInput()
    context.florenceTestInput.sysHIEvt = HumanInput(None, context.bluetooth_serial_port,
                                                    mock_enable=False)
    context.florenceTestInput.sysIntEvt = SystemInternalEvent(context.bluetooth_serial_port, mock_enable=False)
    context.florenceTestInput.sysExtEvt = SystemExternalEvent(None, mock_enable=False)
    context.florenceExpRes = ExpectedResult()
    context.florenceActRes = ActualResult(None, context.bluetooth_serial_port, mock_enable=False)


def after_all(context):
    '''
    Close all serial port after all feature done
    :param context: behave global variable
    :return: None
    '''
    context.bluetooth_serial_port.close()

# def before_feature(context, feature):
#    context = context

# def after_feature(context, feature):
#    context = context


# def before_scenario(context, scenario):
#    context = context


# def after_scenario(context, scenario):
#    context = context
