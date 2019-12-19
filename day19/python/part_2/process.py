#!/usr/bin/env python3

INPUT = "p2.txt"


def print_header(size: int) -> None:
    text = f"""
P1
# AoC 2019, Day 19, Part 2
{size} {size}
""".strip()
    print(text)


def main() -> None:
    with open(INPUT) as f:
        lines = f.read().splitlines()

    size = len(lines[0])

    print_header(size)

    for line in lines:
        pixels = list(line)
        print(" ".join(pixels))

##############################################################################

if __name__ == "__main__":
    main()
