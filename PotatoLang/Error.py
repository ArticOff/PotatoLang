import sys, os

from .Color import __color__
from .Keywords import NoReturn

# __errorType__ is for make an error
class __errorType__(object):
    """
    __errorType__ is for make an error

    example:
    class fatalError(__errorType__): ...

    fatalError("There's no input file")
    """
    def __new__(cls, _None = None):
        obj = object.__new__(cls)
        cls.name = cls.__name__
        return obj
    
    def __init__(self, message: str) -> None:
        try:
            file = sys.argv[2]
            try:
                open(file, mode="r", encoding="utf-8")
                __PATH__ = f"{os.getcwd()}\{file}"
                from compiler import __lineNumber__ as LN
                __lineNumber__ = LN()
            except FileNotFoundError:
                __PATH__ = "COMMAND PROMPT"
                __lineNumber__ = None
        except IndexError:
            __PATH__ = "COMMAND PROMPT"
            __lineNumber__ = None
        __error__(self.__class__.name, message, __PATH__, __lineNumber__)


# This function is for print the error in the console and stop the program
# DON'T USE THIS FUNCTION !
def __error__(__error: str, message: str, __fileName: str, __lineNumber: int = 0) -> NoReturn:
    print(f"{__color__.RED}{__error}: {message}{__color__.GRAY}\n    at \"{__fileName}\", line {__lineNumber}{__color__.STOP}")
    sys.exit()

# Errors...
class fatalError(__errorType__): ...
class syntaxError(__errorType__): ...
class nameError(__errorType__): ...
class error(__errorType__): ...
class mathError(__errorType__): ...
class returnError(__errorType__): ...
class fileError(__errorType__): ...
class moduleError(__errorType__): ...
class optionError(__errorType__): ...