#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

# process input from mapper
for line in sys.stdin:
    line = line.strip() # remove leading/trailing whitespace
    word, count = line.split("\t", 1) # split line into word and count
    try:
        count = int(count)
    except ValueError:
        continue # ignore lines with errors
    
    if word == current_word:
        current_count += count
    else:
        if current_word:
            # output key-value pair: word \t count
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count
        
# putput the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")
    
    

