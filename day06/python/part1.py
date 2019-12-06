#!/usr/bin/env python3

"""
It must work even if COM is not in the first line.
`input.txt` is like that, so I took the example
and randomized its lines to make the example
similar to the real input.
"""

import helper

from typing import Dict, List


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    full: Dict[str, List[str]] = {}
    orbits: Dict[str, int] = {
        'COM': 0    # init.
    }
    for line in lines:
        left, right = line.split(')')
        if left not in full:
            full[left] = []
        full[left].append(right)

    while len(full) > 0:
        for k in full:
            if k in orbits:
                orbit_value = orbits[k]
                reachable = full[k]
                for obj in reachable:
                    orbits[obj] = orbit_value + 1
                del full[k]
                break
            #
        #
    #
    result = sum(orbits.values())
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
