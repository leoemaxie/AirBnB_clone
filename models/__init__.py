#!/usr/bin/python3
"""Model Package: Model package that exposes functionality to create, store,
uodate and manipulate data used in this website application.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
