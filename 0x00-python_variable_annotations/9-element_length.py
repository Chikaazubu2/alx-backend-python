#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """I it walks likea a duck and it quacks like a duck
     then it must be a duck"""
    return [(i, len(i)) for i in lst]
