#include "helper.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define SIZE 10

// const char INPUT[] = "112233-112233";    // test 1
// const char INPUT[] = "123444-123444";    // test 2
// const char INPUT[] = "111122-111122";    // test 3
const char INPUT[] = "136760-595730";    // input


void reverse(int *lst)
{
    int i = 0;
    int j = arrlen(lst) - 1;
    int tmp;
    while (i < j) {
        tmp = lst[i];
        lst[i] = lst[j];
        lst[j] = tmp;
        ++i;
        --j;
    }
}

int * explode(const int number)
{
    int n = number;
    int *digits = NULL;

    while (n > 0) {
        arrput(digits, n % 10);
        n = n / 10;
    }

    reverse(digits);
    return digits;
}

void debug(int *lst)
{
    for (int i = 0; i < arrlen(lst); ++i) {
        printf("%d ", lst[i]);
    }
    puts("");
}

bool is_password(int *digits)
{
    bool ascending = true;

    for (int i = 0; i <= arrlen(digits) - 2; ++i)
    {
        int a = digits[i];
        int b = digits[i + 1];
        if (a > b) {
            ascending = false;
        }
    }
    if (!ascending) {
        return false;
    }

    int counter[SIZE] = { 0 };    // init with 0s
    for (int i = 0; i < arrlen(digits); ++i) {
        const int digit = digits[i];
        counter[digit] += 1;
    }
    bool has_double = false;
    for (int i = 0; i < SIZE; ++i) {
        if (counter[i] == 2) {
            has_double = true;
            break;
        }
    }

    return has_double && ascending;
}

int process(int lo, int hi)
{
    int cnt = 0;
    for (int n = lo; n <= hi; ++n) {
        int *digits = explode(n);
        if (is_password(digits)) {
            ++cnt;
        }
    }

    return cnt;
}

int main()
{
    char* *parts = extract_strings_from_string(strdup(INPUT), "-");
    const int lo = atoi(parts[0]);
    const int hi = atoi(parts[1]);
    // printf("%d %d\n", lo, hi);
    const int result = process(lo, hi);
    printf("%d\n", result);

    return 0;
}
