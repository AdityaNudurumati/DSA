'''
1. Maximum Sum Subarray of Size K (Easy)
Problem Statement

Given an integer array nums and an integer k, find the maximum sum of any
contiguous subarray of size exactly k.

Example
Input:
nums = [2,1,5,1,3,2], k = 3

Output:
9
Explanation:
Subarray [5,1,3] has the largest sum = 9.
'''

def maxSumSubarray(nums, k):

    window_sum = 0
    best = float("-inf")

    for right in range(len(nums)):

        window_sum += nums[right]

        if right >= k - 1:
            best = max(best, window_sum)
            window_sum -= nums[right - k + 1]   # drop the leftmost element

    return best


if __name__ == "__main__":
    print(maxSumSubarray([2, 1, 5, 1, 3, 2], 3))   # Expected: 9
    print(maxSumSubarray([2, 3, 4, 1, 5], 2))       # Expected: 7

'''
Pattern
✅ Fixed-Size Sliding Window

Key Observation
Instead of re-summing each window, add the new right element and subtract the
element leaving on the left → O(1) per step.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Must read every element once.
'''
