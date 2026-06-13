'''
329. Longest Increasing Path in a Matrix (Hard)
Problem Statement

Given an m x n integers matrix, return the length of the longest increasing path
in matrix. From each cell you may move in four directions: left, right, up, or down.
You may NOT move diagonally or move outside the boundary (i.e., wrapping around is
not allowed). Each step must move to a strictly greater value.

Input:
matrix = [[9,9,4],
          [6,6,8],
          [2,1,1]]

Output:
4

Explanation:
The longest increasing path is [1, 2, 6, 9].
'''

# The "move to a strictly greater value" rule means edges always point from a smaller
# value to a larger value, so the implied graph is a DAG (no cycles possible).
# longest path from a cell = 1 + max(longest path of strictly-greater neighbours).
# Memoize each cell so every cell is solved once -> O(m*n).

def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    memo = [[0] * cols for _ in range(rows)]  # 0 = not computed yet
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c):
        if memo[r][c]:
            return memo[r][c]

        best = 1  # the cell itself is a path of length 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # only step toward a strictly greater value -> guarantees a DAG
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))

        memo[r][c] = best
        return best

    return max(dfs(r, c) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    matrix1 = [[9, 9, 4],
               [6, 6, 8],
               [2, 1, 1]]
    print(longestIncreasingPath(matrix1))  # Expected: 4

    matrix2 = [[3, 4, 5],
               [3, 2, 6],
               [2, 2, 1]]
    print(longestIncreasingPath(matrix2))  # Expected: 4


'''
Pattern
✅ Graph DP (memoized DFS on an implicit DAG)
The strictly-increasing rule forbids cycles, so the cells form a DAG. Longest path on a
DAG is solved by relaxing along that order; here memoized DFS computes each cell once.
| Metric | Value    |
| ------ | -------- |
| Time   | O(m * n) |
| Space  | O(m * n) |
Better Possible?
❌ No
Every cell must be examined at least once, so O(m*n) is optimal. The memo removes the
exponential blow-up of naive DFS; topological-order DP would match this bound, not beat it.
'''
