#!/usr/bin/python3
"""Utils: Helper function to manipulate the commandline"""


def rewrite(line, classes):
    """
    Helper function to rewrite the commandline if it begins with a
    supported class.
    Example: User.show(id) transforms to show [User] [id]
    Args:
        line: str - The line to execute.
        classes: list<class> - A list of suppprted classes.
    """
    import re
    if not re.fullmatch(r"^[A-Z][a-z]+([A-Z][a-z]+)?\.[a-z]+\([^)]*\)$", line):
        return line

    args = re.split(r"[(.,\")\']", line, maxsplit=3)
    args = [arg for arg in args if arg]

    if args[0] not in classes:
        return line

    args[0], args[1] = args[1], args[0]
    return " ".join(args)


def has_correct_args(args, length):
    """
    Helper function to check if a command has the right number of arguments
    Args:
        args: list - commandline arguments passed to a command
        length: int - the appropriate number of arguments a command should have
    """
    args_count = len(args) - 1

    if args_count == length:
        return True
    elif args_count > length:
        print("** Too many arguments **")
    elif args_count == 0:
        print("** class name missing **")
    elif args_count == 1:
        print("** instance id missing **")
    elif args_count == 2:
        print("** attribute missing **")
    elif args_count == 3:
        print("** value missing **")
    else:
        print("** No argument passed **")
    return False
