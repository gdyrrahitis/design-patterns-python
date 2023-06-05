"""Classic singleton"""
class Database:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def save(self):
        print("saving to database")

"""Borg singleton"""
from abc import ABC, abstractmethod
class FileSystem(ABC):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(FileSystem, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    
    @abstractmethod
    def list_directory_contents(self, directory):
        pass

class WindowsExplorer(FileSystem):
    def list_directory_contents(self, directory):
        print(f"Listing contents in Windows directory {directory}")

class Finder(FileSystem):
    def list_directory_contents(self, directory):
        print(f"Listing contents in MacOS directory {directory}")