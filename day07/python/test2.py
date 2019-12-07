#!/usr/bin/env python3

from typing import Dict, Tuple

import helper
from part2 import Setup


def run_test1() -> None:
    line = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    program = tuple([int(n) for n in line.split(",")])
    sequence = (9, 8, 7, 6, 5)
#
    setup = Setup(program, sequence)
    setup.run()
    result = setup.get_output()
    print(result)

    assert(result == 139_629_729)


def run_test2() -> None:
    line = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    program = tuple([int(n) for n in line.split(",")])
    sequence = (9, 7, 8, 5, 6)
#
    setup = Setup(program, sequence)
    setup.run()
    result = setup.get_output()
    print(result)

    assert(result == 18_216)


def find_solution_for_test2() -> None:
    line = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    program = tuple([int(n) for n in line.split(",")])

    permutations = helper.get_all_permutations((5, 6, 7, 8, 9))
    d: Dict[Tuple[int, ...], int] = {}    # sequence -> output_value
    for seq in permutations:
        setup = Setup(program, seq)
        setup.run()
        result = setup.get_output()
        d[seq] = result
    #
    maxi = max(d.items(), key=lambda t: t[1])
    print(maxi)

    assert(maxi[0] == (9, 7, 8, 5, 6))
    assert(maxi[1] == 18_216)


def main() -> None:
    run_test1()
    run_test2()
    find_solution_for_test2()

##############################################################################

if __name__ == "__main__":
    main()
