#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_base(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_neg_base(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    @unittest.expectedFailure
    def test_str(self):
        self.assertEqual(max_integer("hello"))

    @unittest.expectedFailure
    def test_float(self):
        self.assertEqual(max_integer([4.2, 9.8, 7.0]))

    @unittest.expectedFailure
    def test_empty(self):
        self.assertNone(max_integer())
