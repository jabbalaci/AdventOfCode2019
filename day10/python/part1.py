#!/usr/bin/env python3

from pprint import pprint
from typing import Dict, List, Tuple

import helper
from helper import Point


##################
## AsteroidsMap ##
##################

class AsteroidsMap:
    #
    def __init__(self, lines: List[str]) -> None:
        self.lines: Tuple[str, ...] = tuple(lines)    # make it immutable
        self.rows = len(self.lines)
        self.columns = len(self.lines[0])
        self.points: Tuple[Point, ...] = self.collect_asteroids()

    def print_map(self) -> None:
        for line in self.lines:
            print(line)
        print("rows: {}, columns: {}".format(self.rows, self.columns))

    def collect_asteroids(self) -> Tuple[Point, ...]:
        li = []
        for i in range(self.rows):
            for j in range(self.columns):
                if self.lines[i][j] != '.':
                    li.append(Point(x=j, y=i))
            #
        #
        return tuple(li)

    def get_angle_between(self, p1: Point, p2: Point) -> float:
        p3 = Point(x=p1.x + 1, y=p1.y)    # the point next to p1
        return helper.angle(p3, p1, p2)

    def find_visible_asteroids_from(self, curr: Point) -> Dict[float, List[Point]]:
        d: Dict[float, List[Point]] = {}
        for p in self.points:
            if curr != p:    # don't compare curr with itself
                angle = self.get_angle_between(curr, p)
                if angle not in d:
                    d[angle] = []
                d[angle].append(p)
            #
        #
        return d
# endclass


def process_file(fname: str) -> Tuple[Point, int]:
    lines = helper.read_lines(fname)
    am = AsteroidsMap(lines)
    # am.print_map()
    asteroids = am.collect_asteroids()
    visibility: Dict[Point, int] = {}    # key: point, value: number of visible points
    for curr in am.points:
        d = am.find_visible_asteroids_from(curr)
        visibility[curr] = len(d)
    #
    # pprint(visibility)
    maxi = max(visibility.items(), key=lambda t: t[1])
    # print()
    return maxi


def main() -> None:
    maxi = process_file("input.txt")
    print(maxi)

##############################################################################

if __name__ == "__main__":
    main()
