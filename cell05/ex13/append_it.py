#!/usr/bin/env python3

import sys
import re

params_len = len(sys.argv)
if (params_len >= 2) :
    for i in range(1, params_len) :
      if (not sys.argv[i].endswith("ism")) :
        print(sys.argv[i] + "ism")  
else :
    print("none")