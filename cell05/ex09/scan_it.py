#!/usr/bin/env python3

import sys
import re

if (len(sys.argv) == 3) :
    count = len(re.findall(sys.argv[1], sys.argv[2]))
    if (count > 0) :
        print(count)
    else :
        print("none")
else :
    print("none")