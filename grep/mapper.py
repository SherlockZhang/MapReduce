#!/usr/bin/env python
"""mapper.py"""

import sys
import os
from sys import argv

# define search cretiron
cretiron = int(argv[1])
cretiron_value = argv[2]

if(len(argv)==4):
    cretiron_value = [cretiron_value,argv[3]]

#define the cretirons
def one(word,cretiron_value):
    return cretiron_value in word


def two(word,cretiron_value):
    return (word.startswith(cretiron_value[0]) and word.endswith(cretiron_value[1]) )

def three(word,cretiron_value):
    count = 0
    for i in word:
        if i.isupper():
            count = count +1
    return count==int(cretiron_value)

#define swticher for each cretirons
switcher = {
    1: one,
    2: two,
    3: three
}

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        
        func =switcher.get(cretiron, lambda: "Invalid search cretiron")
        if func(word, cretiron_value):
                print '%s\t%s' % (word, 1)
