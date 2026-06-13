'''
1. Range Sum Query - Immutable (Easy)
Problem Statement

Given an integer array nums, answer many queries of the form sumRange(left, right)
= sum of nums[left..right] (inclusive). The array does not change.

Precompute a prefix-sum array so each query is O(1).

Example
Input:
nums = [-2,0,3,-5,2,-1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
'''

class NumArray:

    def __init__(self, nums):
        # prefix[i] = sum of the first i elements (prefix[0] = 0)
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sumRange(0, 2))   # Expected: 1
    print(na.sumRange(2, 5))   # Expected: -1
    print(na.sumRange(0, 5))   # Expected: -3

'''
Pattern
✅ Prefix Sum

| Metric        | Value |
| ------------- | ----- |
| Build         | O(n)  |
| Query         | O(1)  |
| Space         | O(n)  |

Better Possible?
❌ No for many queries. (A single query without precompute is O(n).)
'''
