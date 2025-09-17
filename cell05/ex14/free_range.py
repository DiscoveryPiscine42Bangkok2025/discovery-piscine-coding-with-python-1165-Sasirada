#!/usr/bin/env python3

import sys

params_len = len(sys.argv)
if (params_len == 3) :
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    ls = [(first + i) for i in range(0, second - first + 1)]
    print(ls)
else :
    print("none")