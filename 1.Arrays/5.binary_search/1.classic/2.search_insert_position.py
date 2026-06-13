'''
2. Search Insert Position (Easy)
Problem Statement

Given a sorted array of distinct integers and a target, return the index if found.
If not, return the index where it would be inserted to keep the array sorted.

Example
Input:
nums = [1,3,5,6], target = 5  -> 2
nums = [1,3,5,6], target = 2  -> 1
nums = [1,3,5,6], target = 7  -> 4
'''

def searchInsert(nums, target):

    # lower bound: first index with nums[index] >= target
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo


if __name__ == "__main__":
    print(searchInsert([1, 3, 5, 6], 5))   # Expected: 2
    print(searchInsert([1, 3, 5, 6], 2))   # Expected: 1
    print(searchInsert([1, 3, 5, 6], 7))   # Expected: 4
    print(searchInsert([1, 3, 5, 6], 0))   # Expected: 0

'''
Pattern
✅ Lower-Bound Binary Search (half-open lo..hi)

Key Observation
The insert position is exactly the lower bound — the first slot whose value is
>= target. The half-open [lo, hi) form returns it directly.

| Metric | Value    |
| ------ | -------- |
| Time   | O(log n) |
| Space  | O(1)     |

Better Possible?
❌ No.
'''
