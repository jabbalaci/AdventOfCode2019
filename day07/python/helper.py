from typing import List, Tuple
from lib import permutation as perm


def read_lines(fname: str) -> List[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()


def get_all_permutations(sequence: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    result = []
    #
    li = list(sequence)    # mutable copy
    result.append(tuple(li))
    while perm.lexicographically_next_permutation(li):
        result.append(tuple(li))
    #
    return result
