#!/usr/bin/env python3

import helper


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


def main() -> None:
    lines = helper.read_lines("input.txt")
    result = sum(extra_fuel(int(line)) for line in lines)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
