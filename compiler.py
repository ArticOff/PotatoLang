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
from PotatoLang.Keywords import Any
from PotatoLang.Variable import Init
from PotatoLang.File import File
from PotatoLang.Function import (
    function,
    functions,
    modules
)
from PotatoLang.Modules import (
    Sys
)
from PotatoLang.Constants import (
    __Keywords__,
    __Version__
)
from PotatoLang.DataTypes import (
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
    optionError
)

Sys()

__globals__ = {}
variable = Init(__globals__)

try:
    __File__ = sys.argv[2]
    __Path__ = f"{os.getcwd()}\{__File__}"
except IndexError:
    __File__ = None
    __Path__ = None

variable.set("__FILE__", String(__File__))
variable.set("__KEYWORDS__", List(__Keywords__))
variable.set("__VERSION__", String(__Version__))
variable.set("__PATH__", String(__Path__))
variable.set("__NAME__", String(__name__))

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
    return (", ".join(TEMP_Data)).replace("\\", "\\\\")

def __fire__(function: str, args: str) -> str:
    TEMP_Data = {}
    exec(f"TEMP_value = {function}(\"{args}\")", {f"{function}": function}, TEMP_Data)
    return TEMP_Data["TEMP_value"]

def checkVariable(line: str):
    if line.startswith("declare"):
        TEMP_words = line.split(" ")
        TEMP_value = line.removeprefix(f"declare {TEMP_words[1]} = ").replace('"', "").removesuffix(";")
        if TEMP_value == line:
            variable.set(TEMP_words[1], None)
        for function in functions:
            if TEMP_value.startswith(function):
                TEMP_args = __getArgs__(TEMP_value, function)
                try:
                    TEMP_value = __fire__(function, TEMP_args)
                    variable.set(TEMP_words[1], TEMP_value)
                except TypeError:
                    syntaxError("Missing the argument \"text\".")

def checkModule():
    if lineContent.startswith("with"):
        TEMP_words = lineContent.split(" ")
        TEMP_module = TEMP_words[1]
        for TEMP_i in modules:
            if TEMP_i == TEMP_module:
                

def checkFunctions():
    for TEMP_function in functions:
        if lineContent.startswith(TEMP_function):
            TEMP_args = __getArgs__(lineContent, TEMP_function)
            try:
                exec(f"{TEMP_function}({TEMP_args})")
            except TypeError:
                syntaxError("Missing a argument.")

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
def stop() -> None:
    return sys.exit()

try:
    arguments, values = getopt.getopt(sys.argv[1:], "chmv", ["Console", "Help", "File", "Version"])
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-c", "--Console"):
            print("WIP")
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
                fatalError("There's no input file.")
            for lineNumber, lineContent in File(__File__, __Path__):
                lineContent, lineNumber = str(lineContent), int(lineNumber) + 1
                checkFunctions()
                checkModule()
                GarbageCollection()
        elif currentArgument in ("-v", "--Version"):
            print(__Version__)
except getopt.error as e:
    raise optionError(f"{e}.")