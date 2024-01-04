#!/usr/bin/env python3
""" complex types function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function """
    def that_multi(x: float) -> float:
        """ function """
        return x * multiplier
    return that_multi
