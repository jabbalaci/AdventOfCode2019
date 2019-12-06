#!/usr/bin/env python3

import helper

from typing import Dict, List, Set


def find_path(d: Dict[str, str], src: str, dest: str) -> List[str]:
    path = []
    key = src
    while True:
        value = d[key]
        path.append(value)
        if value == dest:
            break
        key = value
    #
    return path[::-1]


def main() -> None:
    # lines = helper.read_lines("example2.txt")
    lines = helper.read_lines("input.txt")

    child_parent: Dict[str, str] = {}
    for line in lines:
        left, right = line.split(')')
        child_parent[right] = left

    p1 = find_path(child_parent, 'YOU', 'COM')
    # print(p1)
    p2 = find_path(child_parent, 'SAN', 'COM')
    # print(p2)

    p1_set: Set[str] = set(p1)
    p2_set: Set[str] = set(p2)
    diff1 = len(p1_set.difference(p2_set))
    diff2 = len(p2_set.difference(p1_set))
    result = diff1 + diff2
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
