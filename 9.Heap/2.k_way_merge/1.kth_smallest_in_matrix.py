'''
378. Kth Smallest in a Sorted Matrix (Medium)
Problem Statement

Given an n x n matrix where each of the rows and columns is sorted in ascending
order, return the kth smallest element in the matrix. Note that it is the kth
smallest element in sorted order, not the kth distinct element.

Example
Input:
matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8

Output:
13
'''

import heapq

def kthSmallest(matrix, k):
    n = len(matrix)

    # seed the heap with the front of each row: (value, row, col)
    heap = [(matrix[r][0], r, 0) for r in range(min(n, k))]
    heapq.heapify(heap)

    val = None
    # pop k times; each pop refills from the same row (k-way merge of sorted rows)
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c + 1 < len(matrix[r]):
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return val


if __name__ == "__main__":
    print(kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # Expected: 13
    print(kthSmallest([[-5]], 1))                                   # Expected: -5

'''
Pattern
K-Way Merge — treat each sorted row as one of k sorted lists and merge them
with a min-heap, popping k times to reach the kth smallest globally.

Why: the next smallest unseen element is always the front of some row, so a
min-heap of the current row fronts gives O(log k) access to it. We never need
to materialize the full sorted order — only the first k pops.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(k log n)    |
| Space  | O(n)          |

Better Possible?
✅ Yes. Binary search on the value range with a "count <= mid" check runs in
O(n log(max-min)) and avoids the k dependence, which wins when k is large.
'''
