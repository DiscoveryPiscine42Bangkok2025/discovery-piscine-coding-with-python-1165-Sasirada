#!/usr/bin/env python3

import sys

if (len(sys.argv) >= 3) :
    arg_len = len(sys.argv) 
    while (arg_len - 1 > 0) :
        print(sys.argv[arg_len - 1])
        arg_len -= 1
else :
    print("none")