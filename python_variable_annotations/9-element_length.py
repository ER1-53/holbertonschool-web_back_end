#!/usr/bin/env python3
""" Annotate the values """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function """
    return [(i, len(i)) for i in lst]
