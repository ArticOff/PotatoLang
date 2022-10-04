import sys

from .Error import fatalError

def File(__file__: str, __PATH__) -> None:
    __LINES__ = []
    try:
        with open(
            file=__file__,
            mode="r",
            encoding="utf-8"
        ) as __FILE__:
            __CONTENT__ = __FILE__.readlines()
            for __LINE__ in __CONTENT__:
                __LINES__.append(str(__LINE__).removesuffix("\n"))
            for COUNT, LINE in enumerate(__LINES__):
                yield COUNT, LINE
    except FileNotFoundError:
        fatalError("The input file is doesn't exist.")