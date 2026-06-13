'''
3. Search a 2D Matrix (Medium)
Problem Statement

Given an m x n matrix where each row is sorted left-to-right and the first integer
of each row is greater than the last integer of the previous row, determine if a
target value exists. Must run in O(log(m*n)).

Example
Input:
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 3

Output:
True
'''

def searchMatrix(matrix, target):

    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])

    # treat the matrix as one sorted array of length m*n
    lo, hi = 0, m * n - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]      # map 1D index -> 2D cell

        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


if __name__ == "__main__":
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(searchMatrix(m, 3))    # Expected: True
    print(searchMatrix(m, 13))   # Expected: False

'''
Pattern
✅ Binary Search on a flattened sorted matrix

Key Observation
The ordering means the matrix is one sorted sequence. Index i maps to cell
(i // n, i % n), so a standard binary search works without flattening it for real.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(log(m*n))   |
| Space  | O(1)          |

Better Possible?
❌ No for this ordering. (A row/col-sorted-only matrix uses O(m+n) staircase search.)
'''
