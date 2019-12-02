#!/usr/bin/env python3

from typing import List

import helper


def process(numbers: List[int]) -> List[int]:
    data = numbers[:]
    idx = 0
    opcode = data[idx]
    while opcode != 99:
        if opcode == 1:
            inp1 = data[data[idx + 1]]
            inp2 = data[data[idx + 2]]
            data[data[idx + 3]] = inp1 + inp2
        elif opcode == 2:
            inp1 = data[data[idx + 1]]
            inp2 = data[data[idx + 2]]
            data[data[idx + 3]] = inp1 * inp2
        # endif
        idx += 4
        opcode = data[idx]
    # endwhile
    return data


def main() -> None:
    # test cases:
    # line = "1,9,10,3,2,3,11,0,99,30,40,50"
    # line = "1,0,0,0,99"
    # line = "2,3,0,3,99"
    # line = "2,4,4,5,99,0"
    # line = "1,1,1,4,99,5,6,0,99"

    line = helper.read_lines("input.txt")[0]
    numbers = [int(n) for n in line.split(",")]
    numbers[1] = 12
    numbers[2] = 2

    print("before:")
    print(numbers)
    numbers = process(numbers)
    print()
    print("after:")
    print(numbers)

##############################################################################

if __name__ == "__main__":
    main()
