'''
1. Rotate Image (Medium)
Problem Statement

Given an n x n matrix representing an image, rotate it 90 degrees clockwise
in-place (do not allocate another matrix).

Example
Input:
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

Output:
[[7,4,1],
 [8,5,2],
 [9,6,3]]
'''

def rotate(matrix):

    n = len(matrix)

    # 1) transpose (swap across the main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2) reverse each row
    for row in matrix:
        row.reverse()

    return matrix


if __name__ == "__main__":
    print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print(rotate([[1, 2], [3, 4]]))
    # Expected: [[3, 1], [4, 2]]

'''
Pattern
✅ Transpose + Reverse rows

Key Observation
Clockwise 90° = transpose, then mirror each row left-to-right. Both steps are
in-place, so no extra matrix is needed.
(Counter-clockwise = transpose, then reverse each COLUMN.)

| Metric | Value  |
| ------ | ------ |
| Time   | O(n²)  |
| Space  | O(1)   |

Better Possible?
❌ No. Every cell must move.
'''
