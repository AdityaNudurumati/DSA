'''
1. Valid Sudoku (Medium/Hard)
Problem Statement

Determine if a partially filled 9x9 Sudoku board is valid. Only the filled cells
('1'-'9'; '.' = empty) need to be checked: each row, each column, and each of the
nine 3x3 boxes must contain no duplicate digit. The board need not be solvable.

Example
Input: a board whose filled cells have no row/col/box duplicate -> True
       a board with a repeated digit in a row/col/box           -> False
'''

def isValidSudoku(board):

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]      # box index = (r//3)*3 + c//3

    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            b = (r // 3) * 3 + c // 3
            if v in rows[r] or v in cols[c] or v in boxes[b]:
                return False                # duplicate in row, column, or box
            rows[r].add(v)
            cols[c].add(v)
            boxes[b].add(v)

    return True


if __name__ == "__main__":
    valid = [
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
    print(isValidSudoku(valid))                 # Expected: True

    invalid = [row[:] for row in valid]
    invalid[0][0] = "8"                          # clashes with the 8 in the same column/box
    print(isValidSudoku(invalid))               # Expected: False

'''
Pattern
✅ Set-Based Hashing (one set per row / column / box)

Key Observation
Nine row-sets, nine column-sets, nine box-sets give O(1) duplicate checks in a single
pass. Box index = (row // 3) * 3 + (col // 3).

| Metric | Value |
| ------ | ----- |
| Time   | O(81) = O(1) |
| Space  | O(81) = O(1) |

Better Possible?
❌ Every filled cell must be inspected once.
'''
