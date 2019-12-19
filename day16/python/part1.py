#!/usr/bin/env python3

from pprint import pprint
from typing import Dict, Generator

import helper
import numpy as np


def sequence(multiplier: int) -> Generator[int, None, None]:
    assert multiplier >= 1
    #
    base = (0, 1, 0, -1)
    li = []
    for elem in base:
        for _ in range(multiplier):
            li.append(elem)
        #
    #
    length = len(li)
    idx = 0
    while True:
        yield li[idx]
        idx = (idx + 1) % length


class Cache:
    #
    def __init__(self, line: str) -> None:
        self.line = line
        print("Begin: build cache...")
        self.d = self.build_cache(self.line)
        print("End: build cache")

    def build_cache(self, line: str) -> Dict[int, np.array]:
        d: Dict[int, np.array] = {}
        length = len(line)
        for i in range(1, length+1):
            seq = sequence(i)
            li = []
            for _ in range(length+1):
                li.append(next(seq))
            li = li[1:]
            d[i] = np.array(li)
        #
        return d

    def __getitem__(self, key: int) -> np.array:
        return self.d[key]

    def debug(self) -> None:
        pprint(self.d)


def transform(line: str, cache: Cache) -> str:
    numbers = np.array([int(digit) for digit in line])
    length = len(line)
    sb = []
    for i in range(1, length+1):
        mul = numbers * cache[i]
        num = np.sum(mul)
        res = np.abs(num) % 10
        sb.append(str(res))
    #
    return "".join(sb)


def process(curr: str, cache: Cache, repeat=1) -> str:
    # print(curr)
    step = 0
    for i in range(repeat):
        curr = transform(curr, cache)
        step += 1
        # print(f"{step}) {curr}")
    #
    return curr


def test_1() -> None:
    line = "12345678"
    cache = Cache(line)
    process(line, cache, repeat=4)


def test_2() -> None:
    line = "80871224585914546619083218645595"
    cache = Cache(line)
    process(line, cache, repeat=100)


def real() -> None:
    line = helper.read_lines("input.txt")[0]
    cache = Cache(line)
    result = process(line, cache, repeat=100)
    print(result)
    print()
    print("First eight digits:", result[:8])


def main() -> None:
    # test_1()
    # test_2()

    real()

##############################################################################

if __name__ == "__main__":
    main()
