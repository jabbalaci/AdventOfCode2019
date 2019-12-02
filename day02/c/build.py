#!/usr/bin/env python3

"""
pynt's build file
https://github.com/rags/pynt

Usage:

$ pynt
"""

import os
import shutil
import sys

from pynt import task


def get_platform():
    text = sys.platform
    if text.startswith("linux"):
        return "linux"
    if text.startswith("win"):
        return "windows"
    # else
    raise RuntimeError("unknown platform")

platform = get_platform()


def call_external_command(cmd):
    print(f"┌ start: calling external command '{cmd}'")
    os.system(cmd)
    print(f"└ end: calling external command '{cmd}'")


def pretty(name, force=False):
    """
    If name is a directory, then add a trailing slash to it.
    """
    if name.endswith("/"):
        return name    # nothing to do
    # else
    if force:
        return f"{name}/"
    # else
    if not os.path.isdir(name):
        return name    # not a dir. => don't modify it
    # else
    return f"{name}/"


def remove_file(fname):
    if not os.path.exists(fname):
        print(f"{fname} doesn't exist")
        return
    #
    print(f"┌ start: remove {fname}")
    try:
        os.remove(fname)
    except:
        print("exception happened")
    print(f"└ end: remove {fname}")


def remove_directory(dname):
    if not os.path.exists(dname):
        print(f"{pretty(dname, True)} doesn't exist")
        return
    #
    print(f"┌ start: remove {pretty(dname)}")
    try:
        shutil.rmtree(dname)
    except Exception as e:
        print("exception happened:", e)
    print(f"└ end: remove {pretty(dname)}")


def rename_file(src, dest):
    print(f"┌ start: rename {src} -> {dest}")
    shutil.move(src, dest)
    print(f"└ end: rename {src} -> {dest}")


###########
## Tasks ##
###########

@task()
def g1():
    """
    compile Part 1 (gcc, debug)
    """
    cmds = [
        "gcc -Wall part1.c -o p1"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def go1():
    """
    compile and optimize Part 1 (gcc, release)
    """
    cmds = [
        "gcc -Wall -O2 part1.c -o p1"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def gr1():
    """
    compile and run Part 1 (gcc, debug)
    """
    g1()
    cmds = [
        "./p1"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def c1():
    """
    compile Part 1 (clang, debug)
    """
    cmds = [
        "clang -Wall part1.c -o p1"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def co1():
    """
    compile and optimize Part 1 (clang, release)
    """
    cmds = [
        "clang -Wall -O2 part1.c -o p1"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def g2():
    """
    compile Part 2 (gcc, debug)
    """
    cmds = [
        "gcc -Wall part2.c -o p2"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def go2():
    """
    compile and optimize Part 2 (gcc, release)
    """
    cmds = [
        "gcc -Wall -O2 part2.c -o p2"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def gr2():
    """
    compile and run Part 2 (gcc, debug)
    """
    g2()
    cmds = [
        "./p2"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def c2():
    """
    compile Part 2 (clang, debug)
    """
    cmds = [
        "clang -Wall part2.c -o p2"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def co2():
    """
    compile and optimize Part 2 (clang, release)
    """
    cmds = [
        "clang -Wall -O2 part2.c -o p2"
    ]
    for cmd in cmds:
        call_external_command(cmd)
