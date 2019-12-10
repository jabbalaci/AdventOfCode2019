#!/usr/bin/env python3

from helper import Point
from part1 import process_file


def example_1() -> None:
    """
.#..#
.....
#####
....#
...##

with numbers:

.7..7
.....
67775
....7
...87

best location: (3, 4) with 8 other asteroids detected
    """
    point, value = process_file("examples/part1/example1.txt")
    assert(point == Point(3, 4))
    assert(value == 8)
    print("example 1 is OK")


def example_3() -> None:
    """
    Best is (5, 8) with 33 other asteroids detected.
    """
    point, value = process_file("examples/part1/example3.txt")
    assert(point == Point(5, 8))
    assert(value == 33)
    print("example 3 is OK")


def example_4() -> None:
    """
    Best is (1, 2) with 35 other asteroids detected.
    """
    point, value = process_file("examples/part1/example4.txt")
    assert(point == Point(1, 2))
    assert(value == 35)
    print("example 4 is OK")


def example_5() -> None:
    """
    Best is (6, 3) with 41 other asteroids detected.
    """
    point, value = process_file("examples/part1/example5.txt")
    assert(point == Point(6, 3))
    assert(value == 41)
    print("example 5 is OK")


def example_6() -> None:
    """
    Best is (11, 13) with 210 other asteroids detected.
    """
    point, value = process_file("examples/part1/example6.txt")
    assert(point == Point(11, 13))
    assert(value == 210)
    print("example 6 is OK")


def main():
    example_1()
    example_3()
    example_4()
    example_5()
    example_6()

##############################################################################

if __name__ == "__main__":
    main()
