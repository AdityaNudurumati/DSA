'''
2. Constrained Subsequence Sum (Hard)
Problem Statement

Given an integer array nums and an integer k, return the maximum sum of a
non-empty subsequence such that for every two consecutive chosen elements at
indices i < j, the gap satisfies j - i <= k.

Example
Input:
nums = [10,2,-10,5,20], k = 2

Output:
37
Explanation:
Pick 10, 2, 5, 20 -> 37 (every consecutive gap <= 2).
'''

from collections import deque

def constrainedSubsetSum(nums, k):

    n = len(nums)
    dp = [0] * n        # dp[i] = best sum of a valid subsequence ENDING at i
    dq = deque()        # indices with decreasing dp values, within the last k
    best = float("-inf")

    for i in range(n):

        # drop indices that are now further than k behind i
        while dq and dq[0] < i - k:
            dq.popleft()

        prev_best = dp[dq[0]] if dq else 0
        dp[i] = nums[i] + max(0, prev_best)   # extend best window, or start fresh
        best = max(best, dp[i])

        # maintain decreasing dp values in the deque
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)

    return best


if __name__ == "__main__":
    print(constrainedSubsetSum([10, 2, -10, 5, 20], 2))   # Expected: 37
    print(constrainedSubsetSum([-1, -2, -3], 1))           # Expected: -1
    print(constrainedSubsetSum([10, -2, -10, -5, 20], 2))  # Expected: 23

'''
Pattern
✅ DP + Monotonic Deque (sliding-window maximum of dp)

Key Observation
dp[i] = nums[i] + max(0, max(dp[i-k .. i-1])). The inner "max over the last k dp
values" is exactly a sliding-window maximum -> maintain it with a decreasing deque.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Naive DP is O(n*k); the deque removes the inner scan.
'''
