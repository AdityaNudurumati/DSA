'''
79. Word Search (Medium)
Problem Statement

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same cell may not
be used more than once.

Example:
Input:
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"

Output:
True
'''


def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx):
        if idx == len(word):              # matched the whole word
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False

        tmp = board[r][c]
        board[r][c] = "#"                 # mark visited

        found = (backtrack(r + 1, c, idx + 1) or
                 backtrack(r - 1, c, idx + 1) or
                 backtrack(r, c + 1, idx + 1) or
                 backtrack(r, c - 1, idx + 1))

        board[r][c] = tmp                 # restore for other paths
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    print(exist(board, "ABCCED"))  # Expected: True
    print(exist(board, "SEE"))     # Expected: True
    print(exist(board, "ABCB"))    # Expected: False


'''
Pattern
✅ Grid Backtracking (DFS with visited marking + restore)
From every cell we DFS in 4 directions, temporarily marking the current cell so
it cannot be reused, then restoring it when the branch unwinds.
| Metric | Value          |
| ------ | -------------- |
| Time   | O(m * n * 4^L) |
| Space  | O(L)           |
Better Possible?
❌ No

Each cell may start a search and each step branches up to 4 ways for L letters;
this is the standard bound.
'''
