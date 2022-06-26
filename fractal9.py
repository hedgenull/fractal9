"""Fractal9 Interpreter"""
import inspect
import os
import re
import time
from math import *


def main(filename: str) -> None:
    """Run a code file.

    Args:
        filename (string): File to run.
    """
    with open(filename, "r") as source:
        code = source.read()
        interpret(code)


def interpret(code: str) -> None:
    """Interpret Fractal code.

    Args:
        code (str): Source code to interpret.
    """

    for c in code.split():
        if c.isdigit():
            c = int(c)
            args.append(c)
        elif c in commands.keys():
            f = commands[c][0]
            if len(args) < (argc := len(inspect.signature(f).parameters)):
                print("error: not enough arguments")
            else:
                try:
                    funargs = [args.pop() for arg in range(argc)]
                    funargs.reverse()
                    res = f(*funargs)
                except TypeError as e:
                    print("error: wrong types")
                else:
                    if res is not None:
                        args.append(res)
        else:
            args.append(c)


def swap_two():
    """swap top two elements on stack"""
    args[-2], args[-1] = args[-1], args[-2]


def swap_three():
    """swap top three elements on stack"""
    args[-3], args[-2], args[-1] = args[-1], args[-2], args[-3]


def get_numerical_input(prompt: str = ""):
    """get input as integer"""
    i = input(prompt)

    if i.isdigit():
        return int(i)
    return ord(i[0])


def f9_help():
    """show the command help"""
    for k, v in commands.items():
        print(f"{k} -> {v[1]}")


