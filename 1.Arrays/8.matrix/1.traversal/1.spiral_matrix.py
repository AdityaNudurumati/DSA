'''
1. Spiral Matrix (Medium)
Problem Statement

Given an m x n matrix, return all its elements in spiral order (clockwise, starting
from the top-left).

Example
Input:
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

Output:
[1,2,3,6,9,8,7,4,5]
'''

def spiralOrder(matrix):

    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for c in range(left, right + 1):          # top row, left -> right
            result.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):          # right col, top -> bottom
            result.append(matrix[r][right])
        right -= 1

        if top <= bottom:                         # bottom row, right -> left
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:                         # left col, bottom -> top
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result


if __name__ == "__main__":
    print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    # Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

'''
Pattern
✅ Boundary Traversal (shrink top/bottom/left/right)

| Metric | Value  |
| ------ | ------ |
| Time   | O(m*n) |
| Space  | O(1)   | (excluding the output)

Better Possible?
❌ No. Every cell must be visited.
'''
