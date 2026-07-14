'''
4. Jump Game VI (Medium)
Problem Statement

You start at index 0 of an integer array nums. From index i you may jump to any
index in [i+1, i+k]. Your score is the SUM of nums at every index you land on
(including index 0 and the last index). Return the MAXIMUM score to reach the
last index.

Example
Input:
nums = [1,-1,-2,4,-7,3], k = 2

Output:
7
Explanation:
Path 0 -> 1 -> 3 -> 5 collects 1 + (-1) + 4 + 3 = 7 (best possible).
'''

from collections import deque

def maxResult(nums, k):

    n = len(nums)
    dp = [0] * n            # dp[i] = best score to reach index i
    dp[0] = nums[0]

    dq = deque([0])         # indices, kept with DECREASING dp values

    for i in range(1, n):

        # front index must be within the reach window [i-k, i-1]
        while dq and dq[0] < i - k:
            dq.popleft()

        # best previous score in reach is at the front of the deque
        dp[i] = nums[i] + dp[dq[0]]

        # drop back indices whose dp is <= dp[i] (they can never win later)
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()

        dq.append(i)

    return dp[n - 1]


if __name__ == "__main__":
    print(maxResult([1, -1, -2, 4, -7, 3], 2))          # Expected: 7
    print(maxResult([10, -5, -2, 4, 0, 3], 3))           # Expected: 17
    print(maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))  # Expected: 0

'''
Pattern
✅ DP + Monotonic Deque (sliding-window maximum inside a DP transition)

Key Observation
dp[i] = nums[i] + max(dp[j]) for j in [i-k, i-1]. That inner "max over the last k
dp values" is a sliding-window maximum, so a DECREASING deque of indices gives it
in O(1) amortized: front = best reachable predecessor. Pop the front when it
leaves the window; pop the back while its dp <= the new dp.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Each index is pushed/popped from the deque once -> O(n). A plain
dp[i]=max(dp[i-k..i-1]) scan would be O(n*k).
'''
