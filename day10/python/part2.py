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
    def __init__(self, fname: str) -> None:
        """
        constructor
        """
        lines = helper.read_lines(fname)
        self.lines: Tuple[str, ...] = tuple(lines)    # make it immutable
        self.rows = len(self.lines)
        self.columns = len(self.lines[0])
        self.points: Tuple[Point, ...] = self.collect_asteroids()
        self.max_point = Point(0, 0)    # will be set later

    def print_map(self) -> None:
        """
        for debugging
        """
        for line in self.lines:
            print(line)
        print("rows: {}, columns: {}".format(self.rows, self.columns))

    def collect_asteroids(self) -> Tuple[Point, ...]:
        """
        collect asteroids on the map and return them as a tuple of points
        """
        li = []
        for i in range(self.rows):
            for j in range(self.columns):
                if self.lines[i][j] != '.':
                    li.append(Point(x=j, y=i))
            #
        #
        return tuple(li)

    def get_angle_between(self, p1: Point, p2: Point) -> float:
        """
        Get the angle between two points. p1 is the current point
        and we imagine a horizontal line that goes through p1.
        The second line goes through p1 and p2.
        What is the angle between the two lines?

        For the first (horizontal) line, we create a new point
        just next to p1.
        """
        p3 = Point(x=p1.x + 1, y=p1.y)    # the point next to p1
        return helper.angle(p3, p1, p2)

    def find_visible_asteroids_from(self, curr: Point) -> Dict[float, List[Point]]:
        """
        From a given point (curr), scan the whole map and build a dictionary
        where the key is an angle and the value is a list of points that are
        in this angle from the current point. That is, asteroids that are
        in the same direction are collected in a list.
        """
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

    def find_max_point(self) -> Tuple[Point, int]:
        """
        Return the point that can monitor the largest number of asteroids.
        """
        visibility: Dict[Point, int] = {}    # key: point, value: number of visible points
        for curr in self.points:
            d = self.find_visible_asteroids_from(curr)
            visibility[curr] = len(d)
        #
        # pprint(visibility)
        maxi = max(visibility.items(), key=lambda t: t[1])
        # print()
        return maxi

    def sort_values_of(self, d: Dict[float, List[Point]]) -> Dict[float, List[Point]]:
        """
        We have a dictionary, where the key is an angle and
        the values are points that are in that angle.
        The values are in a list. Sort this list in ascending order
        by the distances of the points from the laser station.
        The point that is closest to the station becomes the first, etc.
        """
        #
        def my_func(p: Point) -> int:
            """we use Manhattan distance"""
            return abs(self.max_point.x - p.x) + abs(self.max_point.y - p.y)

        copy: Dict[float, List[Point]] = {}
        for angle, points in d.items():
            copy[angle] = sorted(points, key=my_func)
        #
        return copy

    def get_sorted_angles(self, d: Dict[float, List[Point]]) -> List[float]:
        """
        Sort the angles. However, angle 270 must be the first since points
        that are just above the laser station are in this direction.
        """
        li: List[float] = sorted(d.keys())
        idx = li.index(270.0)
        return li[idx:] + li[:idx]    # starts with 270 degrees, which is right above the self.max_point

    def debug(self, target: Point) -> None:
        print(target)
        input("Press ENTER to continue...")

    def start_shooting(self) -> None:
        """
        Start the laser station and start shooting the asteroids in
        clockwise direction, starting with the point that is just above
        the station.
        """
        visibles = self.find_visible_asteroids_from(self.max_point)
        d = self.sort_values_of(visibles)    # a copy that we'll consume
        # pprint(d)
        # print()
        ordered_angles = self.get_sorted_angles(d)
        # print(ordered_angles)
        # print()

        cnt = 0
        while True:
            if not d:    # if empty
                break
            #
            for angle in ordered_angles:
                li = d.get(angle, [])
                if len(li) > 0:    # not empty
                    target = li.pop(0)    # take it out of the list
                    cnt += 1
                    # self.debug(target)
                    if cnt == 200:
                        print("{}) {}".format(cnt, target))
                        result = target.x * 100 + target.y
                        print("result:", result)
                if len(li) == 0:    # empty
                    if angle in d:
                        del d[angle]    # if the list is empty, remove the key too
            #
        #

    def start(self) -> None:
        """
        Controller method.
        """
        max_point, value = self.find_max_point()
        self.max_point = max_point    # laser station
        # print(max_point, value)
        # print()
        self.start_shooting()

# endclass


def main() -> None:
    # am = AsteroidsMap("examples/part2/example1.txt")
    # am = AsteroidsMap("examples/part1/example6.txt")
    am = AsteroidsMap("input.txt")
    am.start()

##############################################################################

if __name__ == "__main__":
    main()
