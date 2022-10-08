from .Error import fileError

def File(__file__: str, __PATH__) -> None:
    __LINES__ = []
    try:
        with open(
            file=__file__,
            mode="r",
            encoding="utf-8"
        ) as __FILE__:
            for COUNT, LINE in enumerate(__FILE__.readlines()):
                yield COUNT, LINE.removesuffix("\n")
    except FileNotFoundError:
        fileError("The input file is doesn't exist.")