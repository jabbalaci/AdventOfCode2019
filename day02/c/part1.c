#include <stdio.h>
#include <stdlib.h>

#include "helper.h"


void debug(const int *numbers)
{
    for (int i = 0; i < arrlen(numbers); ++i) {
        printf("%d ", numbers[i]);
    }
    puts("");
}

int * process(const int *numbers)
{
    // start: make a copy
    int *data = NULL;
    arrsetlen(data, arrlen(numbers));
    for (int i = 0; i < arrlen(numbers); ++i) {
        data[i] = numbers[i];
    }
    // end

    int idx = 0;
    int opcode = data[idx];
    while (opcode != 99) {
        if (opcode == 1) {
            const int inp1 = data[data[idx + 1]];
            const int inp2 = data[data[idx + 2]];
            data[data[idx + 3]] = inp1 + inp2;
        }
        else if (opcode == 2) {
            const int inp1 = data[data[idx + 1]];
            const int inp2 = data[data[idx + 2]];
            data[data[idx + 3]] = inp1 * inp2;
        }
        idx += 4;
        opcode = data[idx];
    }

    return data;
}

int main()
{
    // test cases:
    // char line[] = "1,9,10,3,2,3,11,0,99,30,40,50";
    // char line[] = "1,0,0,0,99";
    // char line[] = "2,3,0,3,99";
    // char line[] = "2,4,4,5,99,0";
    // char line[] = "1,1,1,4,99,5,6,0,99";

    char* *lines = read_lines("input.txt");
    char* line = lines[0];

    int *numbers = extract_ints_from_string(line, ",");
    numbers[1] = 12;
    numbers[2] = 2;

    puts("before:");
    debug(numbers);
    numbers = process(numbers);
    puts("");
    puts("after:");
    debug(numbers);

    return 0;
}
