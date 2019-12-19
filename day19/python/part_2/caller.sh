#!/usr/bin/env bash

./part2.py > p2.txt

./process.py > image.pbm

# then open image.pbm with Gimp, create a fixed-size selection (100 x 100 pixels),
# adjust it to the correct position and read the position of its top left pixel
