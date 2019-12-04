#!/usr/bin/env python3

from typing import Dict, List


def explode(n: int) -> List[int]:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    #
    return digits[::-1]


def is_password(digits: List[int]) -> bool:
    ascending = True
    for i in range(len(digits)-1):
        a = digits[i]
        b = digits[i+1]
        if a > b:
            ascending = False
    #
    if not ascending:
        return False
    #
    d: Dict[int, int] = {}
    for digit in digits:
        d[digit] = d.get(digit, 0) + 1
    has_double = 2 in d.values()
    #
    if not has_double:
        return False
    #
    return True


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
    # line = "112233-112233"    # test 1
    # line = "123444-123444"    # test 2
    # line = "111122-111122"    # test 3
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
