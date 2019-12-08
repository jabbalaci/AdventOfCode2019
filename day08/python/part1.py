#!/usr/bin/env python3

import helper


def main() -> None:
    # line = "123456789012"    # layer size: 2 * 3 = 6
    line = helper.read_lines("input.txt")[0]    # layer size: 6 * 25 = 150

    mini = min(helper.grouper(line, 6 * 25), key=lambda t: t.count("0"))
    result = mini.count("1") * mini.count("2")

    print(result)

##############################################################################

if __name__ == "__main__":
    main()
