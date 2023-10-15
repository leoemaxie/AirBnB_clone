#!/usr/bin/python3
"""FileStorage Test: Tests to validate the reliability of the engine"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTestCase(unittest.TestCase):
    """Tests the FileStorage engine"""

    def setUp(self):
        """Sets up the module docs"""
        self.Model = BaseModel()
        self.class_id = "BaseModel.{}".format(self.Model.id)
        self.docs = __import__(
            "models.engine.file_storage",
            fromlist="file_storage"
        ).__doc__
        self.storage = FileStorage()
        self.storage.reload()

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
        self.assertIsNotNone(FileStorage.__doc__)

    def test_documented_methods(self):
        """All class methods should be documented"""
        import inspect

        for name, member in inspect.getmembers(
            FileStorage,
            predicate=inspect.ismethod
        ):
            docs = member.__doc__
            self.assertIsNotNone(docs)
            self.assertGreater(len(docs), 20)

    def test_new(self):
        """The new method should save a new model to a file"""
        self.storage.new(self.Model)
        self.assertIn(self.class_id, self.storage.all())

    def test_reload(self):
        """Reloading the storage should refresh all the models created"""
        self.storage.reload()
        self.assertIn(self.class_id, self.storage.all())

    def test_all(self):
        """The all method should return a dict"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_json_objects(self):
        """Objects returned from a JSON file should be a valid class"""
        self.assertEqual(self.storage.all().get(self.class_id), self.Model)

    def test_valid_dict(self):
        """JSON file should have the same attributes with a saved Model"""
        obj = self.storage.all().get(self.class_id)
        self.assertEqual(obj.to_dict(), self.Model.to_dict())

    def test_file_error(self):
        """
        Save method should not raise an exception when a file doesn't exists
        """
        self.tearDown()
        self.storage.reload()


if __name__ == "__main__":
    unittest.main()
