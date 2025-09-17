#!/usr/bin/env python3

import sys

count = len(sys.argv)
if (count >= 2) :
    print("parameters:", count - 1)
    for i in range(1, count) :
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
        i += 1
else :
    print("none")