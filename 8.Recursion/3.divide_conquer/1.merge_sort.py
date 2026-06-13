"""
1. Merge Sort (Easy/Medium)

Problem Statement
-----------------
Sort an array of integers in ascending order using the Merge Sort algorithm.

Merge Sort is the canonical divide & conquer sort: split the array into two
halves, recursively sort each half, then merge the two sorted halves into a
single sorted array.

Example
-------
Input:  [5, 2, 8, 1, 9, 3]
Output: [1, 2, 3, 5, 8, 9]
"""


def merge_sort(a):
    # Base case: 0 or 1 element is already sorted.
    if len(a) <= 1:
        return a[:]

    # Divide: split into two halves.
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    # Conquer + Combine: merge the two sorted halves.
    return _merge(left, right)


def _merge(left, right):
    merged = []
    i = j = 0
    # Walk both halves, always taking the smaller front element.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= keeps the sort stable
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # One side may have leftovers; append them as-is (already sorted).
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    print(merge_sort([5, 2, 8, 1, 9, 3]))  # Expected: [1, 2, 3, 5, 8, 9]
    print(merge_sort([]))                   # Expected: []
    print(merge_sort([1]))                  # Expected: [1]
    print(merge_sort([3, 3, 1]))            # Expected: [1, 3, 3]


"""
Pattern
-------
Divide & Conquer (Merge Sort). Recursively halve the array until single
elements remain (trivially sorted), then merge sorted halves bottom-up. The
real work lives in the combine/merge step, which interleaves two sorted lists
in linear time. The split is balanced (always at the midpoint), giving the
recurrence T(n) = 2T(n/2) + O(n), which by the Master Theorem is O(n log n).
This implementation uses `<=` in the merge to preserve stability.

| Metric          | Value      |
| --------------- | ---------- |
| Time            | O(n log n) |
| Space           | O(n)       |

Better Possible?
----------------
O(n log n) is optimal for comparison-based sorting (the comparison-sort lower
bound is Omega(n log n)), so the time cannot be improved asymptotically in the
general case. The O(n) auxiliary space can be reduced: an in-place merge sort
trades extra memory for more complex (and slower-constant) merging, while
heapsort sorts in O(n log n) time with O(1) extra space but is not stable.
Quicksort has the same average time with better cache behavior but O(n^2)
worst case. For integers specifically, a non-comparison sort like radix/counting
sort can reach O(n) time when the key range is bounded.
"""
