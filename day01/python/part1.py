#!/usr/bin/env python3

from typing import List


def read_lines(fname: str) -> List[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()


def fuel(mass: int) -> int:
    return (mass // 3) - 2


def main():
    lines = read_lines("input.txt")
    result = sum(fuel(int(line)) for line in lines)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
