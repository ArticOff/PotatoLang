# Sorry if my english is bad, I'm a young french developer who just wants to have fun with code

"""
the functionality that needs to be added

-> conditional syntax
-> modular syntax
-> MORE methods
-> easter eggs
"""

# There, I import the modules "sys" and "os"
import sys, os

# The class __color__ is for makes my errors more beautiful
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

# The __method__ class is for create a method in the language
class __method__:
    """
    __method__ class is for create a method in my language

    example:
    def __printf__(text, end="\n"):
        return print(text, end=end)

    printf = __method__("printf", __printf__)
    """
    def __init__(self, name: str, callback: callable) -> None:
        # To set the mathod's name and the callback
        self.funcname = name
        self.callback = callback
    
    def __str__(self) -> str:
        # This function is triggered when we str() the variable
        return f"{self.funcname}("

    def __call__(self, *args):
        # This function is triggered when whe call the variable like a function, it will call the callback.
        data = {}
        exec(f"back = self.callback{args}", {"self": self}, data)
        return data["back"]

# __errorType__ is for make an error
class __errorType__:
    """
    __errorType__ is for make an error

    example:
    fatalError = __errorType__("fatalError")

    __error__(fatalError("There's no input file"), "command prompt", None)
    """
    def __init__(self, errorName: str):
        # To set the error's name
        self.name = errorName
    
    def __call__(self, errorMessage: str):
        # This function is triggered when whe call the variable like a function, it will return a error message.
        self.message = errorMessage
        return self

# This function is for print the error in the console and stop the program
def __error__(__error: __errorType__, __fileName: str, __lineNumber: int) -> None:
    printf(f"{__color__.RED}{__error.name}: {__error.message}.{__color__.GRAY}\n    at \"{__fileName}\", line {__lineNumber}{__color__.STOP}")
    sys.exit()

# This function is for get the args in a method and return it (if the args is a variable, it will return the variable's value)
def __getArgs__(line: str, method: str) -> str:
    __lineNumber__ = __LINES__.index(line) + 1
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
        else:
            __error__(nameError(f"\"{i}\" is not a declared variable"), __PATH__, __lineNumber__)
    return ", ".join(tempData)

# Methods... (the code)
def __printf__(text, end="\n"):
    return print(text, end=end)

def __inputf__(text, end=""):
    return input(f"{text}{end}")

def __calc__(calculation):
    return eval(calculation, {}, {})

def __Error__(message):
    return __error__(_error(message), __PATH__, __lineNumber__)

def __exit__():
    return sys.exit()

# The most important variables !
__VARIABLES__ = {}
__LINES__ = []
__KEYWORDS__ = ["is", "and", "or", "in", "for", "build", "declare", "if", "not", "with"]

# Errors...
fatalError = __errorType__("fatalError")
syntaxError = __errorType__("syntaxError")
nameError = __errorType__("nameError")
_error = __errorType__("error")

# Methods (the variables)
printf = __method__("printf", __printf__)
inputf = __method__("inputf", __inputf__)
calc = __method__("calc", __calc__)
error = __method__("error", __Error__)
stop = __method__("stop", __exit__)

# Function that retun the line by a number
def __getLineByNumber__(number: int) -> str:
    return __LINES__[number]

# Function that return the line's number by a keyword (or a sentence)
def __getLineByWord__(word: str) -> str:
    for i, v in enumerate(__LINES__):
        if word in v:
            return __LINES__[i]
        i += 1

