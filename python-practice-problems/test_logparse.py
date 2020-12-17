#!/usr/bin/env python3

import unittest
from logparse import parse_logs


class LogparseTestCase(unittest.TestCase):

    def test_error_timestamps_list(self):
        result = ['Jul 11 16:11:54:661000', 'Jul 11 16:11:56:067000']
        self.assertListEqual(parse_logs('test.log')[1], result)

    def test_runtime(self):
        result = 6.305999999999999
        self.assertEqual(parse_logs('test.log')[0], result)


if __name__ == '__main__':
    unittest.main()
