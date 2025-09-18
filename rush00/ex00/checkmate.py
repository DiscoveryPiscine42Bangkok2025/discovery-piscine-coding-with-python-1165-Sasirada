#!/usr/bin/env python3

def issquare(rows, n) :
    if not all(len(r) == n for r in rows) :
        print("ERROR! BOARD IS NOT SQUARE.")
        return False
    return True

def isempty(rows, n) :
    pieces = ['P', 'B', 'R', 'Q', 'K']


def checkkings(kings) :
    if (len(kings) !=)

def checkmate(board: str) :
    rows = board.strip().split('\n')
    print(rows)
    n = len(rows)

    if not (issquare(rows, n)) : 
        return

    pieces = ['P', 'B', 'R', 'Q', 'K']
    kings = [(x, y) for x in range(n) for y in range(n) if rows[x][y] == 'K']
    print(kings)

