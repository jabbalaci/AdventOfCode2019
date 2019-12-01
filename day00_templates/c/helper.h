#define STB_DS_IMPLEMENTATION
#include "lib/stb_ds.h"

/*
stb_ds.h:

Source: https://github.com/nothings/stb/blob/master/stb_ds.h
Docs: http://nothings.org/stb_ds
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXCHAR 1000

char* * read_lines(const char* fname)
{
    char* *lines = NULL;    // dynamic array

    char buffer[MAXCHAR];

    FILE *fp = fopen(fname, "r");

    if (fp == NULL) {
        printf("Error: could not open file %s", fname);
        exit(1);
    }

    while (fgets(buffer, MAXCHAR, fp) != NULL) {
        size_t len = strlen(buffer);
        if (len > 0 && buffer[len-1] == '\n') {
            buffer[len - 1] = '\0';
        }
        arrput(lines, strdup(buffer));
    }

    fclose(fp);

    return lines;
}
