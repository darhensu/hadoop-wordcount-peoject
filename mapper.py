#!/usr/bin/env python 3
import sys

# Input processing
for line in sys.stdin:
    line = line.strip() # remove leading and trailing whitespace
    words = line.split() # split line into words
    for word in words:
        # output key-value pair: word\t 1
        print(f"{word}\t1")