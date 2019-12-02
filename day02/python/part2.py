#!/usr/bin/env python3

from typing import List

import helper

GOAL = 19690720


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
    line = helper.read_lines("input.txt")[0]
    numbers = [int(n) for n in line.split(",")]
    terminate = False

    for i in range(0, 99+1):
        for j in range(0, 99+1):
            numbers[1] = i
            numbers[2] = j
            print(f"# i = {i}, j = {j}")
            result = process(numbers)
            if result[0] == GOAL:
                print("i =", i)
                print("j =", j)
                print("answer:", 100 * i + j)
                terminate = True
                break
            # endif
        # endfor
        if terminate:
            break
    # endfor
    print("__END__")

##############################################################################

if __name__ == "__main__":
    main()
