#!/usr/bin/env python3

def is_square(rows, n) -> bool:
	if not all(len(r) == n for r in rows) :
		print("ERROR! BOARD IS NOT SQUARE.")
		return False
	return True

def check_kings(kings) -> bool :
	if (len(kings) != 1) :
		print("ERROR! ONLY 1 KING ALLOWED.")
		return False
	return True

def in_bound(x, y, n) -> bool :
	return (0 <= x < n and 0 <= y < n)

def check_pawn(pawn_dir, x, y, k_pos) -> bool :
	for i, j in pawn_dir :
		if ((x+i, y+j) == k_pos) :
			print("Success")
			return True
	return False

def check_other(dir, x, y, k_pos, n, rows, pieces) -> bool :
	for i, j in dir :
		tx, ty = x + i, y + j
		while in_bound(tx, ty, n) :
			if ((tx, ty) == k_pos) :
				print("Success")
				return True
			if (rows[tx][ty] in pieces) :
				break
			tx += i
			ty += j
	return False

def checkmate(board: str) :
	pieces = ['P', 'B', 'R', 'Q', 'K']
	rows = board.strip().split('\n')
	n = len(rows)

	if not (is_square(rows, n)) : 
		return

	kings = [(x, y) for x in range(n) for y in range(n) if rows[x][y] == 'K']
	if not check_kings(kings) :
		return
	king_position = kings[0]

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
				if (check_other(bishop_dir, x, y, king_position, n, rows, pieces)) :
					return
			if (piece == 'R') :
				if (check_other(rook_dir, x, y, king_position, n, rows, pieces)) :
					return
			if (piece == 'Q') :
				if (check_other(queen_dir, x, y, king_position, n, rows, pieces)) :
					return
	print("Fail")