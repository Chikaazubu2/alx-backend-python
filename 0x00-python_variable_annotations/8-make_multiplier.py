#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float my multiplier"""
    def retfunc(x: float) -> float:
        """multiplis a float by multiplier"""
        return multiplier * x
    return retfunc
