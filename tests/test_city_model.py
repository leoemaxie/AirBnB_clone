#!/usr/bin/python3
"""Unittests for the City Model"""
import unittest
from tests.base_test import BaseTestCase
from models.city import City


class BaseModelTestCase(BaseTestCase, unittest.TestCase):
    """Tests the City Model"""

    def setUp(self):
        """Sets up the model"""
        self.model = City
        self.Model1 = City()
        self.Model2 = City(**self.Model1.to_dict())
        self.docs = __import__(
            "models.city",
            fromlist="city"
        ).__doc__


if __name__ == "__main__":
    unittest.main()
