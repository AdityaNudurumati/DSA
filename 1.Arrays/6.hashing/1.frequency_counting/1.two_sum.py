'''
1. Two Sum (Easy) — unsorted
Problem Statement

Given an unsorted integer array nums and a target, return the indices of the two
numbers that add up to target. Exactly one solution exists; you may not reuse an
element.

Example
Input:
nums = [2,7,11,15], target = 9

Output:
[0,1]
'''

def twoSum(nums, target):

    seen = {}       # value -> index

    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i

    return []


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
    print(twoSum([3, 2, 4], 6))         # Expected: [1, 2]
    print(twoSum([3, 3], 6))            # Expected: [0, 1]

'''
Pattern
✅ Hashmap complement lookup

Key Observation
For each x, check if its complement (target - x) was already seen. One pass, O(1)
lookups. (The sorted-input version uses two pointers — see ../../1.two_pointer_problems/)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No for unsorted input.
'''
