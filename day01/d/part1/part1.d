#!/usr/bin/env rdmd

import std.algorithm;
import std.conv;
import std.file;
import std.stdio;
import std.string;

int fuel(const int mass) pure
{
    return mass / 3 - 2;
}

void main()
{
    // const int mass = 12; // 2
    // const int mass = 14; // 2
    // const int mass = 1969; // 654
    // const int mass = 100_756; // 33583

    // int result = fuel(mass);
    // writeln(result);

    int result = readText("input.txt").splitLines.map!(line => fuel(line.to!int)).sum;
    writeln(result);
}
