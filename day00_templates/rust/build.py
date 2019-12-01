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
def p1():
    """
    compile and run Part 1
    """
    cmds = [
        "cargo run --bin part1"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def p1r():
    """
    compile and run Part 1 with --release
    """
    cmds = [
        "cargo run --release --bin part1"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def p2():
    """
    compile and run Part 2
    """
    cmds = [
        "cargo run --bin part2"
    ]
    for cmd in cmds:
        call_external_command(cmd)


@task()
def p2r():
    """
    compile and run Part 2 with --release
    """
    cmds = [
        "cargo run --release --bin part2"
    ]
    for cmd in cmds:
        call_external_command(cmd)
