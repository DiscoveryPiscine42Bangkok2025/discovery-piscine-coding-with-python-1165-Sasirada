#!/usr/bin/env python3

def is_square(rows, n) -> bool:
    if not all(len(r) == n for r in rows) :
        print("ERROR! BOARD IS NOT SQUARE.")
        return False
    return True

# def is_empty(rows, n) -> bool :
#     pieces = ['P', 'B', 'R', 'Q', 'K']
#     if cell not in pieces

def check_kings(kings) -> bool :
    if (len(kings) != 1) :
        print("ERROR! MORE THAN 1 KING.")
        return False
    return True

def in_bound(x, y, n) :
    return (0 <= x < n and 0 <= y < n)

def check_pawn(pawn_dir, x, y, k_pos) -> bool :
    for i, j in pawn_dir :
        if ((x+i, y+j) == k_pos) :
            print("Success")
            return True
    return False

def check_other(dir, x, y, k_pos, n) -> bool :
    for i, j in dir :
        while in_bound(x, y, n) :
            x += i
            j += j
            if ((x, y) == k_pos) :
                print("Success")
                return True
    return False

def checkmate(board: str) :
    rows = board.strip().split('\n')
    print(rows)
    n = len(rows)

    if not (is_square(rows, n)) : 
        return

    # if not (is_empty(rows, n)) :
    #     return

    pieces = ['P', 'B', 'R', 'Q', 'K']
    kings = [(x, y) for x in range(n) for y in range(n) if rows[x][y] == 'K']
    print("Kings found:", kings)
    if not check_kings(kings) :
        return
    king_position = kings[0]
    print("Kings position:", kings)

    pawn_dir = [(-1, -1), (-1, 1)]
    bishop_dir = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queen_dir = bishop_dir + rook_dir

    for x in range(n) :
        for y in range(n) :
            piece = rows[x][y]
            if piece not in pieces :
                continue
            if (piece == 'P') :
                if (check_pawn(pawn_dir, x, y, king_position)) :
                    return
            if (piece == 'B') :
                if (check_other(bishop_dir, x, y, king_position, n)) :
                    return
            if (piece == 'R') :
                if (check_other(rook_dir, x, y, king_position, n)) :
                    return
            if (piece == 'Q') :
                if (check_other(queen_dir, x, y, king_position, n)) :
                    return