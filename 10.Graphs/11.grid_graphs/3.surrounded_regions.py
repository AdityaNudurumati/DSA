"""
130. Surrounded Regions (Medium)

Problem Statement:
Given an m x n matrix board containing 'X' and 'O', capture all regions that are
4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into
'X's in that surrounded region. Any 'O' connected to a border can never be
surrounded, so it (and everything reachable from it) survives.

Example:
    Input:  [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]]
    Output: [["X","X","X","X"],
             ["X","X","X","X"],
             ["X","X","X","X"],
             ["X","O","X","X"]]
"""


def solve(board):
    # Border DFS: any 'O' reachable from an edge is safe. Mark all such cells with
    # a sentinel, then flip the remaining (truly surrounded) 'O's to 'X'.
    if not board or not board[0]:
        return board
    m, n = len(board), len(board[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c):
        if not (0 <= r < m and 0 <= c < n) or board[r][c] != 'O':
            return
        board[r][c] = '#'                     # mark border-connected (safe)
        for dr, dc in dirs:
            dfs(r + dr, c + dc)

    # Launch DFS from every 'O' on the four borders.
    for r in range(m):
        dfs(r, 0)
        dfs(r, n - 1)
    for c in range(n):
        dfs(0, c)
        dfs(m - 1, c)

    # Capture interior 'O's; restore the safe ones marked '#'.
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'X'             # surrounded -> captured
            elif board[r][c] == '#':
                board[r][c] = 'O'             # border-connected -> restored
    return board


if __name__ == "__main__":
    b1 = [["X", "X", "X", "X"],
          ["X", "O", "O", "X"],
          ["X", "X", "O", "X"],
          ["X", "O", "X", "X"]]
    print(solve(b1))
    # Expected: [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]

"""
Pattern: Grid Graph / Region Capture (border DFS / reverse flood fill).
Technique: rather than testing each region for being surrounded, flood-fill from
the borders to flag every 'O' that escapes to an edge. Whatever is left unflagged
is necessarily enclosed and gets flipped to 'X'; flagged cells revert to 'O'.
Why: an 'O' survives iff it is connected to the boundary, so seeding DFS only from
border 'O's identifies exactly the safe component in one pass.

| Metric | Value     |
|--------|-----------|
| Time   | O(m * n)  |
| Space  | O(m * n)  |   recursion stack worst case

Better Possible?
No — must visit every cell. Iterative BFS or Union-Find (union border 'O's to a
virtual node) gives the same O(m*n) without recursion depth concerns.
"""
