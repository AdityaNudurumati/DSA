'''
1. Number of Increasing Paths in a Grid (Hard) — LC2328
Problem Statement

You are given an m x n integer matrix grid, where you can move from a cell to any
adjacent cell in all 4 directions. Return the number of strictly increasing paths in
the grid, where you can start from any cell and end at any cell. Since the answer may
be very large, return it modulo 10^9 + 7.

Two paths are considered different if they do not have exactly the same sequence of
visited cells.

Example
Input:
grid = [[1,1],[3,4]]

Output:
8
Explanation:
The strictly increasing paths are:
- Length 1 paths (each single cell): 1, 1, 3, 4 -> 4 paths.
- Length 2 paths: (1->3), (1->4), (3->4), (1->4) -> 4 paths.
Total = 4 + 4 = 8.
'''

import sys
from functools import lru_cache

MOD = 10 ** 9 + 7


def countPaths(grid):

    m, n = len(grid), len(grid[0])

    # DAG DP / path counting:
    #   Edges go only from a cell to a strictly larger neighbour, so the graph is a DAG.
    # state:      f(r, c) = number of strictly increasing paths that START at cell (r, c).
    # transition: f(r, c) = 1 + sum( f(nr, nc) ) for each neighbour with grid[nr][nc] > grid[r][c].
    #             (the leading 1 counts the length-1 path consisting of (r, c) alone.)
    # base:       a cell with no larger neighbour contributes only itself -> f = 1.
    @lru_cache(maxsize=None)
    def f(r, c):
        total = 1  # the single-cell path starting (and ending) here
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                total += f(nr, nc)
        return total % MOD

    # answer = sum over every possible starting cell
    ans = 0
    for r in range(m):
        for c in range(n):
            ans = (ans + f(r, c)) % MOD
    return ans


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 20)
    print(countPaths([[1, 1], [3, 4]]))  # Expected: 8
    print(countPaths([[1], [2]]))        # Expected: 3

'''
Pattern
✅ Graph DP — DAG path counting via memoized DFS

Which DP & why
Because moves are only allowed to a strictly greater value, the implicit graph over
cells is a Directed Acyclic Graph (no cell can be revisited along an increasing path).
On a DAG we can define f(cell) = number of increasing paths starting at that cell and
fill it bottom-up with memoization: a path starting here is either just this cell, or
this cell followed by any increasing path starting at a larger neighbour. Summing
f(cell) over all starting cells gives every increasing path exactly once. Memoization
ensures each cell's subproblem is solved a single time.

| Metric | Value     |
| ------ | --------- |
| Time   | O(m * n)  |
| Space  | O(m * n)  |

Better Possible?
❌ No (asymptotically). Each cell has at most 4 outgoing edges, so the DAG has O(m*n)
nodes and edges; every cell must be visited at least once, making O(m*n) optimal.
'''
