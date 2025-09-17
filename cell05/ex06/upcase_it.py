#!/usr/bin/env python3

import sys

if (len(sys.argv) == 2) :
    try :
        str = sys.argv[1].upper()
        print(str)
    except :
        print(sys.argv[1])
else :
    print("none")