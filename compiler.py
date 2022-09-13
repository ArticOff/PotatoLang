import sys, os

class __color__:
    VIOLET = "\033[95m"
    CYAN = "\033[96m"
    DARK_CYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    WHITE = "\033[37m"
    BLACK = "\033[30m"
    GRAY = "\033[38;2;88;88;88m"
    MAGENTA = "\033[35m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    NORMAL = "\033[22m"
    UNDERLINED = "\033[4m"
    STOP = "\033[0m"

class __method__:
    def __init__(self, name: str, callback: callable) -> None:
        self.funcname = name
        self.callback = callback
    
    def __str__(self) -> str:
        return f"{self.funcname}("

    def __call__(self, *args):
        return exec(f"self.callback{args}")

class __errorType__:
    def __init__(self, errorName: str):
        self.name = errorName
    
    def __call__(self, errorMessage: str):
        self.message = errorMessage
        return self

def __error__(__error: __errorType__, __fileName: str, __lineNumber: int) -> None:
    print(f"{__color__.RED}{__error.name}: {__error.message}.{__color__.GRAY}\n    at \"{__fileName}\", line {__lineNumber}{__color__.STOP}")
    sys.exit()

def __getArgs__(line: str, method: str) -> str:
    tempData = []
    tempValues = []
    tempSplit = None
    line = line.replace(str(method), "").removeprefix("(").removesuffix(")").removesuffix(";").split(",")
    for i in line:
        if i in list(__VARIABLES__):
            for count, value in enumerate(line):
                if value == i:
                    line[count] = f"\"{__VARIABLES__[i]}\""
    for i in line:
        if i in list(__VARIABLES__):
            tempData.append(__VARIABLES__[i])
        else:
            tempData.append(i)
    for _item in tempData:
        tempSplit = str(_item).split()
        for i in tempSplit:
            if "[" and "]" in i:
                tempValues.append(i.replace('"', "").removeprefix("[").removesuffix("]").replace(",", ""))
    for i in tempValues:
        if i in list(__VARIABLES__):
            string = ("".join(tempData)).replace(f"[{i}]", __VARIABLES__[i])
            tempData[0] = string

    return ", ".join(tempData)

def __printf__(text, end="\n"):
    return print(text, end=end)

def __inputf__(text, end=""):
    return input(f"{text}{end}")

def __calc__(calculation):
    return eval(calculation, {}, {})

__VARIABLES__ = {}
__LINES__ = []
__KEYWORDS__ = ["close", "is", "and", "or", "in", "for", "build", "declare", "if"]

fatalError = __errorType__("fatalError")
syntaxError = __errorType__("syntaxError")

printf = __method__("printf", __printf__)
inputf = __method__("inputf", __inputf__)
calc = __method__("calc", __calc__)

def __getLineByNumber__(number: int) -> str:
    return __LINES__[number]

def __getLineByWord__(word: str) -> str:
    for i, v in enumerate(__LINES__):
        if word in v:
            return __LINES__[i]
        i += 1

try:
    with open(file=sys.argv[1], mode="r", encoding="utf-8") as __FILE__:
        __CONTENT__ = __FILE__.readlines()
        __PATH__ = f"{os.getcwd()}\{sys.argv[1]}"
        for __LINE__ in __CONTENT__:
            __LINES__.append(__LINE__.removesuffix("\n"))
        for LINE in __LINES__:
            __lineNumber__ = __LINES__.index(LINE) + 1
            if str(LINE).startswith("//"):
                continue
            if str(LINE).startswith(str(printf)):
                args = __getArgs__(LINE, printf)
                if args.startswith(str(inputf)):
                    argA = __getArgs__(args, inputf)
                    try:
                        tData = {}
                        exec(f"value = input({argA})", {"input": input}, tData)
                        value = tData["value"]
                        exec(f"printf(\"{value}\")")
                    except TypeError:
                        __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
                elif args.startswith(str(calc)):
                    argA = __getArgs__(args, calc)
                    try:
                        tData = {}
                        try:
                            exec(f"value = eval({argA})", {"eval": eval}, tData)
                        except NameError:
                            __error__(syntaxError("Too many arguments"), __PATH__, __lineNumber__)
                        value = tData["value"]
                        exec(f"printf(\"{value}\")")
                    except TypeError:
                        __error__(syntaxError("Missing the argument \"calculation\""), __PATH__, __lineNumber__)
                else:
                    try:
                        try:
                            exec(f"printf({args})")
                        except SyntaxError:
                            tArgs = args.removeprefix('"').removesuffix('"').removesuffix(")")
                            if not '"' in tArgs:
                                print(__VARIABLES__[tArgs])
                    except TypeError as e:
                        print(e)
                        if "missing" in str(e):
                            __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
                        else:
                            __error__(syntaxError("Too many arguments"), __PATH__, __lineNumber__)
            if str(LINE).startswith(str(inputf)):
                args = __getArgs__(LINE, inputf)
                try:
                    exec(f"inputf({args})")
                except TypeError:
                    __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
            if str(LINE).startswith(str(calc)):
                args = __getArgs__(LINE, calc)
                try:
                    exec(f"calc({args})")
                except TypeError:
                    __error__(syntaxError("Missing the argument \"calculation\""), __PATH__, __lineNumber__)
            if str(LINE).startswith("declare"):
                words = str(LINE).split(" ")
                value = str(LINE).removeprefix(f"declare {words[1]} = ").replace('"', "").removesuffix(";")
                if value.startswith("inputf("):
                    args = __getArgs__(value, inputf)
                    try:
                        tData = {}
                        exec(f"value = input(\"{args}\")", {"input": input}, tData)
                        value = tData["value"]
                        __VARIABLES__[words[1]] = value
                    except TypeError:
                        __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
                if value.startswith("calc("):
                    args = __getArgs__(value, calc)
                    try:
                        tData = {}
                        exec(f"value = eval(\"{args}\")", {"eval": eval}, tData)
                        value = tData["value"]
                        __VARIABLES__[words[1]] = value
                    except TypeError:
                        __error__(syntaxError("Missing the argument \"calculation\""), __PATH__, __lineNumber__)
                    calcul = []
                    for i in value.split():
                        calcul.append(i)
                    for count, __value in enumerate(calcul):
                        if __value in list(__VARIABLES__):
                            calcul[count] = f"{__VARIABLES__[__value]}"
                    value = "".join(calcul)
                    __VARIABLES__[words[1]] = eval(value)
                else:
                    __VARIABLES__[words[1]] = value
except IndexError:
    try:
        sys.argv[1]
    except IndexError:
        __error__(fatalError("There's no input file"), "command prompt", None)
    else:
        __error__(fatalError("There's a problem with the compiler"), "COMPILER", None)
except FileNotFoundError:
    __error__(fatalError("The input file is doesn't exist"), "command prompt", None)
finally:
    sys.exit()