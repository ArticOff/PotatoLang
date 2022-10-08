# /!\ PLEASE, READ THE CONVENTIONS.txt BEFORE WORKING ON THE LANGUAGE /!\

# Sorry if my english is bad, I'm a young french developer who just wants to have fun with code

"""
TODO list

-> conditional syntax
-> MORE methods (working on...)
-> easter eggs
""" 

import sys, os, getopt

from PotatoLang.Clear import GarbageCollection as GC
from PotatoLang.Clear import variableHandler
from PotatoLang.Keywords import Any
from PotatoLang.Variable import Init
from PotatoLang.File import File
from PotatoLang.Function import (
    functionHandler,
    function,
    functions,
    modules
)
from PotatoLang.Modules import (
    Sys,
    Math,
    Random
)
from PotatoLang.Constants import (
    __Keywords__,
    __Version__
)
from PotatoLang.DataTypes import (
    DataType,
    String,
    Number,
    Boolean,
    List
)
from PotatoLang.Error import (
    fatalError,
    syntaxError,
    nameError,
    error,
    mathError,
    returnError,
    fileError,
    moduleError,
    optionError,
    dataTypeNotSupported
)

CODE_isFunction = False
CODE_functions = {}

CODE_longComment = False

__globals__ = {}
variable = Init(__globals__)
VariableHandler = variableHandler(globals())
FunctionHandler = functionHandler(functions, CODE_functions, VariableHandler, globals())

__importedModules__ = {}

try:
    __File__ = sys.argv[2]
    __Path__ = f"{os.getcwd()}\{__File__}"
except IndexError:
    __File__ = __Path__ = None

variable.set("__FILE__", str(__File__))
variable.set("__KEYWORDS__", list(__Keywords__))
variable.set("__VERSION__", str(__Version__))
variable.set("__PATH__", str(__Path__))
variable.set("__NAME__", str(__name__))

def __getArgs__(line: str, method: str) -> str:
    TEMP_Data = TEMP_Values = []
    line = line.replace(str(method), "").removeprefix("(").removesuffix(")").removesuffix(";").split(",")
    for TEMP_i in line:
        if TEMP_i in list(variable.globals):
            for TEMP_count, TEMP_value in enumerate(line):
                if TEMP_value == TEMP_i:
                    line[TEMP_count] = f"\"{variable.get(TEMP_i)}\""
                    TEMP_Data.append(f"\"{variable.get(TEMP_i)}\"")
        else:
            TEMP_Data.append(TEMP_i)
    for TEMP_item in TEMP_Data:
        for TEMP_i in str(TEMP_item).split():
            if "[" and "]" in TEMP_i:
                TEMP_Values.append(TEMP_i.replace('"', "").removeprefix("[").removesuffix("]").replace(",", ""))
    for TEMP_i in TEMP_Values:
        if TEMP_i in list(variable.globals):
            TEMP_Data[0] = ("".join(TEMP_Data)).replace(f"[{TEMP_i}]", variable.get(TEMP_i))
    return ",".join(TEMP_Data)

def __fire__(function: str, args: str) -> Any:
    TEMP_Data = {}
    exec(f"TEMP_value = {function}({args})", globals(), TEMP_Data)
    return TEMP_Data["TEMP_value"]

def checkDataType(_return: Any) -> DataType:
    if isinstance(_return, str):
        return String(_return)
    elif isinstance(_return, int) or isinstance(_return, float):
        return Number(_return)
    elif isinstance(_return, list) or isinstance(_return, tuple):
        return List(_return)
    elif isinstance(_return, bool):
        return Boolean(_return)
    else:
        dataTypeNotSupported("This data type is unsupported.")

def checkFunctions(TEMP_l: str = None):
    if TEMP_l is None:
        TEMP_l = lineContent
    TEMP_Data = {}
    for TEMP_function in functions:
        if TEMP_l.startswith(TEMP_function):
            TEMP_args = __getArgs__(lineContent, TEMP_function)
            try:
                # print(f"index: {TEMP_function}\nargs: {TEMP_args}")
                exec(f"TEMP_response = {TEMP_function}({TEMP_args})", globals(), TEMP_Data)
                return TEMP_Data["TEMP_response"]
            except NameError:
                if len(__importedModules__) == 0:
                    FunctionHandler.exeCode(TEMP_function)
                else:
                    for TEMP_modules in list(__importedModules__):
                        if TEMP_function in __importedModules__[TEMP_modules]:
                            exec(f"TEMP_response = {TEMP_modules}().{TEMP_function}({TEMP_args})", globals(), TEMP_Data)
                            return TEMP_Data["TEMP_response"]
                        else:
                            FunctionHandler.exeCode(TEMP_function)
            except TypeError:
                syntaxError("Missing a argument.")

