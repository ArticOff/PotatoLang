functions = []
modules = []

def function(func: callable):
    functions.append(func.__name__) if func.__name__ not in functions else None
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class Module(object):
    def __new__(cls, _None = None):
        obj = object.__new__(cls)
        cls.name = cls.__name__
        modules.append(cls.name)
        return obj

    def __init__(self) -> None:
        self.dataName = self.__class__.name