# This code is the language's brain
try:
    # There, we open the input file (in readmode and utf-8)
    with open(file=sys.argv[1], mode="r", encoding="utf-8") as __FILE__:
        # Other variables (don't delete them !)
        __CONTENT__ = __FILE__.readlines()
        __PATH__ = f"{os.getcwd()}\{sys.argv[1]}"

        # We read the file and append to a list (__LINES__) all lines in the file
        for __LINE__ in __CONTENT__:
            __LINES__.append(__LINE__.removesuffix("\n"))

        # Here, we read line by line the __LINES__ content
        for LINE in __LINES__:
            
            # The line number
            __lineNumber__ = __LINES__.index(LINE) + 1

            # Comment
            if str(LINE).startswith("//"):
                continue

            # Method stop()
            if str(LINE).startswith(str(stop)):
                exec("stop()")

            # Method printf()
            if str(LINE).startswith(str(printf)):
                args = __getArgs__(LINE, printf)
                if args.startswith(str(inputf)):
                    argA = __getArgs__(args, inputf)
                    try:
                        tData = {}
                        exec(f"value = inputf({argA})", {"inputf": inputf}, tData)
                        value = tData["value"]
                        exec(f"printf(\"{value}\")")
                    except TypeError:
                        __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
                elif args.startswith(str(calc)):
                    argA = __getArgs__(args, calc)
                    try:
                        tData = {}
                        try:
                            exec(f"value = calc({argA})", {"calc": calc}, tData)
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
                                printf(__VARIABLES__[tArgs])
                    except TypeError as e:
                        if "missing" in str(e):
                            __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
                        else:
                            __error__(syntaxError("Too many arguments"), __PATH__, __lineNumber__)
            
            # Method inputf()
            if str(LINE).startswith(str(inputf)):
                args = __getArgs__(LINE, inputf)
                try:
                    exec(f"inputf({args})")
                except TypeError:
                    __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
            
            # Method calc()
            if str(LINE).startswith(str(calc)):
                args = __getArgs__(LINE, calc)
                try:
                    exec(f"calc({args})")
                except TypeError:
                    __error__(syntaxError("Missing the argument \"calculation\""), __PATH__, __lineNumber__)
            
            # Method error()
            if str(LINE).startswith(str(error)):
                args = __getArgs__(LINE, error)
                try:
                    exec(f"error({args})")
                except TypeError:
                    __error__(syntaxError("Missing the argument \"message\""), __PATH__, __lineNumber__)
            
            # To set a variable in my language
            if str(LINE).startswith("declare"):
                words = str(LINE).split(" ")
                value = str(LINE).removeprefix(f"declare {words[1]} = ").replace('"', "").removesuffix(";")
                if value.startswith("inputf("):
                    args = __getArgs__(value, inputf)
                    try:
                        tData = {}
                        exec(f"value = inputf(\"{args}\")", {"inputf": inputf}, tData)
                        value = tData["value"]
                        __VARIABLES__[words[1]] = value
                    except TypeError:
                        __error__(syntaxError("Missing the argument \"text\""), __PATH__, __lineNumber__)
                if value.startswith("calc("):
                    args = __getArgs__(value, calc)
                    try:
                        tData = {}
                        exec(f"value = calc(\"{args}\")", {"calc": calc}, tData)
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
                    __VARIABLES__[words[1]] = calc(value)
                else:
                    __VARIABLES__[words[1]] = value
            
            # Here, we check if the line has a variable and a "=" after, this is for change the variable's value
            try:
                splittedLine = str(LINE).split(" ")
                if ("".join(splittedLine)).startswith("++"):
                    nVar = "".join(splittedLine).removeprefix("++")
                    for var in __VARIABLES__:
                        if nVar == var:
                            nVal = 1 + int(__VARIABLES__[var])
                            __VARIABLES__[var] = nVal
                if ("".join(splittedLine)).endswith("++"):
                    nVar = "".join(splittedLine).removesuffix("++")
                    for var in __VARIABLES__:
                        if nVar == var:
                            nVal = int(__VARIABLES__[var]) + 1
                            __VARIABLES__[var] = nVal
                tempLine = []
                _tempLine = []
                for i in splittedLine:
                    tempLine.append(i)
                for var in __VARIABLES__:
                    if splittedLine[0] == var:
                        value = str(LINE).removeprefix(f"{var} = ")
                        for count, item in enumerate(tempLine[2:]):
                            if item in list(__VARIABLES__):
                                tempLine[count + 2] = __VARIABLES__[item]
                        for i in tempLine[2:]:
                            _tempLine.append(i)
                        __VARIABLES__[var] = calc(" ".join(_tempLine))
            except IndexError:
                continue
except IndexError:
    # Here, it seems logic to unbderstand
    try:
        # This line is for check if there is an input file
        sys.argv[1]
    except IndexError:
        __error__(fatalError("There's no input file"), "command prompt", None)
    else:
        __error__(fatalError("There's a problem with the compiler"), "COMPILER", None)
except FileNotFoundError:
    __error__(fatalError("The input file is doesn't exist"), "command prompt", None)
finally:
    # When the compilation has finished, we stop the language
    sys.exit()
    # zzz...