# -*- coding: utf-8 -*-
'''
actual_result.py derives from test_result.py
It defines actual result and bluetooth serials feedback 

'''
import logging


class TestInput:
    '''
    TestInput is general test input class
    :static variable sysExtEvt: system external events
    :static variable sysIntEvt: system internal events
    :static variable humanInputEvt: human input events
    :static variable mock_enable: True for mock enable, otherwise disable
    '''
    sysExtEvt = None
    sysIntEvt = None
    humanInputEvt = None
    mock_enable = False

    def __init__(self, mock_enable=False):
        '''
        constructor of TestInput
        :param mock_enable: True for mock enable, otherwise disable
        '''
        self.mock_enable = mock_enable
        if self.mock_enable:
            logging.debug('TestInput enable')
        else:
            logging.debug('TestInput')
