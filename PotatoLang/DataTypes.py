from .Keywords import Any
from .Error import syntaxError

class DataType(object):
    def __new__(cls, _None = None):
        obj = object.__new__(cls)
        cls.name = cls.__name__
        return obj
    
    def __init__(self) -> None:
        self.dataName = self.__class__.name

class Boolean(DataType):
    def __init__(self, content) -> None:
        super().__init__()
        self.content = bool(content)
    
    def __str__(self) -> str:
        return str(self.content)

    def __type__(self) -> str:
        return self.dataName
    
    def __bool__(self) -> bool:
        return self.content

class String(DataType):
    def __init__(self, content) -> None:
        super().__init__()
        self.content = str(content)

    def __str__(self) -> str:
        return str(self.content)
    
    def __type__(self) -> str:
        return self.dataName

    def split(self, letter) -> list[str]:
        return self.content.split(letter)
    
    def isStartingWith(self, letter) -> Boolean:
        return Boolean(self.content.startswith(letter))
    
    def isEndingWith(self, letter) -> Boolean:
        return Boolean(self.content.endswith(letter))
    
class Number(DataType):
    def __init__(self, content) -> None:
        super().__init__()
        self.content = int(content) if float(content).is_integer() else float(content)
    
    def __str__(self) -> str:
        return str(self.content)
    
    def __type__(self) -> str:
        return self.dataName
    
    def __int__(self) -> int:
        return self.content

    def isFloat(self) -> Boolean:
        return Boolean(not float(self.content).is_integer())
    
    def isInteger(self) -> Boolean:
        return Boolean(float(self.content).is_integer())

class List(DataType):
    def __init__(self, content) -> None:
        super().__init__()
        self.content = list(content)
    
    def __str__(self) -> str:
        return str(self.content)

    def __type__(self) -> str:
        return self.dataName
    
    def add(self, value: Any) -> None:
        self.content.append(value)
    
    def removeByIndex(self, index: Number) -> None:
        del self.content[(index.__int__() - 1)]
    
    def removeByValue(self, value: Any):
        self.content.remove(value)
    
    def index(self, index: Number) -> Any:
        if Boolean(index.isFloat()).__bool__():
            syntaxError("List indice must be entire number.")
        elif len(self.content) < index.__int__():
            syntaxError("List index out of range.")
        else:
            return self.content[(index.__int__() - 1)]