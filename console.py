#!/usr/bin/python3
"""Console Module: Contains the entry point of the command interpreter"""
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command Line Interpreter to manipulate the resources and data of the
    website
    """
    prompt = "(hbnb) "
    last_output = ""

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
        args = line.split(" ")
        if has_correct_args(args, 1):
            print(line[0])

    def do_show(self, line):
        """
        Usage: show [Model] [ID]
        Prints the string representation of an instance based on the
        class name and id
        """
        args = line.split(" ")
        if has_correct_args(line, 2):
            objs = storage.all()
            obj_id = "{}.{}".format(args[0], args[1])
            del objs[obj_id]
            storage.reload()

    def do_all(self, line):
        """
        Usage: all [Model]
        Prints all string representation of all instances based or no
        on the class name.
        If Model is not provided, all instances are read and displayed from a
        JSON file
        """
        args = line.split(" ")
        if has_correct_args(line, 2):
            objs = storage.all()
            obj_id = "{}.{}".format(args[0], args[1])
            del objs[obj_id]
            storage.reload()

    def do_update(self, line):
        """
        Usage: update [Model] [ID] [AttributeName] [AttributeValue]
        Updates an instance based on the class name and id by adding or
        updating attribute and saves the change into a JSON file.
        """
        args = line.split(" ")
        if has_correct_args(line, 4):
            objs = storage.all()
            obj_id = "{}.{}".format(args[0], args[1])
            del objs[obj_id]
            storage.reload()

    def do_destroy(self, line):
        """
        Usage: destroy [Model] [ID]
        Deletes an instance based on the class name and id and saves the change
        into a JSON file
        """
        args = line.split(" ")
        if has_correct_args(line, 2):
            objs = storage.all()
            obj_id = "{}.{}".format(args[0], args[1])
            del objs[obj_id]
            storage.reload()


def has_correct_args(args, length):
    """
    Helper function to check if a command has the right number of arguments
    Args:
        args: list - commandline arguments passed to a command
        length: int - the appropriate number of arguments a command should have
    """
    args_len = len(args)

    if args_len == length:
        return True
    elif args_len > length:
        print("** Too many arguments **")
    elif args_len == 1:
        print("** class name missing **")
    elif args_len == 2:
        print("** instance id missing **")
    else:
        print("** Too few arguments **")
    return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
