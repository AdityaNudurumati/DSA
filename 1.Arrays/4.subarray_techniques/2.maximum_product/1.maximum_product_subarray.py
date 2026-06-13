'''
1. Maximum Product Subarray (Medium)
Problem Statement

Given an integer array nums, find the contiguous subarray (containing at least one
number) with the largest product and return that product.

Example
Input:
nums = [2,3,-2,4]

Output:
6
Explanation:
[2,3] has the largest product = 6.
'''

def maxProduct(nums):

    best = cur_max = cur_min = nums[0]

    for x in nums[1:]:

        # a negative x swaps which of max/min is largest after multiplying
        if x < 0:
            cur_max, cur_min = cur_min, cur_max

        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)

        best = max(best, cur_max)

    return best


if __name__ == "__main__":
    print(maxProduct([2, 3, -2, 4]))    # Expected: 6
    print(maxProduct([-2, 0, -1]))      # Expected: 0
    print(maxProduct([-2, 3, -4]))      # Expected: 24

'''
Pattern
✅ Kadane variant tracking BOTH max and min

Key Observation
Unlike sums, a negative number flips a large-negative product into a large-positive
one. So track the running min alongside the max; a negative x swaps their roles.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
