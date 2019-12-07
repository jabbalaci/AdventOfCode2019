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
        self.data = list(program)       # mutable copy
        self.prg_input = 0              # will be set later
        self.prg_output = 0             # will be set later
        self.phase = 0                  # will be set later
        self.first_call = True          # Was read_input() called for the first time?
        self.stopped = False
        self.idx = 0                    # instruction pointer

    def set_phase(self, value: int) -> None:
        self.phase = value

    def get_input(self) -> int:
        return self.prg_input

    def set_input(self, value: int) -> None:
        self.prg_input = value

    def read_input(self) -> int:
        if self.first_call:
            self.first_call = False
            return self.phase
        # else
        return self.prg_input

    def get_output(self) -> int:
        return self.prg_output

    def set_output(self, value) -> None:
        self.prg_output = value

    def is_stopped(self):
        return self.stopped

    def run(self) -> None:
        """
        data and idx became self.data and self.idx, thus the execution
        of the program can be paused any time and it can be continued
        later (i.e., the program's state is freezed and can be resumed).
        How? The program (data) and the instruction pointer (idx) are
        instance variables.
        """
        #
        def get_param(data: List[int], value: int, mode: Mode) -> int:
            if mode == Mode.IMMEDIATE_MODE:
                return value
            else:
                return data[value]

        inst: Instruction = read_instruction(self.data[self.idx])
        while True:
            if inst.opcode == 1:
                inp1 = get_param(self.data, self.data[self.idx + 1], inst.first_param_mode)
                inp2 = get_param(self.data, self.data[self.idx + 2], inst.second_param_mode)
                self.data[self.data[self.idx + 3]] = inp1 + inp2
                self.idx += 4
            elif inst.opcode == 2:
                inp1 = get_param(self.data, self.data[self.idx + 1], inst.first_param_mode)
                inp2 = get_param(self.data, self.data[self.idx + 2], inst.second_param_mode)
                self.data[self.data[self.idx + 3]] = inp1 * inp2
                self.idx += 4
            elif inst.opcode == 3:
                inp = self.read_input()
                self.data[self.data[self.idx + 1]] = inp
                self.idx += 2
            elif inst.opcode == 4:    # output
                inp1 = get_param(self.data, self.data[self.idx + 1], inst.first_param_mode)
                self.prg_output = inp1
                self.idx += 2
                #
                break    # pause execution
            elif inst.opcode == 5:    # jump-if-true
                inp1 = get_param(self.data, self.data[self.idx + 1], inst.first_param_mode)
                inp2 = get_param(self.data, self.data[self.idx + 2], inst.second_param_mode)
                if inp1 != 0:
                    self.idx = inp2
                else:
                    self.idx += 3
            elif inst.opcode == 6:    # jump-if-false
                inp1 = get_param(self.data, self.data[self.idx + 1], inst.first_param_mode)
                inp2 = get_param(self.data, self.data[self.idx + 2], inst.second_param_mode)
                if inp1 == 0:
                    self.idx = inp2
                else:
                    self.idx += 3
            elif inst.opcode == 7:    # less than
                inp1 = get_param(self.data, self.data[self.idx + 1], inst.first_param_mode)
                inp2 = get_param(self.data, self.data[self.idx + 2], inst.second_param_mode)
                if inp1 < inp2:
                    self.data[self.data[self.idx + 3]] = 1
                else:
                    self.data[self.data[self.idx + 3]] = 0
                #
                self.idx += 4
            elif inst.opcode == 8:    # equals
                inp1 = get_param(self.data, self.data[self.idx + 1], inst.first_param_mode)
                inp2 = get_param(self.data, self.data[self.idx + 2], inst.second_param_mode)
                if inp1 == inp2:
                    self.data[self.data[self.idx + 3]] = 1
                else:
                    self.data[self.data[self.idx + 3]] = 0
                #
                self.idx += 4
            elif inst.opcode == 99:    # halt
                self.stopped = True
                break
            else:
                raise ShouldNeverGetHere()    # invalid opcode
            # endif
            inst = read_instruction(self.data[self.idx])
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
        self.num_of_amplifiers = 5
        self.last_idx = self.num_of_amplifiers - 1
        self.amplifiers = [Amplifier(program) for _ in range(self.num_of_amplifiers)]
        #
        self.set_init_sequence(sequence)

    def set_init_sequence(self, sequence: Tuple[int, ...]) -> None:
        for i in range(self.num_of_amplifiers):
            self.amplifiers[i].set_phase(sequence[i])

    def run(self) -> None:
        first = self.amplifiers[0]
        last = self.amplifiers[-1]
        last.set_output(0)    # for Ampl. A, it'll be its first input
        idx = 0
        #
        while True:
            curr = self.amplifiers[idx]
            prev = self.amplifiers[idx-1]
            #
            curr.set_input(prev.get_output())
            curr.run()
            # print("idx: {}, input: {}, output: {}".format(idx, curr.get_input(), curr.get_output()))
            if curr.is_stopped():
                break
            #
            idx += 1
            if idx > self.last_idx:
                idx = 0
        # endfor

    def get_output(self) -> int:
        return self.amplifiers[-1].get_output()
# endclass

##############################################################################

def find_solution(program: Tuple[int, ...]) -> None:
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


def main() -> None:
    line = helper.read_lines("input.txt")[0]
    program = tuple([int(n) for n in line.split(",")])

    find_solution(program)

##############################################################################

if __name__ == "__main__":
    main()
