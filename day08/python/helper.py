from itertools import zip_longest
from typing import List


def read_lines(fname: str) -> List[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()


def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks:
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx

    (from Peter Norvig's pytudes)
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
