#!/usr/bin/env python3

from typing import List

import helper


def decode(image: List[str], line_length: int) -> None:
    for line in helper.grouper(image, line_length):
        s = "".join(line)
        s = s.replace("0", " ").replace("1", "▮")
        print(s)


def main() -> None:
    # line = "0222112222120000"    # layer size: 2 * 2 = 4
    line = helper.read_lines("input.txt")[0]    # layer size: 6 * 25 = 150

    result = []
    layers = list(helper.grouper(line, 6 * 25))
    for i in range(len(layers[0])):
        for layer in layers:
            if layer[i] == "0":    # black
                result.append("0")
                break
            if layer[i] == "1":    # white
                result.append("1")
                break
        #
    #
    # print(result)
    decode(result, line_length=25)

##############################################################################

if __name__ == "__main__":
    main()
