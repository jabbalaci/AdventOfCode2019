#!/usr/bin/env python3

from typing import List


def explode(n: int) -> List[int]:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    #
    return digits[::-1]


def is_password(digits: List[int]) -> bool:
    has_double = False
    ascending = True

    for i in range(len(digits)-1):
        a = digits[i]
        b = digits[i+1]
        if a == b:
            has_double = True
        if a > b:
            ascending = False
    #
    return has_double and ascending


def process(lo: int, hi: int) -> int:
    cnt = 0
    for n in range(lo, hi+1):
        digits = explode(n)
        if is_password(digits):
            cnt += 1
        #
    #
    return cnt


def main() -> None:
    # line = "111111-111111"    # test 1
    # line = "223450-223450"    # test 2
    # line = "123789-123789"    # test 3
    line = "136760-595730"    # input
    parts = line.split("-")
    lo = int(parts[0])
    hi = int(parts[1])
    # print(lo)
    # print(hi)
    result = process(lo, hi)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
