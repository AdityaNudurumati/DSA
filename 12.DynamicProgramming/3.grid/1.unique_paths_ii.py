"""
63. Unique Paths II (Medium)

Problem Statement:
A robot is located at the top-left corner of an m x n grid and can only move
either down or right. Some cells contain obstacles (marked 1); a path cannot
pass through an obstacle. Count the number of distinct paths from the top-left
corner to the bottom-right corner.

Example:
    Input:  [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2

    Input:  [[0,1],[0,0]]
    Output: 1
"""

# (Cross-referenced to Recursion: Unique Paths I is the obstacle-free version.)


def unique_paths_with_obstacles(grid):
    m, n = len(grid), len(grid[0])

    # State: dp[r][c] = number of distinct paths reaching cell (r, c).
    dp = [[0] * n for _ in range(m)]

    # Base: the start cell has 1 path, unless it is itself an obstacle.
    dp[0][0] = 0 if grid[0][0] == 1 else 1

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                dp[r][c] = 0          # obstacle => unreachable
                continue
            if (r, c) == (0, 0):
                continue              # already set as base
            # Transition: paths come only from above or from the left.
            top = dp[r - 1][c] if r else 0
            left = dp[r][c - 1] if c else 0
            dp[r][c] = top + left

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # Expected: 2
    print(unique_paths_with_obstacles([[0, 1], [0, 0]]))                    # Expected: 1


"""
Pattern: GRID DP — tabulation.
Why: each cell's path count depends only on the cell above and to the left,
giving the recurrence dp[r][c] = dp[r-1][c] + dp[r][c-1] (0 at obstacles).
A bottom-up 2D table fills these dependencies in row-major order.

| Metric | Value      |
|--------|------------|
| Time   | O(m * n)   |
| Space  | O(m * n)   |

Better Possible?
Time is optimal (every cell must be inspected). Space can be reduced to O(n)
by keeping a single rolling row, since each row depends only on the previous one.
"""
