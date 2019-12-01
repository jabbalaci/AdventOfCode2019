#include "helper.h"

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char* *lines = read_lines("input.txt");

    for (int i = 0; i < arrlen(lines); ++i) {
        char* line = lines[i];
        int value = atoi(line);
        // printf("%s\n", line);
        printf("%d\n", value);
    }

    return 0;
}
