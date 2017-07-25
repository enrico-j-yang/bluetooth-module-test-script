# -*- coding: utf-8 -*-
'''
test_result.py defines general test result class and its methods
'''
import logging


class TestResult:
    '''
    TestResult is general test result class
    :static variable dist: test result dictionary
    :static variable mock_enable: True for mock enable, otherwise disable
    '''
    dist = {}
    mock_enable = False

    def __init__(self, mock_enable=False):
        '''
        constructor of TestResult
        :param mock_enable: True for mock enable, otherwise disable
        '''
        self.mock_enable = mock_enable
        if self.mock_enable:
            logging.debug('TestResult enable')
        else:
            logging.debug('TestResult')

    def set_value(self, key, value):
        '''
        set dictionary value according to specified key
        :param key: test result dictionary key
        :param value: test result dictionary value
        :return: None
        '''
        self.dist[key] = value

    def mock_value(self, key, value):
        '''
        set dictionary value according to specified key if mock is enabled
        :param key: test result dictionary key
        :param value: test result dictionary value
        :return: None
        '''
        if self.mock_enable:
            self.set_value(key, value)

    def get_value(self, key):
        '''
        get dictionary value according to specified key
        :param key:  test result dictionary key
        :return: test result dictionary value
        '''
        return self.dist[key]
