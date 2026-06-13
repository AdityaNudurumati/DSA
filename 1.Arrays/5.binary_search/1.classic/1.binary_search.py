'''
1. Binary Search (Easy)
Problem Statement

Given a sorted (ascending) array of distinct integers nums and a target, return the
index of target, or -1 if it is not present. Must run in O(log n).

Example
Input:
nums = [-1,0,3,5,9,12], target = 9

Output:
4
'''

def search(nums, target):

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))   # Expected: 4
    print(search([-1, 0, 3, 5, 9, 12], 2))   # Expected: -1

'''
Pattern
✅ Classic Binary Search (inclusive lo..hi)

| Metric | Value      |
| ------ | ---------- |
| Time   | O(log n)   |
| Space  | O(1)       |

Better Possible?
❌ No for a comparison-based search on a sorted array.
'''
