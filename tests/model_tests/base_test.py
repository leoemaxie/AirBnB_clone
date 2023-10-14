#!/usr/bin/python3
"""Base Test: The base test case for all models"""
from datetime import datetime
from models.base_model import BaseModel


class BaseTestCase(object):
    """Tests all common attributes across all models"""

    def tearDown(self):
        """Removes the json file(s) after test execution"""
        import os
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_empty_module_doc(self):
        """The Module doc should be documented i.e it shouldn't be empty"""
        self.assertIsNotNone(self.docs)

    def test_short_module_doc(self):
        """
        The Module doc should be properly documented.
        It should be precise and detailed
        """
        self.assertGreater(len(self.docs), 20)

    def test_empty_class_doc(self):
        """The Class should be documented"""
        self.assertIsNotNone(self.Model1.__doc__)

    def test_documented_methods(self):
        """All class methods should be documented"""
        import inspect

        for name, member in inspect.getmembers(
            self.Model1,
            predicate=inspect.ismethod
        ):
            docs = member.__doc__
            self.assertIsNotNone(docs)
            self.assertGreater(len(docs), 20)

    def test_model_is_a_class(self):
        """The Model should be a class"""
        self.assertIsInstance(self.Model1, self.model)

    def test_model_is_subclass(self):
        """All models should be a subclass of BaseModel"""
        self.assertTrue(issubclass(self.model, BaseModel))

    def test_created_at(self):
        """The public instance attribute (created_at) should be a date"""
        self.assertIsInstance(self.Model1.created_at, datetime)

    def test_updated_at(self):
        """The public instance attribute (updated_at) should be a date"""
        self.assertIsInstance(self.Model2.updated_at, datetime)

    def test_id(self):
        """The public instance attribute (id) should be a string"""
        self.assertIsInstance(self.Model1.id, str)

    def test_to_dict(self):
        """The to_dict method should return a dict"""
        self.assertIsInstance(self.Model1.to_dict(), dict)

    def test_updated_at_in_dictionary(self):
        """
        The public instance attribute (updated_at) should be serialized to a
        string when to_dict() is called
        """
        dictionary = self.Model2.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)

    def test_created_at_in_dictionary(self):
        """
        The public instance attribute (created_at) should be serialized to a
        string when to_dict() is called
        """
        dictionary = self.Model2.to_dict()
        self.assertIsInstance(dictionary["created_at"], str)

    def test_save(self):
        """
        The public instance attribute (updated_at) should change when save() is
        called.
        """
        last_updated = self.Model1.updated_at
        self.Model1.save()
        updated_at = self.Model1.updated_at
        self.assertNotEqual(last_updated, updated_at)

    def test_unique_id(self):
        """The id of two instances of a class should not be the same"""
        self.assertNotEqual(self.Model1.id, self.model().id)

    def test_id_of_to_dict_instances_are_equal(self):
        """
        The id of a model created from the dictionary of another
        model should be equal.
        """
        self.assertEqual(self.Model1.id, self.Model2.id)

    def test_create_object_from_dict(self):
        """
        A new model should be created from the dictionary of another
        model
        """
        self.assertIsInstance(self.Model2, self.model)

    def test_model_created_from_dict_is_not_none(self):
        """
        A new model created from the dictionary of another
        model should not be None
        """
        self.assertIsNotNone(self.Model2)

    def test_object_created_from_dict_are_not_the_same(self):
        """
        A new model created from the dictionary of another
        model should not be the same.
        """
        self.assertIsNot(self.Model1, self.Model2)

    def test_class_attribute_not_in_dict(self):
        """
        __class__ attribute should not be an attribute of a class
        """
        self.assertNotIn("__class__", self.Model2.__dict__)

    def test_class_attribute_in_to_dict(self):
        """
        __class__ attribute should be in the dictionary returned by to_dict
        """
        self.assertIn("__class__", self.Model1.to_dict())

    def test_to_string(self):
        """
        The output string when a Model is converted to a string should
        follow this format: [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[{}] ({}) {}".format(
            self.Model1.__class__.__name__,
            self.Model1.id,
            self.Model1.__dict__
        )
        self.assertEqual(string, str(self.Model1))
