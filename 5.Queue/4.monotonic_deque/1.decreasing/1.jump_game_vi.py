'''
1696. Jump Game VI (Medium)
Problem Statement

You are given a 0-indexed integer array nums and an integer k. You start at
index 0. In one move you may jump from index i to any index in the range
[i+1, i+k] (without going out of bounds). Your score is the sum of nums[j] for
every index j you visit (including index 0 and the final index n-1).

Return the maximum score you can get by reaching the last index.

Example
Input:
nums = [1,-1,-2,4,-7,3], k = 2

Output:
7
(path 0 -> 1 -> 3 -> 5 : 1 + (-1) + 4 + 3 = 7)
'''

from collections import deque

def maxResult(nums, k):

    n = len(nums)
    # dp[i] = best score to reach index i. dp[0] = nums[0].
    # dp[i] = nums[i] + max(dp[i-k .. i-1]); a decreasing deque gives that max.
    dp = [0] * n
    dp[0] = nums[0]

    dq = deque([0])   # indices, dp values decreasing; front = best reachable dp

    for i in range(1, n):

        # drop the front index if it is now out of jump range [i-k, i-1]
        if dq[0] < i - k:
            dq.popleft()

        # front of deque is the maximum dp in the reachable window
        dp[i] = nums[i] + dp[dq[0]]

        # maintain decreasing order: pop smaller dp values from the back
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()

        dq.append(i)

    return dp[-1]


if __name__ == "__main__":
    print(maxResult([1, -1, -2, 4, -7, 3], 2))            # Expected: 7
    print(maxResult([10, -5, -2, 4, 0, 3], 3))            # Expected: 17
    print(maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))   # Expected: 0

'''
Pattern
✅ Monotonic Deque (decreasing) over a DP array

Key Observation
The DP recurrence dp[i] = nums[i] + max(dp[i-k .. i-1]) needs the maximum of a
sliding window of previous states. A decreasing deque of indices keeps that
maximum at the front in O(1), turning an O(n*k) DP into O(n).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  | (each index pushed and popped at most once)
| Space  | O(n)  | (dp array + deque)

Better Possible?
❌ No. A heap/segment tree gives O(n log n); the deque is optimal at O(n).
'''
