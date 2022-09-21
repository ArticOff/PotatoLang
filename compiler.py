# Sorry if my english is bad, I'm a young french developer who just wants to have fun with code

"""
TODO list

-> conditional syntax
-> MORE methods (working on...)
-> easter eggs
"""

# There, I import the modules "sys", "os", "re", "getopt" and "typing"
import sys, os, re, getopt
from typing import (
    NoReturn
)

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
                __PATH__ = globals()["__PATH__"]
                __lineNumber__ = globals()["__lineNumber__"]
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
    printf(f"{__color__.RED}{__error}: {message}{__color__.GRAY}\n    at \"{__fileName}\", line {__lineNumber}{__color__.STOP}")
    sys.exit()

# This function is for get the args in a method and return it (if the args is a variable, it will return the variable's value)
def __getArgs__(line: str, method: str) -> str:
    __lineNumber__ = globals()["__lineNumber__"]
    tempData = []
    tempValues = []
    tempSplit = None
    line = line.replace(str(method), "").removeprefix("(").removesuffix(")").removesuffix(";").split(",")
    for i in line:
        if i in list(__VARIABLES__):
            for count, value in enumerate(line):
                if value == i:
                    line[count] = f"\"{__VARIABLES__[i]}\""
                    tempData.append(f"\"{__VARIABLES__[i]}\"")
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
            nameError(f"\"{i}\" is not a declared variable.")
    return ", ".join(tempData)

def __getArgsInsideFunction__(line: str, method: str, __locals: dict) -> str:
    VAR = __locals
    __lineNumber__ = globals()["__lineNumber__"]
    tempData = []
    tempValues = []
    tempSplit = None
    line = line.replace(str(method), "").removeprefix("(").removesuffix(")").removesuffix(";").split(",")
    for i in line:
        if i in list(VAR):
            for count, value in enumerate(line):
                if value == i:
                    line[count] = f"{VAR[i]}"
                    tempData.append(VAR[i])
        else:
            tempData.append(i)
    for _item in tempData:
        tempSplit = str(_item).split()
        for i in tempSplit:
            if "[" and "]" in i:
                tempValues.append(i.replace('"', "").removeprefix("[").removesuffix("]").replace(",", ""))
    for i in tempValues:
        if i in list(VAR):
            string = ("".join(tempData)).replace(f"[{i}]", str(VAR[i]).replace('"', ""))
            tempData[0] = string
        else:
            nameError(f"\"{i}\" is not a declared variable.")
    for count, item in enumerate(tempData):
        if item in list(__VARIABLES__):
            tempData[count] = f"\"{__VARIABLES__[item]}\""
        else:
            SplittedValue = str(tempData[0]).split()
            for count, item in enumerate(SplittedValue):
                if item in list(__VARIABLES__):
                    SplittedValue[count] = __VARIABLES__[item]
            tempData = [" ".join(SplittedValue)]
    return ", ".join(tempData)

def __fire__(function: __method__, args: str) -> str:
    tData = {}
    exec(f"value = {function.funcname}(\"{args}\")", {f"{function.funcname}": function}, tData)
    return tData["value"]

# Methods... (the code)
def __printf__(text, end="\n"):
    return print(text, end=end)

def __inputf__(text):
    return input(f"{text}")

def __calc__(calculation):
    try:
        eval(calculation)
    except ZeroDivisionError:
        mathError("Divisions by 0 are impossible.")
    return eval(calculation, {}, {})

def __Error__(message):
    return error(message)

def __exit__():
    return sys.exit()

# Errors...
class fatalError(__errorType__): ...
class syntaxError(__errorType__): ...
class nameError(__errorType__): ...
class error(__errorType__): ...
class mathError(__errorType__): ...
class returnError(__errorType__): ...
class fileError(__errorType__): ...

# Methods (the variables)
printf = __method__("printf", __printf__)
inputf = __method__("inputf", __inputf__)
calc = __method__("calc", __calc__)
_error = __method__("error", __Error__)
stop = __method__("stop", __exit__)

try:
    __File__ = sys.argv[2]
except IndexError:
    __File__ = None

