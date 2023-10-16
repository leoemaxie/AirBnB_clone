#!/usr/bin/python3
"""Unittests for the State Model"""
import unittest
from test_models.base_test import BaseTestCase
from models.state import State


class StateTestCase(BaseTestCase, unittest.TestCase):
    """Tests the State Model"""

    def setUp(self):
        """Sets up the model"""
        self.model = State
        self.Model1 = State()
        self.Model2 = State(**self.Model1.to_dict())
        self.docs = __import__(
            "models.state",
            fromlist="state"
        ).__doc__


if __name__ == "__main__":
    unittest.main()
