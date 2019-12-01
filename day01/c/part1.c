#include "helper.h"

#include <stdio.h>
#include <stdlib.h>

int fuel(const int mass) {
    return (mass / 3) - 2;
}

int main()
{
    char* *lines = read_lines("input.txt");

    int total = 0;
    for (int i = 0; i < arrlen(lines); ++i) {
        char* line = lines[i];
        int value = atoi(line);
        total += fuel(value);
    }
    printf("%d\n", total);

    return 0;
}
