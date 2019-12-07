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


class Amplifier:
    def __init__(self, program, prg_input):
        self.program = program[:]    # make a copy of it
        self.prg_input = prg_input
        self.prg_output = None    # will be set later

    def read_input(self) -> int:
        return self.prg_input

    def get_output(self) -> int:
        return self.prg_output

    def run(self) -> None:
        #
        def get_param(data: List[int], value: int, mode: Mode) -> int:
            if mode == Mode.IMMEDIATE_MODE:
                return value
            else:
                return data[value]

        data = self.program[:]
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
                inp = self.read_input()
                data[data[idx + 1]] = inp
                idx += 2
            elif inst.opcode == 4:
                inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
                self.prg_output = inp1    # output here
                idx += 2
            elif inst.opcode == 5:    # jump-if-true
                inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
                inp2 = get_param(data, data[idx + 2], inst.second_param_mode)
                if inp1 != 0:
                    idx = inp2
                else:
                    idx += 3
            elif inst.opcode == 6:    # jump-if-false
                inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
                inp2 = get_param(data, data[idx + 2], inst.second_param_mode)
                if inp1 == 0:
                    idx = inp2
                else:
                    idx += 3
            elif inst.opcode == 7:    # less than
                inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
                inp2 = get_param(data, data[idx + 2], inst.second_param_mode)
                if inp1 < inp2:
                    data[data[idx + 3]] = 1
                else:
                    data[data[idx + 3]] = 0
                #
                idx += 4
            elif inst.opcode == 8:    # equals
                inp1 = get_param(data, data[idx + 1], inst.first_param_mode)
                inp2 = get_param(data, data[idx + 2], inst.second_param_mode)
                if inp1 == inp2:
                    data[data[idx + 3]] = 1
                else:
                    data[data[idx + 3]] = 0
                #
                idx += 4
            else:
                raise ShouldNeverGetHere()    # invalid opcode
            # endif
            inst = read_instruction(data[idx])
        # endwhile
    # enddef






def try_permutation():
    sequence = ["0", "1", "2", "3", "4"]
    permutations = helper.get_all_permutations(sequence)
    print(permutations)
    print(len(permutations))


def main() -> None:
    line = helper.read_lines("input_day5.txt")[0]
    program = [int(n) for n in line.split(",")]

    ampl = Amplifier(program, 5)
    ampl.run()
    print(ampl.get_output())
    ampl.run()
    print(ampl.get_output())

##############################################################################

if __name__ == "__main__":
    main()
    # try_permutation()
