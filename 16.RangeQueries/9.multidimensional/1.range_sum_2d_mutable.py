'''
308. Range Sum Query 2D - Mutable (Hard)
Problem Statement

Given a 2D matrix, support two operations efficiently:
  1. update(row, col, val)              set matrix[row][col] = val.
  2. sumRegion(r1, c1, r2, c2)          sum of the rectangle whose upper-left
                                        corner is (r1, c1) and lower-right
                                        corner is (r2, c2), inclusive.

Implement the NumMatrix class:
  - NumMatrix(matrix)
  - update(row, col, val)
  - sumRegion(row1, col1, row2, col2)

Use a 2D Fenwick / Binary Indexed Tree so updates and queries are both fast.

Example
Input:
  matrix = [[3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]]
  sumRegion(2, 1, 4, 3)   -> 8
  update(3, 2, 2)
  sumRegion(2, 1, 4, 3)   -> 10
'''


# ---- Solution: 2D Fenwick / Binary Indexed Tree (1-indexed on both axes) ----
class NumMatrix:
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows else 0
        # Keep a live copy so update() can apply only the delta (new - old).
        self.vals = [[0] * self.cols for _ in range(self.rows)]
        # tree[i][j] is 1-indexed on both dimensions -> +1 padding each way.
        self.tree = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])

    def _add(self, row, col, delta):
        # row, col are 1-indexed; walk both axes by the lowest set bit.
        i = row
        while i <= self.rows:
            j = col
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def _prefix(self, row, col):
        # Sum of the rectangle (1,1)..(row,col) in 1-indexed coordinates.
        s = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                s += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return s

    def update(self, row, col, val):
        # Apply the delta so the tree stays consistent with vals.
        delta = val - self.vals[row][col]
        self.vals[row][col] = val
        self._add(row + 1, col + 1, delta)

    def sumRegion(self, row1, col1, row2, col2):
        # Inclusion-exclusion over four prefix rectangles (shift to 1-indexed).
        return (self._prefix(row2 + 1, col2 + 1)
                - self._prefix(row1, col2 + 1)
                - self._prefix(row2 + 1, col1)
                + self._prefix(row1, col1))


if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    nm = NumMatrix(matrix)
    print(nm.sumRegion(2, 1, 4, 3))   # Expected: 8
    nm.update(3, 2, 2)
    print(nm.sumRegion(2, 1, 4, 3))   # Expected: 10

'''
Pattern
2D Fenwick Tree / Binary Indexed Tree (point update + rectangle sum)

Structure & why
A 1D BIT stores partial prefix sums keyed by the lowest set bit. Nesting one BIT
inside another extends this to 2D: tree[i][j] is responsible for the rectangle
(i-(i&-i), i] x (j-(j&-j), j]. Updating walks i += i&-i AND j += j&-j (an outer
and inner loop), touching O(log rows * log cols) cells. A prefix query reads the
rectangle (1,1)..(r,c) by walking both indices downward. An arbitrary rectangle
sum follows from 2D inclusion-exclusion of four such prefixes:
  region = P(r2,c2) - P(r1-1,c2) - P(r2,c1-1) + P(r1-1,c1-1).
We store a live copy of the matrix so update() applies only (new - old), the
same delta trick that keeps the 1D BIT consistent. Everything is 1-indexed, so
real coordinates are shifted by +1 and the exclusion terms use the unshifted
row1/col1 as the "minus one" prefixes.

| Metric     | Value             |
| ---------- | ----------------- |
| Build      | O(rows*cols*log rows*log cols) |
| update     | O(log rows * log cols)         |
| sumRegion  | O(log rows * log cols)         |
| Space      | O(rows * cols)    |

Better Possible?
A static matrix (no updates) is better served by a plain 2D prefix-sum array:
O(rows*cols) build and O(1) query. With updates, the 2D BIT is the standard
choice -- a 2D segment tree matches the asymptotics but uses ~4x the memory and
much more code. Build can be dropped to O(rows*cols) with a per-axis linear BIT
construction if the initial load dominates.
'''
