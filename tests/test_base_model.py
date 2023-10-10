#!/usr/bin/python3
"""Tests the base model"""
import unittest
from datetime import datetime

BaseModel = __import__("models.base_model", fromlist="base_model").BaseModel


class BaseModelTestCase(unittest.TestCase):
    """Tests the base model"""

    def setUp(self):
        """Sets up the base model"""
        self.BaseModel = BaseModel()
        self.BaseModel2 = None

    def test_module_doc_is_not_empty(self):
        """The Module doc should be documented"""
        docs = __import__("models.base_model", fromlist="base_model").__doc__
        self.assertIsNotNone(docs)
        self.assertIsNot(len(docs), 0)

    def test_class_doc_is_not_empty(self):
        """The Class should be documented"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_all_methods_are_documented(self):
        """All class methods should be documented"""
        import inspect

        for name, member in inspect.getmembers(
            self.BaseModel.__class__,
            predicate=inspect.ismethod
        ):
            docs = member.__doc__
            print(type(docs))
            self.assertIsNotNone(docs)

    def test_base_model_is_a_class(self):
        """The baseModel should be a class"""
        self.assertIsInstance(self.BaseModel, BaseModel)

    def test_created_at(self):
        """The public class attribute (created_at) should be a date"""
        self.assertIsInstance(self.BaseModel.created_at, datetime)

    def test_updated_at(self):
        """The public class attribute (updated_at) should be a date"""
        self.assertIsInstance(self.BaseModel.updated_at, datetime)

    def test_to_dict(self):
        """The to_dict method should return a dict"""
        self.assertIsInstance(self.BaseModel.to_dict(), dict)

    def test_create_object_from_dict(self):
        """
        A new BaseModel should be created from the dictionary of another
        Base Model
        """
        self.BaseModel2 = BaseModel(**self.BaseModel.to_dict())
        self.assertIsInstance(self.BaseModel2, BaseModel)

    def test_create_object_from_dict(self):
        """
        A new BaseModel should be created from the dictionary of another
        Base Model
        """
        self.assertIsNot(self.BaseModel2, self.BaseModel)


if __name__ == "__main__":
    unittest.main()
