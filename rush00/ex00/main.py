#!/usr/bin/env python3

from checkmate import checkmate

def main() :
    board = """\
....
.K..
.P..
.R..\
"""
    print(board)
    checkmate(board)

if __name__ == "__main__" :
    main()