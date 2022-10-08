from os import system as cmd
import sys, math, random

from .Function import Module
from .Keywords import Any
from .Error import mathError

class Sys(Module):
    def __init__(self) -> None:
        super().__init__([i for i in self.__dir__() if not "__" in i and i not in self.__dict__ and not i == "name"])
        self.argv = sys.argv
    
    def system(self, text) -> Any:
        return cmd(text)
    
    def python(self, text) -> Any:
        return exec(text)
    
    def execute(self, text) -> Any:
        return exec(text)

class Math(Module):
    def __init__(self) -> None:
        super().__init__([i for i in self.__dir__() if not "__" in i and i not in self.__dict__ and not i == "name"])
        self.pi = math.pi

    def cos(self, number: float) -> float:
        return math.cos(number)
    
    def sin(self, number: float) -> float:
        return math.sin(number)
    
    def tan(self, number: float) -> float:
        return math.tan(number)
    
    def acos(self, number: float) -> float:
        try:
            return math.acos(number)
        except ValueError as TEMP_e:
            mathError(TEMP_e)

    def asin(self, number: float) -> float:
        try:
            return math.asin(number)
        except ValueError as TEMP_e:
            mathError(TEMP_e)

    def atan(self, number: float) -> float:
        return math.atan(number)
    
    def sqrt(self, number: float) -> float:
        return math.sqrt(number)
    
    def degrees(self, number: float) -> float:
        return math.degrees(number)
    
    def radians(self, number: float) -> float:
        return math.radians(number)

class Random(Module):
    def __init__(self) -> None:
        super().__init__([i for i in self.__dir__() if not "__" in i and i not in self.__dict__ and not i == "name"])
    
    def rand(_x: int, _y: int) -> int:
        return random.randint(_x, _y)