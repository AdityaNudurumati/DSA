'''
4. Median of Two Sorted Arrays (Hard)
Problem Statement

Given two sorted arrays nums1 and nums2, return the median of the combined sorted
array. Must run in O(log(min(m, n))).

Example
Input:
nums1 = [1,3], nums2 = [2]      -> 2.0
nums1 = [1,2], nums2 = [3,4]    -> 2.5
'''

def findMedianSortedArrays(nums1, nums2):

    A, B = nums1, nums2
    if len(A) > len(B):          # always binary-search the shorter array
        A, B = B, A

    m, n = len(A), len(B)
    total = m + n
    half = (total + 1) // 2      # size of the combined left part

    lo, hi = 0, m
    while lo <= hi:

        i = (lo + hi) // 2       # how many taken from A
        j = half - i             # how many taken from B

        A_left  = A[i - 1] if i > 0 else float("-inf")
        A_right = A[i]     if i < m else float("inf")
        B_left  = B[j - 1] if j > 0 else float("-inf")
        B_right = B[j]     if j < n else float("inf")

        if A_left <= B_right and B_left <= A_right:
            # correct partition found
            if total % 2:
                return float(max(A_left, B_left))
            return (max(A_left, B_left) + min(A_right, B_right)) / 2

        elif A_left > B_right:
            hi = i - 1           # took too many from A
        else:
            lo = i + 1           # took too few from A


if __name__ == "__main__":
    print(findMedianSortedArrays([1, 3], [2]))      # Expected: 2.0
    print(findMedianSortedArrays([1, 2], [3, 4]))   # Expected: 2.5
    print(findMedianSortedArrays([], [1]))           # Expected: 1.0

'''
Pattern
✅ Binary Search on the Partition (search on index of the cut)

Key Observation
Find a cut so that everything left of both cuts <= everything right. Binary search
the cut position in the shorter array; the other cut is fixed by the half size.

| Metric | Value             |
| ------ | ----------------- |
| Time   | O(log(min(m, n))) |
| Space  | O(1)              |

Better Possible?
❌ No. Merging would be O(m + n).
'''