commands = {
    # STRING
    "~": ((lambda x, y, z: x.replace(y, z)), "replace in string"),  # String replacement
    "〟": ((lambda x: x.lower()), "convert to lowercase"),  # Lowercase conversion
    "〞": ((lambda x: x.upper()), "convert to uppercase"),  # Uppercase conversion
    "⸮": ((lambda x: x.title()), "convert to titlecase"),  # Titlecase conversion
    "@": (
        (lambda x: ord(x) if type(x) == str else x),
        "ordinal of string",
    ),  # Ordinal of string
    "#": (
        (lambda x: len(x) if type(x) == str else x),
        "length of string",
    ),  # Length of string
    "Δ": (
        (lambda x, y: int(bool(re.match(x, y)))),
        "match regular expression",
    ),  # Regex matching
    "⩪": ((lambda x: str(x)), "convert to string"),  # Convert to string
    # SYSTEM
    "$": ((lambda x: os.system(x)), "execute system command"),  # Execute system command
    "…": ((lambda x: time.sleep(x)), "sleep (in seconds)"),  # Sleep
    ".": ((lambda: exit()), "exit program"),  # Quit program
    # I/O
    "≻": (
        (lambda x: print(x) if type(x) == int else print(ord(x))),
        "print as number",
    ),  # Print number(s)
    "≽": (
        (lambda x: print(chr(x)) if type(x) == int else print(x)),
        "print as string",
    ),  # Print character(s)
    "≺": (get_numerical_input, get_numerical_input.__doc__),  # Get input (integer)
    "≼": (input(), "get input as string"),  # Get input (string)
    # STACK
    '"': ((lambda: print(*args)), "print stack"),  # Print stack
    "⮄": (swap_two, swap_two.__doc__),  # Swap two top elements
    "⬱": (swap_three, swap_three.__doc__),  # Swap three top elements
    "↔": ((lambda: args.reverse()), "reverse stack"),  # Reverse stack
    ",": (
        (lambda: args[0]),
        "copy bottom element to top of stack",
    ),  # Copy bottom element to top
    ":": (
        (lambda: args[-2]),
        "copy second element to top of stack",
    ),  # Copy second-to-top element to top
    ";": (
        (lambda: args[-3]),
        "copy third element to top of stack",
    ),  # Copy third-to-top element to top
    # MATH
    "+": ((lambda x, y: x + y), "addition operator"),  # Addition
    "-": ((lambda x, y: x - y), "subtraction operator"),  # Subtraction
    "×": ((lambda x, y: x * y), "multiplication operator"),  # Multiplication
    "÷": ((lambda x, y: x / y), "division operator"),  # Division
    "%": ((lambda x, y: x % y), "modulo operator"),  # Modulus
    "^": ((lambda x, y: x**y), "exponentiation"),  # Exponentiation
    "√": ((lambda x: sqrt(x)), "square root"),  # Square root
    "²": ((lambda x: x**2), "square"),  # Square
    "³": ((lambda x: x**3), "cube"),  # Cube
    "⁴": ((lambda x: x**4), "fourth power"),  # Fourth power
    "⁵": ((lambda x: x**5), "fifth power"),  # Fifth power
    "⁶": ((lambda x: x**6), "sixth power"),  # Sixth power
    "⁷": ((lambda x: x**7), "seventh power"),  # Seventh power
    "⁸": ((lambda x: x**8), "eighth power"),  # Eighth power
    "⁹": ((lambda x: x**9), "ninth power"),  # Ninth power
    # LOGCIAL/COMPARISON
    "&": ((lambda x, y: int(x and y)), "logical and"),  # Logical and
    "|": ((lambda x, y: int(x or y)), "logical or"),  # Logical or
    "⊻": ((lambda x, y: int(bool(x) != bool(y))), "logical xor"),  # Logical xor
    "¬": ((lambda x: int(not x)), "logical not"),  # Logical not
    "=": ((lambda x, y: int(x == y)), "equal to"),  # Logical equals
    "≠": ((lambda x, y: int(x != y)), "not equal to"),  # Logical not-equals
    "<": ((lambda x, y: int(x < y)), "less than"),  # Less than
    ">": ((lambda x, y: int(x > y)), "greater than"),  # Greater than
    "≤": ((lambda x, y: int(x <= y)), "less than or equal to"),  # Less than or equal to
    "≥": (
        (lambda x, y: int(x >= y)),
        "greater than or equal to",
    ),  # Greater than or equal to
    "≬": ((lambda x, y, z: int(z < x < y or y < x < z)), "between operator"),  # Between
    "≡": ((lambda x, y: type(x) == type(y)), "same types"),  # Logical equals, types
    "≢": (
        (lambda x, y: type(x) != type(y)),
        "different types",
    ),  # Logical not-equals, types
    "∈": ((lambda x, y: int(x in y)), "element of"),  # Element of
    "∉": ((lambda x, y: int(x not in y)), "not element of"),  # Not element of
    # OTHER MATH
    "µ": ((lambda x, y: min(x, y)), "minimum"),  # Minimum
    "γ": ((lambda x, y: max(x, y)), "maximum"),  # Maximum
    "⅟": ((lambda x: 1 / x), "-1 exponentiation"),  # -1 exponentiation
    "δ": ((lambda x, y: (x + y) / 2), "mean average"),  # Mean average
    "λ": ((lambda x, y: [x, y]), "package"),  # Construct tuple
    "θ": ((lambda x: (pi * x) ** 2), "area of circle (w. radius)"),  # Area of circle
    "∑": ((lambda x: sum(x)), "sum"),  # Sum
    "「": ((lambda x: floor(x)), "floor"),  # Floor
    "」": ((lambda x: ceil(x)), "ceiling"),  # Ceiling
    # LITERALS
    "½": ((lambda: 0.5), "literal 1/2"),  # Literal 1/2
    "⅓": ((lambda: 1 / 3), "literal 1/3"),  # Literal 1/3
    "⅔": ((lambda: 2 / 3), "literal 2/3"),  # Literal 2/3
    "¼": ((lambda: 0.25), "literal 1/4"),  # Literal 1/4
    "¾": ((lambda: 0.75), "literal 3/4"),  # Literal 3/4
    "⅕": ((lambda: 0.2), "literal 1/5"),  # Literal 1/5
    "⅖": ((lambda: 0.4), "literal 2/5"),  # Literal 2/5
    "⅗": ((lambda: 0.6), "literal 3/5"),  # Literal 3/5
    "⅘": ((lambda: 0.8), "literal 4/5"),  # Literal 4/5
    "⅙": ((lambda: 1 / 6), "literal 1/6"),  # Literal 1/6
    "⅚": ((lambda: 5 / 6), "literal 5/6"),  # Literal 5/6
    "⅐": ((lambda: 1 / 7), "literal 1/7"),  # Literal 1/7
    "⅛": ((lambda: 0.125), "literal 1/8"),  # Literal 1/8
    "⅜": ((lambda: 0.375), "literal 3/8"),  # Literal 3/8
    "⅝": ((lambda: 0.625), "literal 5/8"),  # Literal 5/8
    "⅞": ((lambda: 0.875), "literal 7/8"),  # Literal 7/8
    "⅑": ((lambda: 1 / 9), "literal 1/9"),  # Literal 1/9
    "⅒": ((lambda: 0.1), "literal 1/10"),  # Literal 1/10
    "π": ((lambda: pi), "literal pi"),  # Literal π (pi)
    "ϕ": ((lambda: (1 + 5**0.5) / 2), "literal phi"),  # Literal ϕ (golden ratio)
    "τ": ((lambda: tau), "literal tau"),  # Literal tau (2 times pi)
    "ε": ((lambda: e), "literal e"),  # Literal e (Euler's number)
    "∞": ((lambda: inf), "literal infinity"),  # Literal infinity
    "∘": ((lambda: " "), "literal space character (' ')"),  # Literal space character
    # OTHER
    "∅": ((lambda x: int(len(x) == 0)), "empty collection"),  # Empty collection
    "∩": ((lambda x: x[0]), "first element"),  # First element
    "∪": ((lambda x: x[-1]), "last element"),  # Last element
    "?": (f9_help, f9_help.__doc__),
}

args = []


if __name__ == "__main__":
    while True:
        interpret(input("fractal9 > "))
