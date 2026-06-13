'''
2. Diagonal Traverse (Medium)
Problem Statement

Given an m x n matrix, return all elements in a zig-zag diagonal order: diagonals
alternate direction, the first going up-right.

Example
Input:
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

Output:
[1,2,4,7,5,3,6,8,9]
'''

def findDiagonalOrder(mat):

    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    result = []

    # there are m + n - 1 diagonals; index d = r + c is constant on a diagonal
    for d in range(m + n - 1):

        if d % 2 == 0:                       # even diagonal -> travel up-right
            r = min(d, m - 1)
            c = d - r
            while r >= 0 and c < n:
                result.append(mat[r][c])
                r -= 1
                c += 1
        else:                                # odd diagonal -> travel down-left
            c = min(d, n - 1)
            r = d - c
            while c >= 0 and r < m:
                result.append(mat[r][c])
                r += 1
                c -= 1

    return result


if __name__ == "__main__":
    print(findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: [1, 2, 4, 7, 5, 3, 6, 8, 9]
    print(findDiagonalOrder([[1, 2], [3, 4]]))
    # Expected: [1, 2, 3, 4]

'''
Pattern
✅ Diagonal Traversal (group by r + c, alternate direction)

| Metric | Value  |
| ------ | ------ |
| Time   | O(m*n) |
| Space  | O(1)   | (excluding the output)

Better Possible?
❌ No.
'''
