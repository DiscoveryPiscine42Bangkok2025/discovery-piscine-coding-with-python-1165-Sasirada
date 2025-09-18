#!/usr/bin/env python3

def is_square(rows, n) -> bool:
    if not all(len(r) == n for r in rows) :
        print("ERROR! BOARD IS NOT SQUARE.")
        return False
    return True

def is_empty(cell) -> bool :
    pieces = ['P', 'B', 'R', 'Q', 'K']
    if cell not in pieces

def check_kings(kings) -> bool :
    if (len(kings) != 1) :
        print("ERROR! MORE THAN 1 KING.")
        return False
    return True

def check_pawn(dir, rows, cur_x, cur_y, k_pos) -> bool :
    for x, y in dir :
        if (cur_x + x, cur_y) == k_pos :
            return True
    return False

def checkmate(board: str) :
    rows = board.strip().split('\n')
    print(rows)
    n = len(rows)

    if not (is_square(rows, n)) : 
        return

    if not (is_empty(rows, n)) :
        return

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
                if (check_piece(pawn_dir, rows)) :
                    print("Success")
                    return