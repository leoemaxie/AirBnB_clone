#!/usr/bin/python3
"""Tests the base model"""
import unittest
from datetime import datetime

BaseModel = __import__("models.base_model", fromlist="base_model").BaseModel


class BaseModelTestCase(unittest.TestCase):
    """Tests the base model"""

    def setUp(self):
        """Sets up the base models"""
        self.BaseModel = BaseModel()
        self.BaseModel2 = BaseModel(**self.BaseModel.to_dict())

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
        """The public instance attribute (created_at) should be a date"""
        self.assertIsInstance(self.BaseModel.created_at, datetime)

    def test_updated_at(self):
        """The public instance attribute (updated_at) should be a date"""
        self.assertIsInstance(self.BaseModel.updated_at, datetime)

    def test_id(self):
        """The public instance attribute (id) should be a string"""
        self.assertIsInstance(self.BaseModel.id, str)

    def test_to_dict(self):
        """The to_dict method should return a dict"""
        self.assertIsInstance(self.BaseModel.to_dict(), dict)

    def test_updated_at_in_dictionary(self):
        """
        The public instance attribute (updated_at) should be serialized to a
        string when to_dict() is called
        """
        dictionary = self.BaseModel2.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)

    def test_created_at_in_dictionary(self):
        """
        The public instance attribute (created_at) should be serialized to a
        string when to_dict() is called
        """
        dictionary = self.BaseModel2.to_dict()
        self.assertIsInstance(dictionary["created_at"], str)

    def test_save(self):
        """
        The public instance attribute (updated_at) should change when save() is
        called.
        """
        last_updated = self.BaseModel.updated_at
        self.BaseModel.save()
        updated_at = self.BaseModel.updated_at
        self.assertNotEqual(last_updated, updated_at)

    def test_id_of_instances_are_not_equal(self):
        """The id of two instances of a class should not be equal"""
        self.assertNotEqual(BaseModel().id, self.BaseModel2.id)

    def test_id_of_to_dict_instances_are_equal(self):
        """
        The id of a BaseModel created from the dictionary of another
        BaseModel should be equal
        """
        self.assertEqual(self.BaseModel.id, self.BaseModel2.id)

    def test_create_object_from_dict(self):
        """
        A new BaseModel should be created from the dictionary of another
        Base Model
        """
        self.assertIsInstance(self.BaseModel2, BaseModel)

    def test_base_model_created_from_dict_is_not_none(self):
        """
        A new BaseModel created from the dictionary of another
        Base Model should not be None
        """
        self.assertIsNotNone(self.BaseModel2)

    def test_object_created_from_dict_are_not_the_same(self):
        """
        A new BaseModel created from the dictionary of another
        Base Model should not be the same
        """
        self.assertIsNot(self.BaseModel2, self.BaseModel)

    def test_clsss_attribute_not_in_dict(self):
        """
        __class__ attribute should not be an attribute of a class
        """
        self.assertNotIn("__class__", self.BaseModel2.__dict__)

    def test_clsss_attribute_in_to_dict(self):
        """
        __class__ attribute should be in the dictionary returned by to_dict
        """
        self.assertIn("__class__", self.BaseModel2.to_dict())

    def test_to_string(self):
        """
        The output string when a BaseModel is converted to a string should
        follow this format: [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[{}] ({}) {}".format(
            self.BaseModel.__class__.__name__,
            self.BaseModel.id,
            self.BaseModel.__dict__
        )
        self.assertEqual(string, str(self.BaseModel))


if __name__ == "__main__":
    unittest.main()
