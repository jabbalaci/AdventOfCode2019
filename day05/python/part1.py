#!/usr/bin/env python3

from enum import Enum
from typing import List, NamedTuple

import helper


class ShouldNeverGetHere(Exception):
    pass


class Mode(Enum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1


class Instruction(NamedTuple):
    opcode: int
    first_param_mode: Mode
    second_param_mode: Mode
    third_param_mode: Mode


def read_input() -> int:
    return 1


def read_instruction(number: int) -> Instruction:
    #
    def to_mode(c: str) -> Mode:
        if c == '0':
            return Mode.POSITION_MODE
        if c == '1':
            return Mode.IMMEDIATE_MODE
        raise ShouldNeverGetHere()

    if number == 99:
        # special case, it'll halt the program; parameter modes are not used, they get a dummy value
        return Instruction(opcode=number, first_param_mode=Mode.POSITION_MODE,
                       second_param_mode=Mode.POSITION_MODE, third_param_mode=Mode.POSITION_MODE)

    s = str(number)
    if len(s) == 1:
        opcode = number
        first_param_mode = second_param_mode = third_param_mode = Mode.POSITION_MODE    # default
    else:
        opcode = int(s[-2:].replace("0", ""))
        params = s[:-2].zfill(3)
        first_param_mode = to_mode(params[-1])
        second_param_mode = to_mode(params[-2])
        third_param_mode = to_mode(params[-3])
    #
    return Instruction(opcode=opcode, first_param_mode=first_param_mode,
                       second_param_mode=second_param_mode, third_param_mode=third_param_mode)


def run(program: List[int]) -> None:
    #
    def get_param(data: List[int], value: int, mode: Mode) -> int:
        if mode == Mode.IMMEDIATE_MODE:
            return value
        else:
            return data[value]

    data = program[:]
    idx = 0
    inst: Instruction = read_instruction(data[idx])
    while inst.opcode != 99:
        if inst.opcode == 1:
            inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
            inp2 = get_param(data, data[idx + 2], inst.second_param_mode)
            data[data[idx + 3]] = inp1 + inp2
            idx += 4
        elif inst.opcode == 2:
            inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
            inp2 = get_param(data, data[idx + 2], inst.second_param_mode)
            data[data[idx + 3]] = inp1 * inp2
            idx += 4
        elif inst.opcode == 3:
            inp = read_input()
            data[data[idx + 1]] = inp
            idx += 2
        elif inst.opcode == 4:
            inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
            print("Output:", inp1)
            idx += 2
        else:
            raise ShouldNeverGetHere()    # invalid opcode
        # endif
        inst = read_instruction(data[idx])
    # endwhile


def main() -> None:
    # test cases:
    # line = "3,0,4,0,99"
    # line = "1002,4,3,4,33"

    line = helper.read_lines("input.txt")[0]
    program = [int(n) for n in line.split(",")]

    run(program)

##############################################################################

if __name__ == "__main__":
    main()
