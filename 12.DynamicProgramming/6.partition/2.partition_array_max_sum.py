'''
2. Partition Array for Maximum Sum (Medium)  (LC 1043)
Problem Statement

Given an integer array arr, partition it into contiguous subarrays of length at
most k. After partitioning, every element in a subarray becomes the maximum
value of that subarray.

Return the largest possible sum of the array after this transformation.

Example
Input:
arr = [1, 15, 7, 9, 2, 5, 10], k = 3

Output:
84
Explanation:
arr becomes [15,15,15,9,10,10,10] -> sum = 84.
'''

from functools import lru_cache


def maxSumAfterPartitioning(arr, k):
    n = len(arr)

    # State: dp(i) = max sum obtainable for the suffix arr[i:].
    # Transition: the next subarray starts at i and has length L in [1, k]
    #   (bounded by the array end). Every element in it becomes the running
    #   max of arr[i:i+L], contributing L * max.
    #   dp(i) = max over L of (L * max(arr[i:i+L]) + dp(i+L))
    # Base: dp(n) = 0  (empty suffix).
    @lru_cache(None)
    def dp(i):
        if i == n:
            return 0
        best = 0
        cur_max = 0
        for L in range(1, min(k, n - i) + 1):
            cur_max = max(cur_max, arr[i + L - 1])
            best = max(best, L * cur_max + dp(i + L))
        return best

    return dp(0)


if __name__ == "__main__":
    print(maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))           # Expected: 84
    print(maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4)) # Expected: 83

'''
Pattern
Partition DP

Which DP & Why
We split the array at the first cut point: the leading block has length L (the
partition choice), every element in it collapses to that block's maximum, and
the remaining suffix is solved recursively. Iterating the cut length L and
combining block value + suffix result is the partition-DP pattern, here on a
1-D suffix index rather than an (i, j) interval.

| Metric | Value    |
| ------ | -------- |
| Time   | O(n * k) |
| Space  | O(n)     |

Better Possible?
O(n*k) is optimal: each of the n positions tries at most k partition lengths,
and the running-max trick keeps each transition O(1). No asymptotically better
solution is known for the general case.
'''
