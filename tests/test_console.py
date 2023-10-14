#!/usr/bin/python3
"""Console Test: The test case for hbnb commandline interpreter"""
import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from console import HBNBCommand
from models import storage


class ConsoleTestCase(unittest.TestCase):
    """Tests the console"""

    def setUp(self):
        """Sets up the module docs"""
        self.docs = __import__("console", fromlist="console").__doc__
        self.objects = storage.all()
        self.tearDown()

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
        It should be precise and detailed.
        """
        self.assertGreater(len(self.docs), 20)

    def test_empty_class_doc(self):
        """The Class should be documented"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_documented_methods(self):
        """All class methods should be documented"""
        import inspect

        for name, member in inspect.getmembers(
            HBNBCommand,
            predicate=inspect.ismethod
        ):
            docs = member.__doc__
            self.assertIsNotNone(docs)
