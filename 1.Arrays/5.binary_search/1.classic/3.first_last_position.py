'''
3. Find First and Last Position of Element in Sorted Array (Medium)
Problem Statement

Given a sorted array nums (with possible duplicates) and a target, return the first
and last index of target as [first, last]. If absent, return [-1, -1]. O(log n).

Example
Input:
nums = [5,7,7,8,8,10], target = 8

Output:
[3,4]
'''

def searchRange(nums, target):

    def lower_bound(t):
        # first index with nums[index] >= t
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(target)

    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    # last occurrence = (first index > target) - 1
    last = lower_bound(target + 1) - 1
    return [first, last]


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))   # Expected: [3, 4]
    print(searchRange([5, 7, 7, 8, 8, 10], 6))   # Expected: [-1, -1]
    print(searchRange([], 0))                     # Expected: [-1, -1]

'''
Pattern
✅ Two Lower-Bound Binary Searches

Key Observation
first = lower_bound(target); last = lower_bound(target + 1) - 1.
Reusing one lower-bound helper keeps both edges correct with duplicates.

| Metric | Value    |
| ------ | -------- |
| Time   | O(log n) |
| Space  | O(1)     |

Better Possible?
❌ No.
'''
