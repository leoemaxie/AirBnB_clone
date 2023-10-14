#!/usr/bin/python3
"""Console Module: Contains the entry point of the command interpreter"""
import cmd

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from utils import rewrite, has_correct_args


class HBNBCommand(cmd.Cmd):
    """
    Command Line Interpreter to manipulate the resources and data of the
    website
    """
    intro = "hbnb commandline interpreter version 1.0.0 by Leo Emaxie"
    prompt = "(hbnb) "
    passed = False
    attr = ""
    value = ""
    class_id = ""
    class_name = ""
    __classes = {
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
        "BaseModel": BaseModel
    }

    def precmd(self, line):
        """Splits the line into arguments before execution"""
        line = rewrite(line.strip(), self.__classes)
        args = line.split(" ")
        command = args[0]
        commands = {
            "all": 1,
            "create": 1,
            "count": 1,
            "destroy": 2,
            "show": 2,
            "update": 4
        }
        self.attr = ""
        self.value = ""
        self.class_id = ""
        self.class_name = ""
        self.passed = False

        if command not in commands.keys():
            return line
        if not has_correct_args(args, commands.get(command, -1)):
            return line

        try:
            self.class_name = args[1]
            if self.class_name not in self.__classes:
                print("** class doesn't exist **")
                return line

            self.class_id = "{}.{}".format(self.class_name, args[2])
            if self.class_id not in storage.all():
                print("** no instance found **")
                return line

            self.attr = args[3]
            self.value = args[4]
        except IndexError:
            pass

        self.passed = True
        return line

    def emptyline(self):
        """Handles empty lines"""

    def do_EOF(self, line):
        """Handles the End of File Condition"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """
        Usage: create [Model]
        Creates a new instance of a model, saves it to a JSON file and
        prints the id
        """
        if self.passed:
            instance = self.__classes[self.class_name]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Usage: show [Model] [ID]
        Prints the string representation of an instance based on the
        class name and id
        """
        if self.passed:
            objs = storage.all()
            print(objs[self.class_id])

    def do_all(self, line):
        """
        Usage: all [Model]
        Prints all string representation of all instances based or no
        on the class name.
        If Model is not provided, all instances are read and displayed from a
        JSON file
        """
        if self.passed:
            objs = []
            for key, value in storage.all().items():
                if self.class_name:
                    if self.class_name == value.__class__.__name__:
                        objs.append(str(value))
                else:
                    objs.append(str(value))
            print(objs)

    def do_count(self, line):
        """
        Usage: count [Model]
        Counts all the instances of a class.
        """
        if self.passed:
            count = 0
            for key, value in storage.all().items():
                if self.class_name == value.__class__.__name__:
                    count += 1
            print(count)

    def do_update(self, line):
        """
        Usage: update [Model] [ID] [AttributeName] [AttributeValue]
        Updates an instance based on the class name and id by adding or
        updating attribute and saves the change into a JSON file.
        """
        if self.passed:
            objs = storage.all()
            obj = objs[self.class_id]
            obj.__dict__.update({self.attr: self.value})
            storage.save()

    def do_destroy(self, line):
        """
        Usage: destroy [Model] [ID]
        Deletes an instance based on the class name and id and saves the change
        into a JSON file
        """
        if self.passed:
            objs = storage.all()
            del objs[self.class_id]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