# The most important variables !
__LINES__ = []
__KEYWORDS__ = ["is", "and", "or", "in", "for", "build", "declare", "if", "not", "with", "as"]
__METHODS__ = [printf, inputf, calc, _error, stop]
__FUNCTIONS__ = {}
__isFunction__ = False
__whatFunction__ = None
__argFunction__ = []
__codeFunction__ = False
__funcCode__ = []
__funcVarTemp__ = {}
__BUILTVAR__ = ["__FILE__", "__KEYWORDS__", "__BUILTINS__", "__VERSION__", "__MAIN__"]
__VARIABLES__ = {
    "__FILE__": __File__,
    "__KEYWORDS__": ", ".join(__KEYWORDS__),
    "__BUILTINS__": ", ".join([f"{i.funcname}()" for i in __METHODS__]),
    "__VERSION__": "v2.1.1a",
    "__MAIN__": __name__
}

# Function that retun the line by a number
def __getLineByNumber__(number: int) -> str:
    return __LINES__[number]

# Function that return the line's number by a keyword (or a sentence)
def __getLineByWord__(word: str) -> str:
    for i, v in enumerate(__LINES__):
        if word in v:
            return __LINES__[i]
        i += 1

try:
    arguments, values = getopt.getopt(sys.argv[1:], "chmv", ["Console", "Help", "File", "Version"])
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-c", "--Console"):
            print("WIP")
        elif currentArgument in ("-h", "--  Help"):
            print("""
usage: PotatoLang.exe [option] ...
options:    
-c --Console    : Run the code in a terminal. (/!\ WIP)
-h --Help       : Display the help message.
-m --File       : Read a file and run the content.
-v --Version    : Display the version.
            """)
        elif currentArgument in ("-m", "--File"):

            # This code is the language's brain
            try:
                # There, we open the input file (in readmode and utf-8)
                with open(file=sys.argv[2], mode="r", encoding="utf-8") as __FILE__:
                    # Other variables (don't delete them !)
                    __CONTENT__ = __FILE__.readlines()
                    __PATH__ = f"{os.getcwd()}\{sys.argv[2]}"

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
                        
                        # If there is a function, we take the code
                        if __codeFunction__:
                            if str(LINE).startswith("}"):
                                __isFunction__ = False
                                __codeFunction__ = False
                                __funcVarTemp__ = {}
                                __whatFunction__ = None
                            elif not bool(str(LINE).startswith("   ")):
                                syntaxError("expected an indented block.")
                            else:
                                line = str(LINE).removeprefix("    ")
                                if str(line).startswith("return"):
                                    words = str(line).split(" ")
                                    varTarget = words[1]
                                    if '"' in varTarget:
                                        returnError(f"The return must contain a variable, not text.")
                                    for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                                        if varTarget == str(number):
                                            returnError(f"The return must contain a variable, not a number.")
                                    if varTarget in list(__funcVarTemp__):
                                        __VARIABLES__[varTarget] = f"{__funcVarTemp__[varTarget]}"
                                    else:
                                        nameError(f"\"{varTarget}\" is not a declared variable.")
                                if str(line).startswith("declare"):
                                    words = str(line).split(" ")
                                    for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                                        if words[1] == str(number):
                                            nameError(f"The variable's name must be text, not a number.")
                                    value = str(line).removeprefix(f"declare {words[1]} = ").replace('"', "").removesuffix(";")
                                    if value == str(line):
                                        __funcVarTemp__[words[1]] = None
                                    elif value.startswith(str(inputf)):
                                        args = __getArgsInsideFunction__(value, inputf, __funcVarTemp__)
                                        try:
                                            value = __fire__(inputf, args)
                                            __funcVarTemp__[words[1]] = value
                                        except TypeError:
                                            syntaxError("Missing the argument \"text\".")
                                    elif value.startswith(str(calc)):
                                        args = __getArgsInsideFunction__(value, calc, __funcVarTemp__)
                                        try:
                                            value = __fire__(calc, args)
                                            __funcVarTemp__[words[1]] = value
                                        except TypeError:
                                            syntaxError("Missing the argument \"calculation\".")
                                        calcul = []
                                        for i in value.split():
                                            calcul.append(i)
                                        for count, __value in enumerate(calcul):
                                            if __value in list(__funcVarTemp__):
                                                calcul[count] = f"{__funcVarTemp__[__value]}"
                                        value = "".join(calcul)
                                        __funcVarTemp__[words[1]] = calc(value)
                                    elif value in list(__funcVarTemp__):
                                        __funcVarTemp__[words[1]] = __funcVarTemp__[value]
                                    elif words[1] in __KEYWORDS__:
                                        nameError(f"\"{words[1]}\" variable is a keyword.")
                                    elif words[1] in __BUILTVAR__:
                                        nameError(f"\"{words[1]}\" variable is a built-in variable.")
                                    else:
                                        __funcVarTemp__[words[1]] = value
                                try:
                                    splittedLine = str(line).split(" ")
                                    if splittedLine[0] in __BUILTVAR__:
                                        nameError(f"\"{splittedLine[0]}\" variable is a built-in variable.")
                                    if ("".join(splittedLine)).startswith("++"):
                                        nVar = "".join(splittedLine).removeprefix("++")
                                        for var in __funcVarTemp__:
                                            if nVar == var:
                                                nVal = 1 + float(__funcVarTemp__[var])
                                                if nVal.is_integer():
                                                    nVal = int(nVal)
                                                __funcVarTemp__[var] = nVal
                                    if ("".join(splittedLine)).endswith("++"):
                                        nVar = "".join(splittedLine).removesuffix("++")
                                        for var in __funcVarTemp__:
                                            if nVar == var:
                                                nVal = float(__funcVarTemp__[var]) + 1
                                                if nVal.is_integer():
                                                    nVal = int(nVal)
                                                __funcVarTemp__[var] = nVal
                                    tempLine = []
                                    _tempLine = []
                                    for i in splittedLine:
                                        tempLine.append(i)
                                    for var in __funcVarTemp__:
                                        if splittedLine[0] == var:
                                            value = str(LINE).removeprefix(f"{var} = ")
                                            if value.startswith(str(inputf)):
                                                args = __getArgsInsideFunction__(value, inputf, __funcVarTemp__)
                                                try:
                                                    __funcVarTemp__[var] = inputf(args.replace('"', ""))
                                                except TypeError:
                                                    syntaxError("Missing the argument \"text\".")
                                            else:
                                                for count, item in enumerate(tempLine[2:]):
                                                    if item in list(__funcVarTemp__):
                                                        tempLine[count + 2] = __funcVarTemp__[item]
                                                for i in tempLine[2:]:
                                                    _tempLine.append(i)
                                                __funcVarTemp__[var] = calc(" ".join(_tempLine))
                                except IndexError:
                                    continue
                                __funcCode__.append(line)
                                __FUNCTIONS__[__whatFunction__]["code"] = __funcCode__
                                __FUNCTIONS__[__whatFunction__]["variables"] = __funcVarTemp__
                        
                        # Check if there's a function call  
                        for function in list(__FUNCTIONS__):
                            _M = (str(LINE).split("("))[0]
                            if _M == function:
                                funcArgs = __FUNCTIONS__[function]["args"]
                                funcVar = __FUNCTIONS__[function]["variables"]
                                Args = str(LINE).removeprefix(f"{function}(").removesuffix(")").split(",")
                                for count, item in enumerate(list(funcVar)):
                                    if item == funcArgs[count]:
                                        funcVar[item] = Args[count]
                                funcCode = __FUNCTIONS__[function]["code"]
                                for o in list(__FUNCTIONS__):
                                    if str(funcCode[0]).startswith(o):
                                        argFuncCode = __FUNCTIONS__[o]["code"]
                                        for i in argFuncCode:
                                            if "system" in funcCode[0]:
                                                args = str(funcCode[0]).removeprefix(f"system(").removesuffix(")")
                                                exec(f"os.system({args})", {}, {})
                                            if "python" in funcCode[0]:
                                                args = str(funcCode[0]).removeprefix(f"python(").removesuffix(")").replace('"', "")
                                                exec(args, {}, {})
                                            if str(funcCode[0]).removesuffix("()") in list(__FUNCTIONS__):
                                                argFuncCode = __FUNCTIONS__[str(funcCode[0]).removesuffix("()")]["code"]
                                                for c in argFuncCode:
                                                    if str(c).startswith("system"):
                                                        args = str(c).removeprefix(f"system(").removesuffix(")")
                                                        os.system(f"{args}")
                                                    if str(c).startswith("python"):
                                                        args = str(c).removeprefix(f"python(").removesuffix(")").replace('"', "")
                                                        exec(args, {}, {})
                                                    else:
                                                        exec(f"{c}")
                                            """
                                            else:
                                                Builtins = [f"{a.funcname}()" for a in __METHODS__]
                                                for b in Builtins:
                                                    if f"{(str(i).split('('))[0]}()" == b:
                                                        print(funcCode[0])
                                                        args = (str(funcCode[0]).removesuffix(")").split("("))[1]
                                                        print(args)
                                            """
                                _Var = funcVar
                                Builtins = [f"{i.funcname}()" for i in __METHODS__]
                                for line in funcCode:
                                    if str(line).startswith("declare"):
                                        words = str(line).split(" ")
                                        value = str(line).removeprefix(f"declare {words[1]} = ").replace('"', "").removesuffix(";")
                                        if value == str(line):
                                            _Var[words[1]] = None
                                        elif value.startswith(str(inputf)):
                                            args = __getArgsInsideFunction__(value, inputf, funcVar)
                                            try:
                                                value = __fire__(inputf, args)
                                                _Var[words[1]] = value
                                            except TypeError:
                                                syntaxError("Missing the argument \"text\".")
                                        elif value.startswith(str(calc)):
                                            args = __getArgsInsideFunction__(value, calc, funcVar)
                                            try:
                                                value = __fire__(calc, args)
                                                _Var[words[1]] = value
                                            except TypeError:
                                                syntaxError("Missing the argument \"calculation\".")
                                            calcul = []
                                            for i in value.split():
                                                calcul.append(i)
                                            for count, __value in enumerate(calcul):
                                                if __value in list(_Var):
                                                    calcul[count] = f"{_Var[__value]}"
                                            value = "".join(calcul)
                                            _Var[words[1]] = calc(value)
                                        elif value in list(_Var):
                                            _Var[words[1]] = _Var[value]
                                        elif words[1] in __KEYWORDS__:
                                            nameError(f"\"{words[1]}\" variable is a keyword.")
                                        elif words[1] in __BUILTVAR__:
                                            nameError(f"\"{words[1]}\" variable is a built-in variable.")
                                        else:
                                            _Var[words[1]] = value
                                    try:
                                        splittedLine = str(line).split(" ")
                                        if splittedLine[0] in __BUILTVAR__:
                                            nameError(f"\"{splittedLine[0]}\" variable is a built-in variable.")
                                        if ("".join(splittedLine)).startswith("++"):
                                            nVar = "".join(splittedLine).removeprefix("++")
                                            for var in _Var:
                                                if nVar == var:
                                                    nVal = 1 + float(_Var[var])
                                                    if nVal.is_integer():
                                                        nVal = int(nVal)
                                                    _Var[var] = nVal
                                        if ("".join(splittedLine)).endswith("++"):
                                            nVar = "".join(splittedLine).removesuffix("++")
                                            for var in _Var:
                                                if nVar == var:
                                                    nVal = float(_Var[var]) + 1
                                                    if nVal.is_integer():
                                                        nVal = int(nVal)
                                                    _Var[var] = nVal
                                        tempLine = []
                                        _tempLine = []
                                        for i in splittedLine:
                                            tempLine.append(i)
                                        for var in _Var:
                                            if splittedLine[0] == var:
                                                value = str(LINE).removeprefix(f"{var} = ")
                                                if value.startswith(str(inputf)):
                                                    args = __getArgsInsideFunction__(value, inputf, funcVar)
                                                    try:
                                                        funcVar[var] = inputf(args.replace('"', ""))
                                                    except TypeError:
                                                        syntaxError("Missing the argument \"text\".")
                                                else:
                                                    for count, item in enumerate(tempLine[2:]):
                                                        if item in list(funcVar):
                                                            tempLine[count + 2] = funcVar[item]
                                                    for i in tempLine[2:]:
                                                        _tempLine.append(i)
                                                    funcVar[var] = calc(" ".join(_tempLine))
                                    except IndexError:
                                        continue
                                    lineM = (str(line).split("("))[0]
                                    for o in __METHODS__:
                                        if o.funcname == lineM:
                                            value = __getArgsInsideFunction__(line, lineM, funcVar)
                                            exec(f"{o.funcname}({value})", {f"{o.funcname}": o})
                                        if lineM in o.funcname and lineM != o.funcname:
                                            if lineM in list(__FUNCTIONS__):
                                                continue
                                            else:
                                                syntaxError(f"\"{lineM}()\" is not a method, would you mean \"{o.funcname}()\" ?")            
                        # Method stop()
                        if str(LINE).startswith(str(stop)):
                            exec("stop()")

                        # Method printf()
                        if str(LINE).startswith(str(printf)):
                            args = __getArgs__(LINE, printf)
                            if args.startswith(str(inputf)):
                                argA = __getArgs__(args, inputf)
                                try:
                                    value = __fire__(inputf, args)
                                    exec(f"printf(\"{value}\")")
                                except TypeError:
                                    syntaxError("Missing the argument \"text\".")
                            elif args.startswith(str(calc)):
                                argA = __getArgs__(args, calc)
                                try:
                                    try:
                                        value = __fire__(calc, args)
                                    except NameError:
                                        syntaxError("Too many arguments.")
                                    exec(f"printf(\"{value}\")")
                                except TypeError:
                                    syntaxError("Missing the argument \"calculation\".")
                            else:
                                try:
                                    try:
                                        try:
                                            exec(f"printf({args})")
                                        except NameError:
                                            nameError(f"\"{args}\" is not a declared variable.")
                                    except SyntaxError:
                                        tArgs = args.removeprefix('"').removesuffix('"').removesuffix(")")
                                        if not '"' in tArgs:
                                            printf(__VARIABLES__[tArgs])
                                except TypeError as e:
                                    if "missing" in str(e):
                                        syntaxError("Missing the argument \"text\".")
                                    else:
                                        syntaxError("Too many arguments.")
                        
                        # Method inputf()
                        if str(LINE).startswith(str(inputf)):
                            args = __getArgs__(LINE, inputf)
                            try:
                                exec(f"inputf({args})")
                            except TypeError:
                                syntaxError("Missing the argument \"text\".")
                        
                        # Method calc()
                        if str(LINE).startswith(str(calc)):
                            args = __getArgs__(LINE, calc)
                            try:
                                exec(f"calc({args})")
                            except TypeError:
                                syntaxError("Missing the argument \"calculation\".")
                        
                        # Method error()
                        if str(LINE).startswith(str(_error)):
                            args = __getArgs__(LINE, _error)
                            try:
                                exec(f"_error({args})")
                            except TypeError:
                                syntaxError("Missing the argument \"message\".")
                        
                        # To set a function
                        if str(LINE).startswith("build"):
                            words = str(LINE).split(" ")
                            ids = str(LINE).removeprefix("build ").removesuffix(")").split("(")
                            funcArgs = ids[1:]
                            if funcArgs[0] == "":
                                del funcArgs[0]
                            funcArgs = " ".join(funcArgs).replace(",", "").split(" ")
                            funcName = ids[0]
                            if funcName in list(__KEYWORDS__):
                                nameError(f"\"{funcName}()\" function is a keyword.")
                            __isFunction__ = True
                            __whatFunction__ = funcName
                            __argFunction__ = funcArgs
                            __funcCode__ = []
                            for i in funcArgs:
                                if i == "":
                                    i
                                else:
                                    __funcVarTemp__[i] = None

                        if str(LINE).startswith("with"):
                            if str(LINE).split(" ")[1] == "system":
                                funct = {}
                                funct["args"] = ["text"]
                                funct["code"] = ["os.system(text)"]
                                funct["variables"] = {"text": None}
                                __FUNCTIONS__["system"] = funct
                                funct = {}
                                funct["args"] = ["text"]
                                funct["code"] = ["exec(text)"]
                                funct["variables"] = {"text": None}
                                __FUNCTIONS__["python"] = funct
                                funct = {}
                            else:
                                try:
                                    with open((str(LINE).split(" "))[1], mode="r", encoding="utf-8") as f:
                                        ls = []
                                        cont = f.readlines()
                                        for l in cont:
                                            ls.append(l.removesuffix("\n"))

                                        # Here, we read line by line the __LINES__ content
                                        for _Line in ls:

                                            if str(_Line).startswith("with system"):
                                                funct = {}
                                                funct["args"] = ["text"]
                                                funct["code"] = ["os.system(text)"]
                                                funct["variables"] = {"text": None}
                                                __FUNCTIONS__["system"] = funct
                                                funct = {}
                                                funct["args"] = ["text"]
                                                funct["code"] = ["exec(text)"]
                                                funct["variables"] = {"text": None}
                                                __FUNCTIONS__["python"] = funct
                                                funct = {}

                                            if str(_Line).startswith("build"):
                                                words = str(_Line).split(" ")
                                                ids = str(_Line).removeprefix("build ").removesuffix(")").split("(")
                                                funcArgs = ids[1:]
                                                if funcArgs[0] == "":
                                                    del funcArgs[0]
                                                funcArgs = " ".join(funcArgs).replace(",", "").split(" ")
                                                funcName = ids[0]
                                                if funcName in list(__KEYWORDS__):
                                                    nameError(f"\"{funcName}()\" function is a keyword.")
                                                __isFunction__ = True
                                                __whatFunction__ = funcName
                                                __argFunction__ = funcArgs
                                                __funcCode__ = []
                                                for i in funcArgs:
                                                    if i == "":
                                                        i
                                                    else:
                                                        __funcVarTemp__[i] = None

                                            if __codeFunction__:
                                                if str(_Line).startswith("}"):
                                                    __isFunction__ = False
                                                    __codeFunction__ = False
                                                    __funcVarTemp__ = {}
                                                    __whatFunction__ = None
                                                elif not bool(str(_Line).startswith("   ")):
                                                    syntaxError("expected an indented block.")
                                                else:
                                                    line = str(_Line).removeprefix("    ")
                                                    if str(line).startswith("return"):
                                                        words = str(line).split(" ")
                                                        varTarget = words[1]
                                                        if '"' in varTarget:
                                                            returnError(f"The return must contain a variable, not text.")
                                                        for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                                                            if varTarget == str(number):
                                                                returnError(f"The return must contain a variable, not a number.")
                                                        if varTarget in list(__funcVarTemp__):
                                                            __VARIABLES__[varTarget] = f"{__funcVarTemp__[varTarget]}"
                                                        else:
                                                            nameError(f"\"{varTarget}\" is not a declared variable.")
                                                    if str(line).startswith("declare"):
                                                        words = str(line).split(" ")
                                                        for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                                                            if words[1] == str(number):
                                                                nameError(f"The variable's name must be text, not a number.")
                                                        value = str(line).removeprefix(f"declare {words[1]} = ").replace('"', "").removesuffix(";")
                                                        if value == str(line):
                                                            __funcVarTemp__[words[1]] = None
                                                        elif value.startswith(str(inputf)):
                                                            args = __getArgsInsideFunction__(value, inputf, __funcVarTemp__)
                                                            try:
                                                                value = __fire__(inputf, args)
                                                                __funcVarTemp__[words[1]] = value
                                                            except TypeError:
                                                                syntaxError("Missing the argument \"text\".")
                                                        elif value.startswith(str(calc)):
                                                            args = __getArgsInsideFunction__(value, calc, __funcVarTemp__)
                                                            try:
                                                                value = __fire__(calc, args)
                                                                __funcVarTemp__[words[1]] = value
                                                            except TypeError:
                                                                syntaxError("Missing the argument \"calculation\".")
                                                            calcul = []
                                                            for i in value.split():
                                                                calcul.append(i)
                                                            for count, __value in enumerate(calcul):
                                                                if __value in list(__funcVarTemp__):
                                                                    calcul[count] = f"{__funcVarTemp__[__value]}"
                                                            value = "".join(calcul)
                                                            __funcVarTemp__[words[1]] = calc(value)
                                                        elif value in list(__funcVarTemp__):
                                                            __funcVarTemp__[words[1]] = __funcVarTemp__[value]
                                                        elif words[1] in __KEYWORDS__:
                                                            nameError(f"\"{words[1]}\" variable is a keyword.")
                                                        elif words[1] in __BUILTVAR__:
                                                            nameError(f"\"{words[1]}\" variable is a built-in variable.")
                                                        else:
                                                            __funcVarTemp__[words[1]] = value
                                                    try:
                                                        splittedLine = str(line).split(" ")
                                                        if splittedLine[0] in __BUILTVAR__:
                                                            nameError(f"\"{splittedLine[0]}\" variable is a built-in variable.")
                                                        if ("".join(splittedLine)).startswith("++"):
                                                            nVar = "".join(splittedLine).removeprefix("++")
                                                            for var in __funcVarTemp__:
                                                                if nVar == var:
                                                                    nVal = 1 + float(__funcVarTemp__[var])
                                                                    if nVal.is_integer():
                                                                        nVal = int(nVal)
                                                                    __funcVarTemp__[var] = nVal
                                                        if ("".join(splittedLine)).endswith("++"):
                                                            nVar = "".join(splittedLine).removesuffix("++")
                                                            for var in __funcVarTemp__:
                                                                if nVar == var:
                                                                    nVal = float(__funcVarTemp__[var]) + 1
                                                                    if nVal.is_integer():
                                                                        nVal = int(nVal)
                                                                    __funcVarTemp__[var] = nVal
                                                        tempLine = []
                                                        _tempLine = []
                                                        for i in splittedLine:
                                                            tempLine.append(i)
                                                        for var in __funcVarTemp__:
                                                            if splittedLine[0] == var:
                                                                value = str(_Line).removeprefix(f"{var} = ")
                                                                if value.startswith(str(inputf)):
                                                                    args = __getArgsInsideFunction__(value, inputf, __funcVarTemp__)
                                                                    try:
                                                                        __funcVarTemp__[var] = inputf(args.replace('"', ""))
                                                                    except TypeError:
                                                                        syntaxError("Missing the argument \"text\".")
                                                                else:
                                                                    for count, item in enumerate(tempLine[2:]):
                                                                        if item in list(__funcVarTemp__):
                                                                            tempLine[count + 2] = __funcVarTemp__[item]
                                                                    for i in tempLine[2:]:
                                                                        _tempLine.append(i)
                                                                    __funcVarTemp__[var] = calc(" ".join(_tempLine))
                                                    except IndexError:
                                                        continue
                                                    __funcCode__.append(line)
                                                    __FUNCTIONS__[__whatFunction__]["code"] = __funcCode__
                                                    __FUNCTIONS__[__whatFunction__]["variables"] = __funcVarTemp__

                                            if str(_Line).startswith("{") and __isFunction__ and __whatFunction__:
                                                __codeFunction__ = True
                                                funct = {}
                                                funct["args"] = __argFunction__
                                                funct["code"] = []
                                                funct["variables"] = {}
                                                __FUNCTIONS__[__whatFunction__] = funct

                                except FileNotFoundError:
                                    fileError(f"There's no file named \"{(str(LINE).split(' '))[1]}\"")

                        if str(LINE).startswith("{") and __isFunction__ and __whatFunction__:
                            __codeFunction__ = True
                            funct = {}
                            funct["args"] = __argFunction__
                            funct["code"] = []
                            funct["variables"] = {}
                            __FUNCTIONS__[__whatFunction__] = funct
                    
                        # To set a variable in my language
                        if str(LINE).startswith("declare"):
                            words = str(LINE).split(" ")
                            value = str(LINE).removeprefix(f"declare {words[1]} = ").replace('"', "").removesuffix(";")
                            if value == str(LINE):
                                __VARIABLES__[words[1]] = None
                            elif value.startswith(str(inputf)):
                                args = __getArgs__(value, inputf)
                                try:
                                    value = __fire__(inputf, args)
                                    __VARIABLES__[words[1]] = value
                                except TypeError:
                                    syntaxError("Missing the argument \"text\".")
                            elif value.startswith(str(calc)):
                                args = __getArgs__(value, calc)
                                try:
                                    value = __fire__(calc, args)
                                    __VARIABLES__[words[1]] = value
                                except TypeError:
                                    syntaxError("Missing the argument \"calculation\".")
                                calcul = []
                                for i in value.split():
                                    calcul.append(i)
                                for count, __value in enumerate(calcul):
                                    if __value in list(__VARIABLES__):
                                        calcul[count] = f"{__VARIABLES__[__value]}"
                                value = "".join(calcul)
                                __VARIABLES__[words[1]] = calc(value)
                            elif value in list(__VARIABLES__):
                                __VARIABLES__[words[1]] = __VARIABLES__[value]
                            elif words[1] in __KEYWORDS__:
                                nameError(f"\"{words[1]}\" variable is a keyword.")
                            elif words[1] in __BUILTVAR__:
                                nameError(f"\"{words[1]}\" variable is a built-in variable.")
                            else:
                                __VARIABLES__[words[1]] = value
                        
                        # Here, we check if the line has a variable and a "=" after, this is for change the variable's value
                        try:
                            splittedLine = str(LINE).split(" ")
                            if splittedLine[0] in __BUILTVAR__:
                                nameError(f"\"{words[1]}\" variable is a built-in variable.")
                            if ("".join(splittedLine)).startswith("++"):
                                nVar = "".join(splittedLine).removeprefix("++")
                                for var in __VARIABLES__:
                                    if nVar == var:
                                        nVal = 1 + float(__VARIABLES__[var])
                                        if nVal.is_integer():
                                            nVal = int(nVal)
                                        __VARIABLES__[var] = nVal
                            if ("".join(splittedLine)).endswith("++"):
                                nVar = "".join(splittedLine).removesuffix("++")
                                for var in __VARIABLES__:
                                    if nVar == var:
                                        nVal = float(__VARIABLES__[var]) + 1
                                        if nVal.is_integer():
                                            nVal = int(nVal)
                                        __VARIABLES__[var] = nVal
                            tempLine = []
                            _tempLine = []
                            for i in splittedLine:
                                tempLine.append(i)
                            for var in __VARIABLES__:
                                if splittedLine[0] == var:
                                    value = str(LINE).removeprefix(f"{var} = ")
                                    if value.startswith(str(inputf)):
                                        args = __getArgs__(value, inputf)
                                        try:
                                            __VARIABLES__[var] = inputf(args.replace('"', ""))
                                        except TypeError:
                                            syntaxError("Missing the argument \"text\".")
                                    else:
                                        for count, item in enumerate(tempLine[2:]):
                                            if item in list(__VARIABLES__):
                                                tempLine[count + 2] = __VARIABLES__[item]
                                        for i in tempLine[2:]:
                                            _tempLine.append(i)
                                        __VARIABLES__[var] = calc(" ".join(_tempLine))
                        except IndexError:
                            continue
                        else:
                            for method in __METHODS__:
                                fmethod = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", str(LINE)).replace("()", "")
                                if str(LINE) == "":
                                    continue
                                if fmethod in method.funcname and not fmethod == method.funcname:
                                    _method = method.funcname
                                    if fmethod in list(__FUNCTIONS__):
                                        continue
                                    else:
                                        syntaxError(f"\"{fmethod}()\" is not a method, would you mean \"{_method}()\" ?")
            except IndexError:
                # Here, it seems logic to unbderstand
                try:
                    # This line is for check if there is an input file
                    sys.argv[2]
                except IndexError:
                    fatalError("There's no input file.")
                else:
                    fatalError("There's a problem with the compiler.")
            except FileNotFoundError:
                fatalError("The input file is doesn't exist.")
            finally:
                # When the compilation has finished, we stop the language
                sys.exit()
                # zzz...
        elif currentArgument in ("-v", "--Version"):
            print(__VARIABLES__["__VERSION__"])
except getopt.error as e:
    print(e)