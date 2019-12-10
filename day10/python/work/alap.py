#!/usr/bin/env python3

"""
Find the Angle between three points from 2D using python

https://medium.com/@manivannan_data/find-the-angle-between-three-points-from-2d-using-python-348c513e2cd
"""

import math
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def angle(a: Point, b: Point, c: Point):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return abs(ang)
    # return ang + 360 if ang < 0 else ang


def main():
    a = Point(1, 1)
    b = Point(3, 1)
    c = Point(3, 3)
    d = Point(6, 1)
    print(angle(a, b, c))
    print(angle(c, a, b))
    print(angle(b, c, a))
    print(angle(a, b, d))

##############################################################################

if __name__ == "__main__":
    main()
