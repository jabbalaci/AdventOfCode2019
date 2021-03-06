#!/usr/bin/env python3

import helper


def fuel(mass: int) -> int:
    return (mass // 3) - 2


def main() -> None:
    lines = helper.read_lines("input.txt")
    result = sum(fuel(int(line)) for line in lines)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
