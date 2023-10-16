#!/usr/bin/python3
"""Unittests for the Amenity Model"""
import unittest
from test_models.base_test import BaseTestCase
from models.amenity import Amenity


class AmenityTestCase(BaseTestCase, unittest.TestCase):
    """Tests the Amenity Model"""

    def setUp(self):
        """Sets up the model"""
        self.model = Amenity
        self.Model1 = Amenity()
        self.Model2 = Amenity(**self.Model1.to_dict())
        self.docs = __import__(
            "models.amenity",
            fromlist="amenity"
        ).__doc__


if __name__ == "__main__":
    unittest.main()
