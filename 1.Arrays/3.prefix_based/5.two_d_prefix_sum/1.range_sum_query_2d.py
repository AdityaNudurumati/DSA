'''
1. Range Sum Query 2D - Immutable (Medium)
Problem Statement

Given a 2D matrix, answer many queries sumRegion(r1, c1, r2, c2) = sum of the
submatrix with top-left (r1, c1) and bottom-right (r2, c2), inclusive.
The matrix does not change.

Example
Input:
matrix = [[3,0,1,4,2],
          [5,6,3,2,1],
          [1,2,0,1,5],
          [4,1,0,1,7],
          [1,0,3,0,5]]
sumRegion(2,1,4,3) -> 8
sumRegion(1,1,2,2) -> 11
sumRegion(1,2,2,4) -> 12
'''

class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m else 0

        # prefix[i+1][j+1] = sum of the rectangle from (0,0) to (i,j)
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix[i][j + 1]
                    + self.prefix[i + 1][j]
                    - self.prefix[i][j]
                )

    def sumRegion(self, r1, c1, r2, c2):
        P = self.prefix
        # inclusion-exclusion on the 2D prefix
        return (
            P[r2 + 1][c2 + 1]
            - P[r1][c2 + 1]
            - P[r2 + 1][c1]
            + P[r1][c1]
        )


if __name__ == "__main__":
    nm = NumMatrix([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ])
    print(nm.sumRegion(2, 1, 4, 3))   # Expected: 8
    print(nm.sumRegion(1, 1, 2, 2))   # Expected: 11
    print(nm.sumRegion(1, 2, 2, 4))   # Expected: 12

'''
Pattern
✅ 2D Prefix Sum + Inclusion-Exclusion

Key Observation
region = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
(subtract the top and left strips, add back the doubly-subtracted corner).

| Metric | Value    |
| ------ | -------- |
| Build  | O(m*n)   |
| Query  | O(1)     |
| Space  | O(m*n)   |

Better Possible?
❌ No for many queries.
'''
