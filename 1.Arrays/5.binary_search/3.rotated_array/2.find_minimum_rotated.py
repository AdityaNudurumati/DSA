'''
2. Find Minimum in Rotated Sorted Array (Medium)
Problem Statement

A sorted array of distinct integers was rotated at an unknown pivot. Return the
minimum element in O(log n).

Example
Input:
nums = [3,4,5,1,2]

Output:
1
'''

def findMin(nums):

    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        # compare to the rightmost element to locate the unsorted (lower) half
        if nums[mid] > nums[hi]:
            lo = mid + 1        # minimum is to the right of mid
        else:
            hi = mid            # minimum is at mid or to its left

    return nums[lo]


if __name__ == "__main__":
    print(findMin([3, 4, 5, 1, 2]))         # Expected: 1
    print(findMin([4, 5, 6, 7, 0, 1, 2]))   # Expected: 0
    print(findMin([11, 13, 15, 17]))         # Expected: 11

'''
Pattern
✅ Binary Search against the right boundary

Key Observation
If nums[mid] > nums[hi], the rotation point (and thus the minimum) is strictly to
the right; otherwise it is at mid or to the left. Converges to the pivot.

| Metric | Value    |
| ------ | -------- |
| Time   | O(log n) |
| Space  | O(1)     |

Better Possible?
❌ No.
'''
