#!/usr/bin/python3
"""Console Test: The test case for hbnb commandline interpreter"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class ConsoleTestCase(unittest.TestCase):
    """Tests the console"""

    def setUp(self):
        """Sets up the module docs"""
        self.docs = __import__("console", fromlist="console").__doc__
        self.no_classname = "** class name missing **"
        self.no_class = "** class doesn't exist **"
        self.no_instance = "** no instance found **"

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

    def test_prompt(self):
        """The prompt should be (hbnb)"""
        self.assertIsNotNone(HBNBCommand.prompt, "(hbnb) ")

    def test_all_help(self):
        """The [all] command should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on all")
            self.assertGreater(len(output), 20)

    def test_count_help(self):
        """The [count] command should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on count")
            self.assertGreater(len(output), 20)

    def test_create_help(self):
        """The [create] command should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on create")
            self.assertGreater(len(output), 20)

    def test_destroy_help(self):
        """The [destroy] command should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on destroy")
            self.assertGreater(len(output), 20)

    def test_show_help(self):
        """The [show] command should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on show")
            self.assertGreater(len(output), 20)

    def test_update_help(self):
        """The [update] command should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on update")
            self.assertGreater(len(output), 20)

    def test_quit_help(self):
        """The [quit] command should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on quit")
            self.assertGreater(len(output), 20)

    def test_EOF_help(self):
        """EOF should be properly documented"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue().strip()
            self.assertNotEqual(output,  "*** No help on EOF")
            self.assertGreater(len(output), 20)

    def test_create_cmd_no_classname(self):
        """An error message must be displayed if class name is not provided"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().precmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, self.no_classname)

    def test_destroy_cmd_no_classname(self):
        """An error message must be displayed if class name is not provided"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().precmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, self.no_classname)

    def test_count_cmd_no_classname(self):
        """An error message must be displayed if class name is not provided"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().precmd("count")
            output = f.getvalue().strip()
            self.assertEqual(output, self.no_classname)

    def test_show_cmd_no_classname(self):
        """An error message must be displayed if class name is not provided"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().precmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, self.no_classname)

    def test_update_cmd_no_classname(self):
        """An error message must be displayed if class name is not provided"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().precmd("update")
            output = f.getvalue().strip()
            self.assertEqual(output, self.no_classname)

    def test_create_cmd_invalid_class(self):
        """An error message must be displayed if a class is unsupported"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().precmd("create Restaurant")
            output = f.getvalue().strip()
            self.assertEqual(output, self.no_class)

    def test_update_cmd_no_classname(self):
        """An error message must be displayed if class name is not provided"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().precmd("update")
            output = f.getvalue().strip()
            self.assertEqual(output, self.no_classname)


if __name__ == "__main__":
    unittest.main()
