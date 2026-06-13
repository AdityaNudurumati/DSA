'''
5. Unique Paths (Medium)   [LC62]
Problem Statement

A robot is located at the top-left corner of an m x n grid. It can only
move either down or right at any point in time. The robot is trying to
reach the bottom-right corner.

Return the number of unique paths.

Input:
m = 3, n = 7

Output:
28

Explanation:
There are 28 distinct down/right paths from top-left to bottom-right.
'''

from functools import lru_cache


def uniquePaths(m, n):
    # paths(r, c) = ways to reach bottom-right from cell (r, c)
    @lru_cache(maxsize=None)
    def paths(r, c):
        if r == m - 1 or c == n - 1:     # last row or column: one straight path
            return 1
        return paths(r + 1, c) + paths(r, c + 1)  # move down or right

    return paths(0, 0)


if __name__ == "__main__":
    print(uniquePaths(3, 7))  # Expected: 28
    print(uniquePaths(3, 2))  # Expected: 3


'''
Pattern
✅ Recursive DP (Memoization)
The state is the cell (r, c); each cell is reached from above and from the
left, so caching paths(r, c) turns the branching recursion into O(m*n) work.
| Metric | Value    |
| ------ | -------- |
| Time   | O(m * n) |
| Space  | O(m * n) |
Better Possible?
✅ Yes
The answer is the binomial C(m+n-2, m-1), computable in O(min(m, n)) time
and O(1) space.
'''
