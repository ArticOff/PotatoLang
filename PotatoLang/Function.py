from .Variable import Init
from .Keywords import Any

functions = []
modules = {}

def function(func: callable):
    functions.append(func.__name__) if func.__name__ not in functions else None
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class Module(object):
    def __new__(cls, _None = None):
        obj = object.__new__(cls)
        cls.name = cls.__name__
        return obj

    def __init__(self, funcs) -> None:
        self.dataName = self.__class__.name
        modules[self.dataName] = funcs

class functionHandler:
    def __init__(self, functions: list, Function: dict, VariableHandler: Init, _globals: dict) -> None:
        self.functions = functions
        self.Function = Function
        self.variable = VariableHandler
        self.globals = _globals
        self.name = None

    def create(self, name: str, args: list[str]) -> None:
        if args[0] == '':
            del args[0]
        self.name = name
        self.args = args
        self.code = []
        self.Function[self.name] = {}
        self.Function[self.name]["args"] = self.args
        self.Function[self.name]["code"] = self.code
        self.variable.set("CODE_isFunction", True)
        return
    
    def end(self) -> None:
        self.variable.set("CODE_isFunction", False)
        self.variable.set("functions", [*self.functions, *self.name])
        self.functions = [*self.functions, *self.name]
        return
    
    def getCode(self, line: str) -> None:
        if line.startswith("{"):
            return
        elif line.startswith("}"):
            self.end()
        else:
            (self.Function[self.name]["code"]).append(line.removeprefix("    "))
            return
    
    def exeCode(self, index: str) -> Any:
        TEMP_code = self.Function[index]["code"]
        TEMP_run = True
        while TEMP_run:
            for TEMP_line in TEMP_code:
                for TEMP_i in list(self.Function):
                    if TEMP_i == (str(TEMP_line).split("("))[0]:
                        TEMP_code = self.Function[TEMP_i]["code"]
                        break
                else:
                    exec(TEMP_line, self.globals, {})
                    TEMP_run = False
                    break