"""
120. Triangle (Medium)

Problem Statement:
Given a triangle array, return the minimum path sum from top to bottom. At each
step you may move to an adjacent number of the row below; from index i in the
current row you may move to index i or i + 1 in the next row.

Example:
    Input:  [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11

    Input:  [[-10]]
    Output: -10
"""


def minimum_total(triangle):
    # Work bottom-up so each cell has exactly two well-defined children.
    # State: dp[c] = minimum path sum from row r, column c down to the base.
    dp = triangle[-1][:]                     # Base: last row is its own value.

    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            # Transition: add current value to the cheaper of its two children.
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])

    return dp[0]


if __name__ == "__main__":
    print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # Expected: 11
    print(minimum_total([[-10]]))                                  # Expected: -10


"""
Pattern: GRID DP — triangle / bottom-up tabulation.
Why: defining the answer from the bottom row upward gives each cell exactly two
children, yielding dp[c] = triangle[r][c] + min(dp[c], dp[c+1]); the result
collapses into dp[0]. Going top-down would force handling the two boundary edges
that only have one parent.

| Metric | Value      |
|--------|------------|
| Time   | O(n^2)     |
| Space  | O(n)       |

Better Possible?
Time is optimal (each of the ~n^2/2 cells is touched once). Space is already
O(n) via the single rolling array; it can be made O(1) extra by reusing the
triangle's last row in place.
"""
