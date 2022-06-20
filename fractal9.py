"""Fractal9 Interpreter"""
import inspect
import os
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
            f = commands[c]
            if len(args) < (argc := len(inspect.signature(f).parameters)):
                print("error: not enough arguments")
            else:
                res = f(*[args.pop() for i in range(argc)])
                if res is not None:
                    args.append(res)
        else:
            args.append(c)


def swap_two():
    """Swap the top two elements on the stack."""
    args[-2], args[-1] = args[-1], args[-2]


def swap_three():
    """Swap the top three elements on the stack."""
    args[-3], args[-2], args[-1] = args[-1], args[-2], args[-3]


def get_input(prompt: str):
    """Get input- numerical if possible

    Args:
        prompt (str): Prompt for input

    Returns:
        str | int: input gathered
    """
    i = input(prompt)
    if i.isdigit():
        return int(i)
    return i


commands = {
    # STRING
    "~": (lambda x, y, z: x.replace(y, z)),
    "@": (lambda x: ord(x) if type(x) == str else x),  # Ordinal of string
    "#": (lambda x: len(x) if type(x) != int else x),  # Length of string
    # SYSTEM
    "$": (lambda x: os.system(x)),  # Execute system command
    "…": (lambda x: time.sleep(x)),  # Sleep
    ".": (lambda: exit()),  # Quit program
    # I/O
    "`": (
        lambda x: print(chr(x)) if type(x) == int else print(x)
    ),  # Print character(s)
    "'": (lambda x: print(x) if type(x) == int else print(ord(x))),  # Print number(s)
    "«": get_input,
    # STACK
    '"': (lambda: print(" ".join([str(arg) for arg in args]))),  # Print stack
    "⮄": swap_two,  # Swap two top elements
    "⬱": swap_three,  # Swap three top elements
    "↔": (lambda: args.reverse()),  # Reverse stack
    ",": (lambda: args[0]),  # Copy bottom element to top
    ":": (lambda: args[-2]),  # Copy second-to-top element to top
    ";": (lambda: args[-3]),  # Copy third-to-top element to top
    # MATH
    "+": (lambda x, y: x + y),  # Addition
    "-": (lambda x, y: x - y),  # Subtraction
    "×": (lambda x, y: x * y),  # Multiplication
    "÷": (lambda x, y: x / y),  # Division
    "%": (lambda x, y: x % y),  # Modulus
    "^": (lambda x, y: x**y),  # Exponentiation
    "√": (lambda x: sqrt(x)),  # Square root
    "²": (lambda x: x**2),  # Square
    "³": (lambda x: x**3),  # Cube
    "⁴": (lambda x: x**4),  # Fourth power
    "⁵": (lambda x: x**5),  # Fifth power
    "⁶": (lambda x: x**6),  # Sixth power
    "⁷": (lambda x: x**7),  # Seventh power
    "⁸": (lambda x: x**8),  # Eighth power
    "⁹": (lambda x: x**9),  # Ninth power
    # LOGCIAL/COMPARISON
    "&": (lambda x, y: int(x and y)),  # Logical and
    "|": (lambda x, y: int(x or y)),  # Logical or
    "⊻": (lambda x, y: int(bool(x) != bool(y))),  # Logical xor
    "¬": (lambda x: int(not x)),  # Logical not
    "=": (lambda x, y: int(x == y)),  # Logical equals
    "≠": (lambda x, y: int(x != y)),  # Logical not-equals
    "<": (lambda x, y: int(x < y)),  # Less than
    ">": (lambda x, y: int(x > y)),  # Greater than
    "≤": (lambda x, y: int(x <= y)),  # Less than or equal to
    "≥": (lambda x, y: int(x >= y)),  # Greater than or equal to
    "≬": (lambda x, y, z: int(z < x < y or y < x < z)),  # Between
    "≡": (lambda x, y: type(x) == type(y)),  # Lpgical equals, types
    "≢": (lambda x, y: type(x) != type(y)),  # Logical not-equals, types
    "∈": (lambda x, y: int(x in y)),  # Element of
    "∉": (lambda x, y: int(x not in y)),  # Not element of
    # OTHER MATH
    "µ": (lambda x, y: min(x, y)),  # Minimum
    "γ": (lambda x, y: max(x, y)),  # Maximum
    "⅟": (lambda x: 1 / x),  # -1 exponentiation
    "δ": (lambda x, y: (x + y) / 2),  # Mean average
    "λ": (lambda x, y: [x, y]),  # Construct tuple
    "θ": (lambda x: (pi * x) ** 2),  # Area of circle
    "∑": (lambda x: sum(x)),  # Sum
    "「": (lambda x: floor(x)),  # Floor
    "」": (lambda x: ceil(x)),  # Ceiling
    # LITERALS
    "½": (lambda: 0.5),  # Literal 1/2
    "⅓": (lambda: 1 / 3),  # Literal 1/3
    "⅔": (lambda: 2 / 3),  # Literal 2/3
    "¼": (lambda: 0.25),  # Literal 1/4
    "¾": (lambda: 0.75),  # Literal 3/4
    "⅕": (lambda: 0.2),  # Literal 1/5
    "⅖": (lambda: 0.4),  # Literal 2/5
    "⅗": (lambda: 0.6),  # Literal 3/5
    "⅘": (lambda: 0.8),  # Literal 4/5
    "⅙": (lambda: 1 / 6),  # Literal 1/6
    "⅚": (lambda: 5 / 6),  # Literal 5/6
    "⅐": (lambda: 1 / 7),  # Literal 1/7
    "⅛": (lambda: 0.125),  # Literal 1/8
    "⅜": (lambda: 0.375),  # Literal 3/8
    "⅝": (lambda: 0.625),  # Literal 5/8
    "⅞": (lambda: 0.875),  # Literal 7/8
    "⅑": (lambda: 1 / 9),  # Literal 1/9
    "⅒": (lambda: 0.1),  # Literal 1/10
    "π": (lambda: pi),  # Literal π (pi)
    "ϕ": (lambda: (1 + 5**0.5) / 2),  # Literal ϕ (golden ratio)
    "τ": (lambda: tau),  # Literal tau (2 times pi)
    "ε": (lambda: e),  # Literal e (Euler's number)
    "∞": (lambda: inf),  # Literal infinity
    # OTHER
    "∩": (lambda x: x[0]),  # First element
    "∪": (lambda x: x[-1]),  # Last element
}

args = []


if __name__ == "__main__":
    while True:
        interpret(input("fractal9 > "))
