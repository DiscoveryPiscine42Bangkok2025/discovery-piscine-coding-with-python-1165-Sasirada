#!/usr/bin/env python3

import sys

params_len = len(sys.argv)
if (params_len == 2) :
    count = 0
    for i in range(len(sys.argv[1])) :
        if (sys.argv[1][i] == 'z') :
            count += 1
    if (count > 0) :
        for i in range(0, count) :
            print("z", end="" if (i < count - 1) else "\n")
    else :
        print("none")
else :
    print("none")