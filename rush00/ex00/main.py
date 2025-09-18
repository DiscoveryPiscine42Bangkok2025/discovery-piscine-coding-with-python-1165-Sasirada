#!/usr/bin/env python3

from checkmate import checkmate

def main() :
    board = """\
R..o
.K..
..B.
....\
"""
    checkmate(board)

if __name__ == "__main__" :
    main()