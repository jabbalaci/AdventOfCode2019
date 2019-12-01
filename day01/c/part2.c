#include "helper.h"

#include <stdio.h>
#include <stdlib.h>

int fuel(const int mass) {
    return (mass / 3) - 2;
}

int extra_fuel(const int mass)
{
    int value = mass;
    int total = 0;

    while (value > 0) {
        value = fuel(value);
        if (value > 0) {
            total += value;
        }
    }
    return total;
}

int main()
{
    char* *lines = read_lines("input.txt");

    int total = 0;
    for (int i = 0; i < arrlen(lines); ++i) {
        char* line = lines[i];
        int value = atoi(line);
        total += extra_fuel(value);
    }
    printf("%d\n", total);

    return 0;
}
