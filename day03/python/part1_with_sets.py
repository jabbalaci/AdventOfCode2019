#!/usr/bin/env python3

# This is an OLD version, but I leave it here for references.
# It works well though, it gives the good result.
#
# This is the first version of Part 1.
# Here I used sets. However, after reading Part 2,
# I saw that in Part 2 it'd be better to use dictionaries.
# Since Part 1 can also be solved with dictionaries,
# I decided to rewrite Part 1 with dictionaries and then
# it'd be easier to extend this new version for Part 2.

import helper


class ShouldNeverGetHere(Exception):
    pass


class Grid:
    def __init__(self, line1, line2):
        self.wire1 = line1.split(',')
        self.wire2 = line2.split(',')

    def debug(self):
        print(self.wire1)
        print(self.wire2)

    def follow_wire(self, wire):
        coordinates = set()
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
                coordinates.add((x, y))
            # endfor
        # endfor
        return coordinates

    def follow_wires(self):
        self.wire1_path = self.follow_wire(self.wire1)
        self.wire2_path = self.follow_wire(self.wire2)

    def debug2(self):
        print(self.wire1_path)
        print(self.wire2_path)

    def find_closest_intersection(self):
        crosses = self.wire1_path.intersection(self.wire2_path)
        closest = min(crosses, key=lambda t: abs(t[0]) + abs(t[1]))
        result = sum(abs(val) for val in closest)
        return result


def main():
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
