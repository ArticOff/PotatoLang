from .Keywords import Any

def GarbageCollection(_global: dict) -> None:
    for variable in list(_global):
        if str(variable).startswith("TEMP_"):
            del _global[variable]

class variableHandler:
    def __init__(self, _globals: dict) -> None:
        self.globals = _globals
    
    def get(self, index: str) -> Any:
        return self.globals[index]
    
    def set(self, index: str, value: Any) -> None:
        self.globals[index] = value
        return