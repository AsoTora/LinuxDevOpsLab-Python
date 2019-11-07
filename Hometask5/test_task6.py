#! /usr/bin/env python3

import task6
import unittest


class TestTasks(unittest.TestCase):
    ''' Unit tests for any task from Homework 2.'''

    def test_task6(self):
        self.assertEqual(task6.decode('L7MO'), 'test')
        self.assertEqual(task6.decode('576J9FLF'), 'decoding')
        self.assertEqual(task6.decode('97FGK63N0MF'), 'hello world')


if __name__ == '__main__':
    unittest.main()
