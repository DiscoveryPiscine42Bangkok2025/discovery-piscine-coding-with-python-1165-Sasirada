#!/usr/bin/env python3

import sys

def print_table(n) :
    i = 0
    while (i <= 10) :
        print((n * i), end=" " if (i < 10) else "\n")
        i += 1

if (len(sys.argv) == 1) :
    n = 0
    while (n <= 10) :
        print(f"Table de {n}:", end=" ")
        print_table(n)
        n += 1
else :
    try :
        n = int(sys.argv[1])
        print(f"Table de {n}:", end=" ")
        print_table(n)
    except :
        print("none")