def checkCreateFunction() -> None:
    if lineContent.startswith("build"):
        TEMP_index = lineContent.removeprefix("build ").split("(")[0]
        TEMP_args = str((lineContent.split("("))[1]).replace(",", "").removesuffix(")").removesuffix(";").split(" ")
        FunctionHandler.create(TEMP_index, TEMP_args)
        return 

def checkVariable():
    if lineContent.startswith("declare"):
        TEMP_words = lineContent.split(" ")
        TEMP_value = lineContent.removeprefix(f"declare {TEMP_words[1]} = ").removesuffix(";")
        if TEMP_value == lineContent:
            variable.set(TEMP_words[1], None)
        if TEMP_words[1] in [*__Keywords__, *functions]:
            nameError(f"You can't name your variable \"{TEMP_words[1]}\" like that.")
        for TEMP_function in functions:
            try:
                if TEMP_value.startswith(TEMP_function):
                    TEMP_args = __getArgs__(TEMP_value, TEMP_function)
                    try:
                        TEMP_value = __fire__(TEMP_function, TEMP_args)
                        variable.set(TEMP_words[1], checkDataType(TEMP_value))
                    except TypeError:
                        syntaxError("Missing a argument.")
            except AttributeError:
                variable.set(TEMP_words[1], checkDataType(TEMP_value))

def checkModule():
    functions = VariableHandler.get("functions")
    if lineContent.startswith("with"):
        TEMP_words = lineContent.split(" ")
        TEMP_module = TEMP_words[1]
        try:
            exec(f"{TEMP_module}()")
        except TypeError:
            moduleError(f"The module \"{TEMP_module}\" doesn't exist.")
        except NameError:
            moduleError(f"The module \"{TEMP_module}\" doesn't exist.")
        else:
            for TEMP_i in modules:
                if TEMP_i == TEMP_module:
                    VariableHandler.set("functions", [*functions, *modules[TEMP_i]])
                    __importedModules__[TEMP_i] = modules[TEMP_i]
            for TEMP_functions in modules[TEMP_i]:
                exec(f"globals()[\"{TEMP_functions}\"] = {TEMP_module}().{TEMP_functions}")

def checkComments():
    if str(lineContent).startswith("//"):
        return
    if str(lineContent).startswith("/*"):
        globals()["CODE_longComment"] = True
    if str(lineContent).startswith("*/"):
        globals()["CODE_longComment"] = False

def __lineNumber__() -> int:
    return lineNumber

def GarbageCollection() -> None:
    GC(globals())

@function
def printf(text) -> None:
    return print(text)

@function
def inputf(text) -> None:
    return input(text)

@function
def calc(text) -> Any:
    try:
        eval(text, {}, {})
    except ZeroDivisionError:
        mathError("Divisions by 0 are impossible.")
    return eval(text, {}, {})

@function
def variables() -> Any:
    return variable.globals

@function
def circle(text) -> int:
    return round(text)

@function
def problem(text) -> error:
    return error(text)

@function
def help() -> None:
    print(f"""
Welcome to Potatolang {__Version__}'s help utility!

If this is your first time using Python, you should definitely check out
Good luck, there is no documentattion... for now.

Enter the name of any module, keyword, or topic to get help on writing  
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "stop()".
    """)
    return

@function
def credits() -> None:
    print(f"""
Thanks to CodeSec Community
for supporting the PotatoLang develoment.
    """)

@function
def copyright() -> None:
    for TEMP_i in [["Artic", "2022-today"], ["CodeSec Community", "2022-today"]]:
        print(f"\nCopyright (c) {TEMP_i[1]} {TEMP_i[0]}\nAll Rights Reserved.")
    print(end="\n")
    return

@function
def stop() -> None:
    return sys.exit()

try:
    arguments, values = getopt.getopt(sys.argv[1:], "chmv", ["Console", "Help", "File", "Version"])
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-c", "--Console"):
            print(f"PotatoLang {__Version__}\nType \"help()\", \"copyright()\", \"credits()\"")
            while True:
                exec(input("(base) > "))
        elif currentArgument in ("-h", "--  Help"):
            print("""
usage: python compiler.py [option] ...
options:    
-c --Console    : Run the code in a terminal. (/!\ WIP)
-h --Help       : Display the help message.
-m --File       : Read a file and run the content.
-v --Version    : Display the version.
            """)
        elif currentArgument in ("-m", "--File"):
            if __File__ is None:
                fileError("There's no input file.")
            for lineNumber, lineContent in File(__File__, __Path__):
                lineContent, lineNumber = str(lineContent), int(lineNumber) + 1
                if CODE_isFunction:
                    FunctionHandler.getCode(lineContent)
                elif CODE_longComment:
                    checkComments()
                else:
                    checkComments()
                    checkModule()
                    checkVariable()
                    checkCreateFunction()
                    checkFunctions()
                    GarbageCollection()
        elif currentArgument in ("-v", "--Version"):
            print(__Version__)
except getopt.error as e:
    optionError(f"{e}.")