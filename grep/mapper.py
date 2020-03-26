#!/usr/bin/env python

import sys
import os
from sys import argv
import re

#set regular expression
re_expr = argv[1]

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
        
        re_resu = re.findall(re_expr,word)
        if re_resu:
            print '%s\t%s' % (word, 1)
        else:
            print '%s\t%s' % (word, 0)
