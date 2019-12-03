#!/usr/bin/env python3

import helper

from typing import Dict, List, Tuple


class ShouldNeverGetHere(Exception):
    pass


class Grid:
    def __init__(self, line1: str, line2: str) -> None:
        self.wire1 = line1.split(',')
        self.wire2 = line2.split(',')

    def debug(self) -> None:
        print(self.wire1)
        print(self.wire2)

    def follow_wire(self, wire: List[str]) -> Dict[Tuple[int, int], int]:
        coordinates: Dict[Tuple[int, int], int] = {}
        x, y = 0, 0    # origo, central port
        path_length = 0
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
                #
                path_length += 1
                #
                if (x, y) not in coordinates:
                    coordinates[(x, y)] = path_length
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
        def my_func(point):
            val1 = self.wire1_path[point]
            val2 = self.wire2_path[point]
            return val1 + val2

        wire1_path_as_set = set(self.wire1_path.keys())
        wire2_path_as_set = set(self.wire2_path.keys())
        crosses = wire1_path_as_set.intersection(wire2_path_as_set)
        closest = min(crosses, key=my_func)
        result = self.wire1_path[closest] + self.wire2_path[closest]
        return result


def main() -> None:
    # fname = "examples/part2/example1.txt"
    # fname = "examples/part2/example2.txt"
    # fname = "examples/part2/example3.txt"
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
