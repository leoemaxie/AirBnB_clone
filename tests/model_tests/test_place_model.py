#!/usr/bin/python3
"""Unittests for the Place Model"""
import unittest
from model_tests.base_test import BaseTestCase
from models.place import Place


class PlaceTestCase(BaseTestCase, unittest.TestCase):
    """Tests the Place Model"""

    def setUp(self):
        """Sets up the model"""
        self.model = Place
        self.Model1 = Place()
        self.Model2 = Place(**self.Model1.to_dict())
        self.docs = __import__(
            "models.place",
            fromlist="place"
        ).__doc__


if __name__ == "__main__":
    unittest.main()
