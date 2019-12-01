#!/usr/bin/env python3

from typing import List


def read_lines(fname: str) -> List[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()


def fuel(mass: int) -> int:
    return (mass // 3) - 2


def extra_fuel(mass: int) -> int:
    value = mass
    total = 0

    while value > 0:
        value = fuel(value)
        if value > 0:
            total += value
    #
    return total


def main():
    lines = read_lines("input.txt")
    result = sum(extra_fuel(int(line)) for line in lines)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
