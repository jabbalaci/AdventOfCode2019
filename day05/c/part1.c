#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "helper.h"


typedef enum {
    PositionMode = 0,
    ImmediateMode = 1
} Mode;

typedef struct {
    int opcode;
    Mode first_param_mode;
    Mode second_param_mode;
    Mode third_param_mode;
} Instruction;

int read_input() {
    return 1;
}

Mode to_mode(char c)
{
    if (c == '0') {
        return PositionMode;
    } else {
        return ImmediateMode;
    }
}

Instruction read_instruction(const int number)
{
    if (number == 99)
    {
        // special case, it'll halt the program; parameter modes are not used, they get a dummy value
        return (Instruction){ 99, PositionMode, PositionMode, PositionMode };
    }

    char s[10];
    sprintf(s, "%d", number);
    const int len = strlen(s);
    if (len == 1)
    {
        return (Instruction){ number, PositionMode, PositionMode, PositionMode };
    }
    else
    {
        const char* last = &s[len-1];
        int opcode;
        sscanf(last, "%d", &opcode);
        char *copy = strdup(s);
        copy[len-2] = '\0';
        Mode first_param_mode = PositionMode;
        Mode second_param_mode = PositionMode;
        Mode third_param_mode = PositionMode;
        if (strlen(copy) >= 1) {
            first_param_mode = to_mode(copy[strlen(copy)-1]);
        }
        if (strlen(copy) >= 2) {
            second_param_mode = to_mode(copy[strlen(copy)-2]);
        }
        if (strlen(copy) >= 3) {
            third_param_mode = to_mode(copy[strlen(copy)-3]);
        }

        return (Instruction){ opcode, first_param_mode, second_param_mode, third_param_mode };
    }
}

int get_param(int *data, int value, Mode mode)
{
    if (mode == ImmediateMode) {
        return value;
    } else {
        return data[value];
    }
}

void run(const int *numbers)
{
    // start: make a copy
    int *data = NULL;
    arrsetlen(data, arrlen(numbers));
    for (int i = 0; i < arrlen(numbers); ++i) {
        data[i] = numbers[i];
    }
    // end

    int idx = 0;
    Instruction inst = read_instruction(data[idx]);
    while (inst.opcode != 99)
    {
        if (inst.opcode == 1)
        {
            const int inp1 = get_param(data, data[idx + 1], inst.first_param_mode);
            const int inp2 = get_param(data, data[idx + 2], inst.second_param_mode);
            data[data[idx + 3]] = inp1 + inp2;
            idx += 4;
        }
        else if (inst.opcode == 2)
        {
            const int inp1 = get_param(data, data[idx + 1], inst.first_param_mode);
            const int inp2 = get_param(data, data[idx + 2], inst.second_param_mode);
            data[data[idx + 3]] = inp1 * inp2;
            idx += 4;
        }
        else if (inst.opcode == 3)
        {
            const int inp = read_input();
            data[data[idx + 1]] = inp;
            idx += 2;
        }
        else if (inst.opcode == 4)
        {
            const int inp1 = get_param(data, data[idx + 1], inst.first_param_mode);
            printf("Output: %d\n", inp1);
            idx += 2;
        }
        else {
            printf("Error: invalid opcode!");
        }

        inst = read_instruction(data[idx]);
    }
}

int main()
{
    // test cases:
    // char line[] = "3,0,4,0,99";
    // char line[] = "1002,4,3,4,33";

    char* *lines = read_lines("input.txt");
    char* line = lines[0];

    const int *program = extract_ints_from_string(line, ",");

    run(program);

    return 0;
}
