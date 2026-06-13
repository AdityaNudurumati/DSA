'''
1. Set Matrix Zeroes (Medium)
Problem Statement

Given an m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place using O(1) extra space.

Example
Input:
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]

Output:
[[1,0,1],
 [0,0,0],
 [1,0,1]]
'''

def setZeroes(matrix):

    m, n = len(matrix), len(matrix[0])

    # use row 0 and col 0 as marker storage; track their own state separately
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # mark: if cell is 0, flag its row (col 0) and column (row 0)
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # apply marks to the interior
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # finally handle the first row / first col themselves
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    # Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
    # Expected: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

'''
Pattern
✅ In-place marking using the first row & column

Key Observation
Reuse row 0 / col 0 as the "should this row/col be zeroed" flags, so no extra
O(m+n) array is needed. Just remember their original state first.

| Metric | Value  |
| ------ | ------ |
| Time   | O(m*n) |
| Space  | O(1)   |

Better Possible?
❌ No. O(1) space is the tight target.
'''
