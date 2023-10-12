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
    intro = "hbnb command line interpreter version 1.0.0 by Leo Emaxie"
    prompt = "(hbnb) "
    last_output = ""
    args = []
    class_id = ""
    class_name = ""
    passed = False
    classes = {
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
        line = rewrite(line.strip(), self.classes)
        self.args = line.split(" ")
        self.class_name = ""
        self.passed = False
        commands = {
            "all": 1,
            "create": 1,
            "count": 1,
            "destroy": 2,
            "show": 2,
            "update": 4
        }
        command = self.args[0]

        if command not in commands.keys():
            return line

        # Checks the number pf arguments given. [all] is peculiar because it
        # accepts 1 arguments or no argument.
        args_count = commands[command]
        if command == "all":
            args_count = len(self.args) - 1
            if args_count == 0:  # [all] doesn't have an argument, continue.
                self.passed = True
                return line
            if args_count > 1:
                print("** Too many arguments **")
                return line
        elif not has_correct_args(self.args, args_count):
            return line

        self.class_name = self.args[1]
        if self.class_name not in self.classes:
            print("** class doesn't exist **")
            return line

        if args_count > 1:
            self.class_id = "{}.{}".format(self.class_name, self.args[2])
            if self.class_id not in storage.all():
                print("** no instance found **")
                return line

        self.passed = True
        self.args.pop(0)
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

    def do_shell(self, line):
        """Run a previous command"""
        import os
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_create(self, line):
        """
        Usage: create [Model]
        Creates a new instance of a model, saves it to a JSON file and
        prints the id
        """
        if self.passed:
            instance = self.classes[self.class_name]()
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
            obj.__dict__.update({self.args[2]: self.args[3]})
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
