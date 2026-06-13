'''
1. Maximum Subarray (Medium) — Kadane's Algorithm
Problem Statement

Given an integer array nums, find the contiguous subarray (containing at least one
number) with the largest sum and return that sum.

Example
Input:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:
6
Explanation:
[4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):

    best = cur = nums[0]

    for x in nums[1:]:
        # either extend the previous subarray, or start fresh at x
        cur = max(x, cur + x)
        best = max(best, cur)

    return best


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected: 6
    print(maxSubArray([1]))                               # Expected: 1
    print(maxSubArray([5, 4, -1, 7, 8]))                  # Expected: 23
    print(maxSubArray([-3, -1, -2]))                      # Expected: -1

'''
Pattern
✅ Kadane's Algorithm (DP over subarrays ending at i)

Key Observation
The best subarray ending at i is either just nums[i], or nums[i] plus the best
subarray ending at i-1. Drop the running sum whenever it would hurt.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Must read every element.
'''
