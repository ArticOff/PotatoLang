import sys

__variables__ = {}

def _print(line: str, contents: str):
    print_statement = line.split("\n")[0].replace("print", "").replace(";", "").replace("(", "").replace(")", "")
    if print_statement[0] == '"' or print_statement[0] == "'":
        print_statement = print_statement[1:]
    if print_statement[-1] == '"' or print_statement[-1] == "'":
        print_statement = print_statement[:-1]
        print(print_statement)
    else:
        for variable in __variables__:
            if f'${variable}' == print_statement:
                print(__variables__[variable])
                break
            line_number = contents.split("\n").index(line)
            return print(f"SyntaxError: Missing dollar sign in line {line_number + 1}")

def _id(line: str, contents: str):
    print_statement = line.split("\n")[0].replace("id", "").replace(";", "").replace("(", "").replace(")", "")
    for variable in __variables__:
        if f'${variable}' == print_statement:
            return print(id(variable))
        elif print_statement.startswith("$"):
            line_number = contents.split("\n").index(line)
            name = line.split("\n")[0].split("(")[0]
            print(f"NameError: The name {name} is not defined in line {line_number + 1}")
            return sys.exit(1)
        else:
            line_number = contents.split("\n").index(line)
            return print(f"SyntaxError: Missing dollar sign in line {line_number + 1}")

def _condition(line: str, contents: str):
    if "if" in line:
        if "(" in line:
            if ")" in line:
                value = line.split("\n")[0].split("(")[1].split(")")[0]
                if value == True:
                    # get all lines with a tab in front of them and after the if
                    lines = []
                    for line in contents.split("\n"):
                        if line.startswith("\t"):
                            lines.append(line)
                    for line in lines:
                        if "else" in line:
                            return
                        print('a')
                else:
                    return False
            else:
                line_number = contents.split("\n").index(line)
                print(f"SyntaxError: Unbalanced parentheses in line {line_number + 1}")
                sys.exit(1)


file = sys.argv[1]
with open(file, "r") as f:
    contents = f.read()
    for line in contents.split("\n")[:]:
        if ";" in line:
            if "=" in line:
                    variables = line.split("\n")[0]
                    var_value = variables[variables.index("=") + 1 :].removesuffix(";").replace(" ", "", 1).replace('"', "")
                    var_name = variables[:variables.index("=")].removesuffix(";").replace(" ", "")
                    __variables__[var_name] = var_value
            elif "print" in line:
                if line.count("\"") % 2 == 0:
                    _print(line, contents)
                elif line.count("\"") % 4 == 0:
                    _print(line, contents)
                elif line.count("\"") % 6 == 0:
                    _print(line, contents)
                elif line.count("\"") % 8 == 0:
                    _print(line, contents)
                elif line.count("\"") == 0:
                    _print(line, contents)
                else:
                    line_number = contents.split("\n").index(line)
                    print(f"SyntaxError: Unbalanced quotes in line {line_number + 1}")
                    sys.exit(1)
            elif "id" in line:
                _id(line, contents)
            else:
                if "(" in line:
                    if ")" in line:
                        line_number = contents.split("\n").index(line)
                        method = line.split("\n")[0].split("(")[0]
                        print(f"UnknownMethod: The method {method} is unknown in line {line_number + 1}")
                        sys.exit(1)
                    else:
                        line_number = contents.split("\n").index(line)
                        print(f"SyntaxError: Unbalanced parentheses in line {line_number + 1}")
                        sys.exit(1)
                else:
                    line_number = contents.split("\n").index(line)
                    name = line.split("\n")[0].split("(")[0]
                    print(f"NameError: The name {name} is not defined in line {line_number + 1}")
                    sys.exit(1)
        elif ":" in line:
            _condition(line, contents)
                
        else:
            if line.startswith("#"):
                continue
            elif line == "":
                continue
            else:
                line_number = contents.split("\n").index(line)
                print(f"SyntaxError: Missing semicolons in line {line_number + 1}")
                sys.exit(1)