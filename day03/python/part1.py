#!/usr/bin/env python3

# This is the second version of Part 1.
# Here I use dictionaries.
# For Part 2, I extended this version.

import helper

from typing import Any, Dict, List, Tuple


class ShouldNeverGetHere(Exception):
    pass


class Grid:
    def __init__(self, line1: str, line2: str) -> None:
        self.wire1: List[str] = line1.split(',')
        self.wire2: List[str] = line2.split(',')

    def debug(self) -> None:
        print(self.wire1)
        print(self.wire2)

    def follow_wire(self, wire: List[str]) -> Dict[Tuple[int, int], Any]:
        coordinates: Dict[Tuple[int, int], Any] = {}
        x, y = 0, 0    # origo, central port
        for instruction in wire:
            direction = instruction[0]
            steps = int(instruction[1:])
            for _ in range(steps):
                if direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                else:
                    raise ShouldNeverGetHere()
                coordinates[(x, y)] = None    # the value doesn't matter; we use a dummy value
            # endfor
        # endfor
        return coordinates

    def follow_wires(self) -> None:
        self.wire1_path = self.follow_wire(self.wire1)
        self.wire2_path = self.follow_wire(self.wire2)

    def debug2(self) -> None:
        print(self.wire1_path)
        print(self.wire2_path)

    def find_closest_intersection(self) -> int:
        wire1_path_as_set = set(self.wire1_path.keys())
        wire2_path_as_set = set(self.wire2_path.keys())
        crosses = wire1_path_as_set.intersection(wire2_path_as_set)
        closest = min(crosses, key=lambda t: abs(t[0]) + abs(t[1]))
        result = sum(abs(val) for val in closest)
        return result


def main() -> None:
    # fname = "examples/part1/example1.txt"
    # fname = "examples/part1/example2.txt"
    # fname = "examples/part1/example3.txt"
    fname = "input.txt"

    lines = helper.read_lines(fname)
    # for line in lines:
        # print(line)
    #
    grid = Grid(lines[0], lines[1])
    # grid.debug()
    grid.follow_wires()
    # grid.debug2()
    result = grid.find_closest_intersection()
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
