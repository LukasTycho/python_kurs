"""module example
Author: Lukas Mendelsohn

This module contains three functions. Its only use is to be an example of what a module might look like.

Functions:
hello_world(): prints "Hello World"
wuerfel(): rolls a six sided dice
summe(): calculates the sum of all args
"""

import random


def hello_world():
    """Print 'Hello World!'"""
    print("Hello World!")
    return None


def wuerfel():
    """Roll a digital dice.
    Returns a random value between 1 and 6.
    """
    return random.randint(1, 6)


def summe(*args):
    """Calculate the sum of all arguments."""
    return sum(args)