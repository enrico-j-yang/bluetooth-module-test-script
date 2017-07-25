# -*- coding: utf-8 -*-
'''
expected_result.py derives from test_result.py
It defines expected result serial feedback 

'''
import sys

sys.path.append("../..")

from common.test_result import TestResult


class ExpectedResult(TestResult):
    '''
    ExpectedResult derives from TestResult
    '''

    def __init__(self):
        '''
        constructor of ExpectedResult
        '''
        super(ExpectedResult, self).__init__()
