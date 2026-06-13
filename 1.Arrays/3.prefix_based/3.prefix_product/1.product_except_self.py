'''
1. Product of Array Except Self (Medium)
Problem Statement

Given an integer array nums, return an array answer where answer[i] is the product
of all elements of nums except nums[i].

Constraints: solve without division, in O(n) time.

Example
Input:
nums = [1,2,3,4]

Output:
[24,12,8,6]
'''

def productExceptSelf(nums):

    n = len(nums)
    result = [1] * n

    # pass 1: result[i] = product of everything to the LEFT of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # pass 2: multiply by product of everything to the RIGHT of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))        # Expected: [24, 12, 8, 6]
    print(productExceptSelf([-1, 1, 0, -3, 3]))   # Expected: [0, 0, 9, 0, 0]

'''
Pattern
✅ Prefix Product × Suffix Product

Key Observation
answer[i] = (product of left of i) * (product of right of i). Two passes, and the
output array doubles as the prefix store -> O(1) extra space.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  | (excluding the output array)

Better Possible?
❌ No. Division would be O(n) too but breaks on zeros.
'''
