#!/usr/bin/env rdmd

import std.algorithm;
import std.conv;
import std.file;
import std.stdio;
import std.string;

int total_fuel(const int mass) pure
{
    int fuel(const int mass) pure
    {
        return mass / 3 - 2;
    }

    int result = 0;
    int value = mass;

    while (value > 0)
    {
        value = fuel(value);
        if (value > 0)
        {
            result += value;
        }
    }

    return result;
}

void main()
{
    // const int mass = 14; // 2
    // const int mass = 1969; // 654 + 216 + 70 + 21 + 5 = 966
    // const int mass = 100_756; // 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346

    // int result = total_fuel(mass);
    // writeln(result);

    int result = readText("input.txt").splitLines.map!(line => total_fuel(line.to!int)).sum;
    writeln(result);
}
