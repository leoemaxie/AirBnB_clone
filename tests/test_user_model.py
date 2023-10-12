#!/usr/bin/python3
"""Unittests for the User Model"""
import unittest
from tests.base_test import BaseTestCase
from models.user import User


class BaseModelTestCase(BaseTestCase, unittest.TestCase):
    """Tests the User Model"""

    def setUp(self):
        """Sets up the model"""
        self.model = User
        self.Model1 = User()
        self.Model2 = User(**self.Model1.to_dict())
        self.docs = __import__(
            "models.user",
            fromlist="user"
        ).__doc__


if __name__ == "__main__":
    unittest.main()
