Advent of Code 2019
===================

My solutions for [AoC 2019](https://adventofcode.com/2019/). [Last year](https://github.com/jabbalaci/AdventOfCode2018)
I used the Nim programming language, but this year I want to use several languages, mainly Python, C and Rust.

pynt
----

I use a minimalistic build tool called [pynt](https://github.com/rags/pynt). It's written in Python
but it can be used for anything. You can install it with `pip3`:

    pip3 install pynt --user -U

Then, if you see a `build.py` file, just launch the command `pynt` and it will print
the available tasks. For instance, to run the static type checker against a Python solution,
run `pynt mypy` inside the folder of a Python solution (for this to work, you need to
install mypy too, but you know the drill: `pip3 install mypy --user -U`).

Links
-----

* [Advent of Code](https://adventofcode.com/)

Environment
-----------

* Python: 3.7.x
* Rust: 1.39.0
* Operating system: Linux

Do you use C++?
---------------

No. For the C solutions, I use a library called [stb](https://github.com/nothings/stb)
that works with C/C++. Since I include this library everywhere (to produce stand-alone solutions),
GitHub includes C++ in the project's language details.

Awesome AoC
-----------

* [Awesome AoC](https://github.com/Bogdanp/awesome-advent-of-code) is a collection of
  awesome resources related to the yearly Advent of Code challenge
* Awesome AoC / [Python](https://github.com/Bogdanp/awesome-advent-of-code#python)
* Awesome AoC / [C](https://github.com/Bogdanp/awesome-advent-of-code#c)
* Awesome AoC / [Rust](https://github.com/Bogdanp/awesome-advent-of-code#rust)
