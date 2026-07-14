'''
4. Find All Duplicates in an Array (Medium)   [LC442]
Problem Statement

Given an array nums of n integers where each nums[i] is in 1..n and each appears
ONCE or TWICE, return all elements that appear twice. O(n) time, O(1) extra space.

Cyclic-sort each value to index v-1. After sorting, any index i holding a value
!= i+1 holds a duplicate (that value appeared twice, so it couldn't reach home).

Example
Input:
nums = [4, 3, 2, 7, 8, 2, 3, 1]

Output:
[2, 3]
'''

def findDuplicates(nums):

    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    return [nums[idx] for idx in range(n) if nums[idx] != idx + 1]


if __name__ == "__main__":
    print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))   # Expected: 2 and 3 (any order) -> [3, 2]
    print(findDuplicates([1, 1, 2]))                   # Expected: [1]
    print(findDuplicates([1, 2, 3]))                   # Expected: []

'''
Pattern
✅ Cyclic Sort (range 1..n, find the twice-appearing values)

Key Observation
Same sort as "find all missing" - but here we report the VALUE sitting in each
wrong slot (the duplicate) instead of the slot's expected number (the missing one).
Missing vs duplicate are two readings of the same sorted array.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. O(n)/O(1) is optimal.
'''
