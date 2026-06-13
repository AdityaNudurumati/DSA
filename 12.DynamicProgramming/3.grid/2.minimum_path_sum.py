"""
64. Minimum Path Sum (Medium)

Problem Statement:
Given an m x n grid filled with non-negative numbers, find a path from the
top-left to the bottom-right which minimizes the sum of all numbers along the
path. You can only move either down or right at any point in time.

Example:
    Input:  [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7

    Input:  [[1,2,3],[4,5,6]]
    Output: 12
"""


def min_path_sum(grid):
    m, n = len(grid), len(grid[0])

    # State: dp[r][c] = minimum cost to reach (r, c) from (0, 0).
    dp = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if (r, c) == (0, 0):
                dp[r][c] = grid[r][c]          # Base: start cell.
                continue
            best = float("inf")
            if r:                              # come from above
                best = min(best, dp[r - 1][c])
            if c:                              # come from the left
                best = min(best, dp[r][c - 1])
            # Transition: add current cost to the cheaper incoming path.
            dp[r][c] = best + grid[r][c]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # Expected: 7
    print(min_path_sum([[1, 2, 3], [4, 5, 6]]))             # Expected: 12


"""
Pattern: GRID DP — tabulation.
Why: the cheapest way to stand on (r, c) is its own cost plus the cheaper of the
two cells that can reach it: dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]).
Optimal substructure + overlapping subproblems => DP.

| Metric | Value      |
|--------|------------|
| Time   | O(m * n)   |
| Space  | O(m * n)   |

Better Possible?
Time is optimal — each cell is read once. Space reduces to O(n) using a single
rolling row updated in place.
"""
