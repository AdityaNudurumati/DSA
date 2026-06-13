'''
1. Search in Rotated Sorted Array (Medium)
Problem Statement

A sorted array of distinct integers was rotated at an unknown pivot. Given the
rotated array nums and a target, return its index, or -1. Must run in O(log n).

Example
Input:
nums = [4,5,6,7,0,1,2], target = 0

Output:
4
'''

def search(nums, target):

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid

        # one side is always properly sorted — figure out which
        if nums[lo] <= nums[mid]:                 # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                     # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))   # Expected: 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3))   # Expected: -1
    print(search([1], 0))                      # Expected: -1

'''
Pattern
✅ Modified Binary Search (identify the sorted half each step)

Key Observation
After a rotation, at least one half [lo..mid] or [mid..hi] is still sorted. Check
whether target lies inside that sorted half; recurse accordingly.

| Metric | Value    |
| ------ | -------- |
| Time   | O(log n) |
| Space  | O(1)     |

Better Possible?
❌ No.
'''
