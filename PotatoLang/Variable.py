from .Keywords import Any

class Init:
    def __init__(self, _globals: dict) -> None:
        self.globals = dict(_globals)
    
    def set(self, index: str, value: Any) -> None:
        self.globals[index] = value
        return
    
    def get(self, index: str) -> Any:
        return self.globals[index]