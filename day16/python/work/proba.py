#!/usr/bin/env python3

import numpy as np


def sequence(multiplier: int):
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


def main():
    np_heights = np.array([1.74, 1.69, 1.70, 1.88])
    mul = np.array([2, 2, 2, 2])
    print(np_heights * mul)
    seq = sequence(1)
    for i in range(20):
        print(next(seq))

##############################################################################

if __name__ == "__main__":
    main()
