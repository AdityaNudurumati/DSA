'''
1. Two Sum (Easy)
Problem Statement

Given an array of integers nums and an integer target, return the indices of the
two numbers that add up to target. Each input has exactly one solution, and you may
not use the same element twice.

Example
Input:  nums = [2, 7, 11, 15], target = 9   -> [0, 1]   (2 + 7 = 9)
        nums = [3, 2, 4],       target = 6   -> [1, 2]   (2 + 4 = 6)
'''

def twoSum(nums, target):

    seen = {}                               # value -> index of values seen so far
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:              # complement lookup in O(1)
            return [seen[complement], i]
        seen[x] = i                         # record current value for later lookups
    return []                               # problem guarantees this is unreachable


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))        # Expected: [0, 1]
    print(twoSum([3, 2, 4], 6))             # Expected: [1, 2]

'''
Pattern
✅ Complement Lookup (store value->index, search for target - x)

Key Observation
Instead of an O(n^2) pair scan, remember each value's index in a dict. For every new
x, the partner we need is target - x; a single hash lookup tells us if it already
appeared. One pass, constant-time checks.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ O(n) time is optimal; every element must be examined at least once. Sorting +
two pointers is O(n log n) but loses original indices, so hashing wins here.
'''
