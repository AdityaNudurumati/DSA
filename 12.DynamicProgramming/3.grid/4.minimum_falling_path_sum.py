"""
931. Minimum Falling Path Sum (Medium)

Problem Statement:
Given an n x n array of integers, return the minimum sum of any falling path.
A falling path starts at any element in the first row and chooses the element
in the next row that is either directly below, diagonally left, or diagonally
right (column index differs by at most one).

Example:
    Input:  [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13

    Input:  [[-19,57],[-40,-5]]
    Output: -59
"""


def min_falling_path_sum(matrix):
    n = len(matrix)

    # State: dp[r][c] = minimum falling-path sum ending at cell (r, c).
    dp = [row[:] for row in matrix]          # Base: first row = its own values.

    for r in range(1, n):
        for c in range(n):
            # Transition: best of the (up to) three cells above that can fall here.
            best = dp[r - 1][c]
            if c > 0:
                best = min(best, dp[r - 1][c - 1])
            if c < n - 1:
                best = min(best, dp[r - 1][c + 1])
            dp[r][c] = matrix[r][c] + best

    return min(dp[n - 1])


if __name__ == "__main__":
    print(min_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # Expected: 13
    print(min_falling_path_sum([[-19, 57], [-40, -5]]))            # Expected: -59


"""
Pattern: GRID DP — falling-path variant (tabulation).
Why: the cheapest path landing on (r, c) extends one of the (at most) three
cells above it: dp[r][c] = matrix[r][c] + min(dp[r-1][c-1], dp[r-1][c],
dp[r-1][c+1]). The answer is the minimum across the final row.

| Metric | Value      |
|--------|------------|
| Time   | O(n^2)     |
| Space  | O(n^2)     |

Better Possible?
Time is optimal (every cell contributes). Space reduces to O(n) by keeping only
the previous row, or O(1) extra by overwriting the input matrix in place.
"""
