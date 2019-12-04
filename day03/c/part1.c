#include "helper.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// ============
// struct Point
// ============

typedef struct {
    int x;
    int y;
} Point;

// =======
// hashmap
// =======

typedef struct {
    Point key;
    int value;
} MapPointInt;

// ===========
// struct Grid
// ===========

typedef struct {
    char* *wire1;               // vector of strings
    char* *wire2;               // vector of strings
    MapPointInt *wire1_path;    // hashmap
    MapPointInt *wire2_path;    // hashmap
} Grid;

void init(Grid *grid, char* line1, char* line2)
{
    grid -> wire1 = extract_strings_from_string(line1, ",");
    grid -> wire2 = extract_strings_from_string(line2, ",");
}

void debug(const Grid *grid)
{
    for (int i = 0; i < arrlen(grid -> wire1); ++i) {
        printf("%s ", (grid -> wire1)[i]);
    }
    puts("");

    for (int i = 0; i < arrlen(grid -> wire2); ++i) {
        printf("%s ", (grid -> wire2)[i]);
    }
    puts("");
}

MapPointInt * follow_wire(char* *wire)
{
    MapPointInt *coordinates = NULL;
    int x = 0;
    int y = 0;
    for (int i = 0; i < arrlen(wire); ++i) {
        char* instruction = wire[i];
        char direction = instruction[0];
        int steps = atoi(instruction + 1);
        // printf("%d ", steps);
        for (int j = 0; j < steps; ++j) {
            switch (direction)
            {
                case 'R':   ++x;
                            break;
                case 'L':   --x;
                            break;
                case 'U':   ++y;
                            break;
                case 'D':   --y;
                            break;
                default:    break;    // we should never get here
            }
            Point p = (Point){x, y};
            hmput(coordinates, p, 0);    // 0 is a dummy value
        }
    }
    // puts("");
    // puts("");

    return coordinates;
}

void follow_wires(Grid *grid)
{
    grid -> wire1_path = follow_wire(grid -> wire1);
    // printf("%ld\n", hmlen(grid -> wire1_path));
    grid -> wire2_path = follow_wire(grid -> wire2);
    // printf("%ld\n", hmlen(grid -> wire2_path));
}

void debug2(Grid *grid)
{
    for (int i = 0; i < hmlen(grid -> wire1_path); ++i) {
        Point p = (grid -> wire1_path)[i].key;
        printf("(%d, %d) ", p.x, p.y);
    }
    puts("");

    for (int i = 0; i < hmlen(grid -> wire2_path); ++i) {
        Point p = (grid -> wire2_path)[i].key;
        printf("(%d, %d) ", p.x, p.y);
    }
    puts("");
}

Point * get_intersection(MapPointInt *path1, MapPointInt *path2)
{
    Point *result = NULL;

    for (int i = 0; i < hmlen(path1); ++i)
    {
        Point p1 = path1[i].key;
        bool found_in_other = (hmgeti(path2, p1) != -1);
        if (found_in_other) {
            arrput(result, p1);
        }
    }

    return result;
}

int find_closest_intersection(const Grid *grid)
{
    Point *common = get_intersection(grid -> wire1_path, grid -> wire2_path);

    // for (int i = 0; i < arrlen(common); ++i) {
        // Point p = common[i];
        // printf("(%d, %d) ", p.x, p.y);
    // }
    // puts("");

    Point* closest = &common[0];
    int closest_distance = abs(closest -> x) + abs(closest -> y);
    for (int i = 0; i < arrlen(common); ++i) {
        Point *p = &common[i];
        int p_distance = abs(p -> x) + abs(p -> y);
        if (p_distance < closest_distance) {
            closest = p;
            closest_distance = p_distance;
        }
    }
    // printf("(%d, %d)\n", closest -> x, closest -> y);
    int result = abs(closest -> x) + abs(closest -> y);

    return result;
}

// ==========================================================================

int main()
{
    // char* *lines = read_lines("examples/part1/example1.txt");
    // char* *lines = read_lines("examples/part1/example2.txt");
    // char* *lines = read_lines("examples/part1/example3.txt");
    char* *lines = read_lines("input.txt");
    char* line1 = lines[0];
    char* line2 = lines[1];

    // printf("%s\n", line1);
    // printf("%s\n", line2);

    Grid grid;
    init(&grid, line1, line2);
    // debug(&grid);
    follow_wires(&grid);
    // debug2(&grid);
    int result = find_closest_intersection(&grid);
    printf("%d\n", result);

    return 0;
}
