#include "helper.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

const int GOAL = 19690720;


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
    char* *lines = read_lines("input.txt");
    char* line = lines[0];
    bool terminate = false;

    int *numbers = extract_ints_from_string(line, ",");

    for (int i = 0; i <= 99; ++i) {
        for (int j = 0; j <= 99; ++j) {
            numbers[1] = i;
            numbers[2] = j;
            printf("# i = %d, j = %d\n", i, j);
            int *result = process(numbers);
            bool found = (result[0] == GOAL);
            arrfree(result);
            if (found) {
                printf("i = %d\n", i);
                printf("j = %d\n", j);
                printf("answer: %d\n", 100 * i + j);
                terminate = true;
                break;
            }
        }
        if (terminate) {
            break;
        }
    }
    puts("__END__");

    return 0;
}
