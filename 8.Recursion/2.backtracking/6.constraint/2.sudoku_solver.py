'''
37. Sudoku Solver (Hard)
Problem Statement

Write a program to solve a Sudoku puzzle by filling the empty cells (denoted by
'.'). Each of the digits 1-9 must occur exactly once in each row, each column,
and each of the nine 3x3 sub-boxes. There is exactly one valid solution.

The board is solved in place.

Example:
Input:  a standard solvable 9x9 puzzle (empty cells are '.')
Output: the same grid fully filled so every row, column, and box holds 1..9.
'''


def solveSudoku(board):
    def is_valid(r, c, ch):
        box_r, box_c = 3 * (r // 3), 3 * (c // 3)
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False
            # scan the 3x3 box
            if board[box_r + i // 3][box_c + i % 3] == ch:
                return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for ch in "123456789":
                        if is_valid(r, c, ch):
                            board[r][c] = ch      # choose
                            if backtrack():       # explore
                                return True
                            board[r][c] = "."     # un-choose
                    return False                  # no digit fits -> dead end
        return True                               # no empty cell -> solved

    backtrack()


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    solveSudoku(board)
    for row in board:
        print("".join(row))
    # Expected:
    # 534678912
    # 672195348
    # 198342567
    # 859761423
    # 426853791
    # 713924856
    # 961537284
    # 287419635
    # 345286179

    # sanity check: each row is a permutation of 1..9
    ok = all(sorted(row) == list("123456789") for row in board)
    print(ok)  # Expected: True


'''
Pattern
✅ Constraint Satisfaction Backtracking
For each empty cell we try digits 1..9, validate against the row/column/3x3 box,
recurse, and undo on failure until the whole grid is consistent.
| Metric | Value    |
| ------ | -------- |
| Time   | O(9^(81)) |
| Space  | O(1)     |
Better Possible?
❌ No

The board is fixed 9x9 so it is effectively constant; constraint pruning makes
it fast in practice and this is the canonical approach.
'''
