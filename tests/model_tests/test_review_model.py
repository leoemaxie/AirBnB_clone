#!/usr/bin/python3
"""Unittests for the Review Model"""
import unittest
from model_tests.base_test import BaseTestCase
from models.review import Review


class ReviewTestCase(BaseTestCase, unittest.TestCase):
    """Tests the Review Model"""

    def setUp(self):
        """Sets up the model"""
        self.model = Review
        self.Model1 = Review()
        self.Model2 = Review(**self.Model1.to_dict())
        self.docs = __import__(
            "models.user",
            fromlist="user"
        ).__doc__


if __name__ == "__main__":
    unittest.main()
