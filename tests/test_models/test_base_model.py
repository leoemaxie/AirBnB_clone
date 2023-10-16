#!/usr/bin/python3
"""Unittests for the BaseModel"""
import unittest
from test_models.base_test import BaseTestCase
from models.base_model import BaseModel


class BaseModelTestCase(BaseTestCase, unittest.TestCase):
    """Tests the BaseModel"""

    def setUp(self):
        """Sets up the models"""
        self.model = BaseModel
        self.Model1 = BaseModel()
        self.Model2 = BaseModel(**self.Model1.to_dict())
        self.docs = __import__(
            "models.base_model",
            fromlist="base_model"
        ).__doc__


if __name__ == "__main__":
    unittest.main()
