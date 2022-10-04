from os import system as cmd
import sys

from .Function import Module
from .Keywords import Any
from .Clear import GarbageCollection as GC


functions = {}

def method(func: callable):
    TEMP_functions.append(func.__name__) if func.__name__ not in TEMP_functions else None
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class Sys(Module):
    def __init__(self) -> None:
        super().__init__()
        self.argv = sys.argv

    @method
    def system(self, text) -> Any:
        return cmd(text)
    
    @method
    def python(self, text) -> Any:
        return exec(text)
    
    @method
    def execute(self, text) -> Any:
        return exec(text)

GarbageCollection()