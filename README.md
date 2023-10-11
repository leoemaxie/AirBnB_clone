# AirBnB_clone
AirBnB fullstack website clone.

## Table of Content
- [Overview](#overview)
  - [The Console](#the-console)
    - [Models](#models)
    - [Commands](#commands)
- [Testing](#testing)
- [License](#license)
- [Authors](#authors)

## Overview
### The Console 
The console is a commandline interpreter that manipulates the resources and data of the website.

#### Models 
The console manipulates the following data:
* User
* Amenity
* Place
* City
* State
* Review

#### Commands 
The console accepts the following commands:
* **all** -> `all [Model]`: Prints all string representation of all instances based on the class name.
If Model is not provided, all instances are read and displayed from a JSON file.
* **create** -> `create [Model]`: Creates a new instance of a model, saves it to a JSON file
* **destroy** -> `destroy [Model] [ID]`: Deletes an instance based on the class name and id and saves the change into a JSON file
* **help** -> `help [command]`: Displays a short description of the usage of a command.
* **quit** -> Quit command to exit the program
* **show** -> `show [Model] [ID]`: Prints the string representation of an instance based on the class name and id.
* **update** -> `update [Model] [ID] [AttributeName] [AttributeValue]`: Updates an instance based on the class name and id by adding or updating attribute and saves the change into a JSON file.

## Testing 
Unittests can be carried out at the root of the project by runnung:
```bash
python3 -m unittest discover tests
```

## License 
This project uses the MIT License as found [here](/LICENSE)

## Authors 
Written by [Leo Emaxie](https://github.com/leoemaxie)
