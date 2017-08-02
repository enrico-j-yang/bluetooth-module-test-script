# -*- coding: utf-8 -*-
"""
bluetooth_module_actual_result.py derives from test_result.py
It defines actual result and bluetooth serials feedback

"""
import logging
from time import sleep
from common.actual_result import ActualResult as CommonActualResult


class ActualResult(CommonActualResult):

    result_serial_port = None
    bluetooth_serial_port = None
    dist = {}

    def get_value_from_multi_line(self, key, expected_value):
        '''
        Get value from multi-line strings, read string line-by-line until expected_value is found in line string
        :param key: Actual result dictionary key
        :param expected_value: Expected value to find in multi-line string
        :return: expected_value if found, otherwise None
        '''
        # read test command to serial port
        out_bytes = ''
        out_buffer_bytes = self.bluetooth_serial_port.inWaiting()
        logging.debug("out_buffer_bytes:" + str(out_buffer_bytes))
        logging.debug("expected_value:" + expected_value)

        while out_buffer_bytes > 0 and not out_bytes == expected_value:
            instruction, author_name, song_name = self.bluetooth_serial_port.readline()
            if instruction != '':
                logging.info("instruction: "+instruction)
                out_bytes = instruction
            out_buffer_bytes = self.bluetooth_serial_port.inWaiting()

        if out_bytes == expected_value:
            self.dist[key] = out_bytes
        else:
            self.dist[key] = ''

        return self.dist[key]

    def get_value_from_mi(self, song_key, author_key, song_expected_value, author_expected_value):
        '''
        Get value from multi-line strings, read string line-by-line until expected_value is found in line string
        :param key: Actual result dictionary key
        :param expected_value: Expected value to find in multi-line string
        :return: expected_value if found, otherwise None
        '''
        # read test command to serial port
        out_bytes = ''
        instruction = ''
        author_name = ''
        song_name = ''
        out_buffer_bytes = self.bluetooth_serial_port.inWaiting()
        logging.debug("out_buffer_bytes:" + str(out_buffer_bytes))
        logging.debug("song_expected_value:" + song_expected_value + "  author_expected_value: " + author_expected_value)

        while out_buffer_bytes > 0 and not song_name == song_expected_value or not author_name == author_expected_value:
            instruction, author_name, song_name = self.bluetooth_serial_port.readline()
            if instruction == '':
                logging.info("song_name: " + song_name + "  author_name: " + author_name)
            out_buffer_bytes = self.bluetooth_serial_port.inWaiting()

        if song_name == song_expected_value:
            self.dist[song_key] = song_name
        else:
            self.dist[song_key] = ''
        if author_name == author_expected_value:
            self.dist[author_key] = author_name
        else:
            self.dist[author_key] = ''

        return self.dist[song_key], self.dist[author_key]
