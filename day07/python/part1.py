#!/usr/bin/env python3

from enum import Enum
from typing import Dict, List, NamedTuple, Tuple

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


###############
## Amplifier ##
###############

class Amplifier:
    def __init__(self, program: Tuple[int, ...]) -> None:
        self.program = list(program)    # mutable copy
        self.prg_input = 0    # will be set later
        self.prg_output = 0    # will be set later
        self.phase = 0    # will be set later
        self.cnt_input_calls = 0    # read_input() was called how many times

    def set_phase(self, value: int) -> None:
        self.phase = value

    def set_input(self, value: int) -> None:
        self.prg_input = value

    def read_input(self) -> int:
        if self.cnt_input_calls == 0:    # this is the first call
            result = self.phase
        elif self.cnt_input_calls == 1:    # second call
            result = self.prg_input
        else:
            raise ShouldNeverGetHere()
        #
        self.cnt_input_calls += 1
        return result

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
# endclass


###########
## Setup ##
###########

class Setup:
    def __init__(self, program: Tuple[int, ...], sequence: Tuple[int, ...]) -> None:
        self.program = program
        self.sequence = sequence
        #
        self.a1 = Amplifier(program)
        self.a2 = Amplifier(program)
        self.a3 = Amplifier(program)
        self.a4 = Amplifier(program)
        self.a5 = Amplifier(program)

        self.a1.set_phase(sequence[0])
        self.a2.set_phase(sequence[1])
        self.a3.set_phase(sequence[2])
        self.a4.set_phase(sequence[3])
        self.a5.set_phase(sequence[4])

    def run(self) -> None:
        self.a1.set_input(0)
        self.a1.run()
        #
        self.a2.set_input(self.a1.get_output())
        self.a2.run()
        #
        self.a3.set_input(self.a2.get_output())
        self.a3.run()
        #
        self.a4.set_input(self.a3.get_output())
        self.a4.run()
        #
        self.a5.set_input(self.a4.get_output())
        self.a5.run()

    def get_output(self) -> int:
        return self.a5.get_output()
# endclass

##############################################################################

def find_solution(program: Tuple[int, ...]) -> None:
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


def main() -> None:
    line = helper.read_lines("input.txt")[0]
    program = tuple([int(n) for n in line.split(",")])

    find_solution(program)

##############################################################################

if __name__ == "__main__":
    main()
