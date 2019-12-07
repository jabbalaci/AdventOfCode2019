#!/usr/bin/env python3

from typing import Dict, Tuple

import helper
from part1 import Setup


def try_permutation() -> None:
    sequence = (0, 1, 2, 3, 4)
    permutations = helper.get_all_permutations(sequence)

    assert(permutations[-1] == (4, 3, 2, 1, 0))
    assert(len(permutations) == 120)


def run_test1() -> None:
    line = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    program = tuple([int(n) for n in line.split(",")])
    sequence = (4, 3, 2, 1, 0)
#
    setup = Setup(program, sequence)
    setup.run()
    result = setup.get_output()
    print(result)

    assert(result == 43210)


def run_test2() -> None:
    line = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    program = tuple([int(n) for n in line.split(",")])
    sequence = (0, 1, 2, 3, 4)
#
    setup = Setup(program, sequence)
    setup.run()
    result = setup.get_output()
    print(result)

    assert(result == 54321)


def run_test3() -> None:
    line = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
    program = tuple([int(n) for n in line.split(",")])
    sequence = (1, 0, 4, 3, 2)
#
    setup = Setup(program, sequence)
    setup.run()
    result = setup.get_output()
    print(result)

    assert(result == 65210)


def find_solution_for_test3() -> None:
    line = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
    program = tuple([int(n) for n in line.split(",")])

    permutations = helper.get_all_permutations((0, 1, 2, 3, 4))
    d: Dict[Tuple[int, ...], int] = {}    # sequence -> output_value
    for seq in permutations:
        setup = Setup(program, seq)
        setup.run()
        result = setup.get_output()
        d[seq] = result
    #
    maxi = max(d.items(), key=lambda t: t[1])
    print(maxi)

    assert(maxi[0] == (1, 0, 4, 3, 2))
    assert(maxi[1] == 65210)


def main() -> None:
    try_permutation()
    run_test1()
    run_test2()
    run_test3()
    find_solution_for_test3()

##############################################################################

if __name__ == "__main__":
    main()
