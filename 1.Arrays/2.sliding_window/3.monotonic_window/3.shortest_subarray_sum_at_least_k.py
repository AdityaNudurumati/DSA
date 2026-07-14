'''
3. Shortest Subarray with Sum at Least K (Hard)
Problem Statement

Given an integer array nums (values may be NEGATIVE) and an integer k, return the
length of the SHORTEST non-empty contiguous subarray whose sum is at least k.
If no such subarray exists, return -1.

Example
Input:
nums = [2,-1,2], k = 3

Output:
3
Explanation:
The whole array sums to 3 (>= k); no shorter subarray reaches 3.
'''

from collections import deque

def shortestSubarray(nums, k):

    n = len(nums)

    # prefix[i] = sum of the first i elements; subarray (l..r-1) sum = prefix[r]-prefix[l]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    dq = deque()            # indices into prefix, kept with INCREASING prefix values
    best = n + 1

    for i in range(n + 1):

        # front: if prefix[i] - prefix[dq[0]] >= k, this window qualifies.
        # it can never get shorter for a later i, so record it and pop the front.
        while dq and prefix[i] - prefix[dq[0]] >= k:
            best = min(best, i - dq.popleft())

        # back: a larger-or-equal earlier prefix is useless (this one is smaller
        # AND more to the right), so drop it to keep the deque increasing.
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()

        dq.append(i)

    return best if best <= n else -1


if __name__ == "__main__":
    print(shortestSubarray([2, -1, 2], 3))   # Expected: 3
    print(shortestSubarray([1], 1))           # Expected: 1
    print(shortestSubarray([1, 2], 4))        # Expected: -1
    print(shortestSubarray([84, -37, 32, 40, 95], 167))  # Expected: 3

'''
Pattern
✅ Monotonic Deque over PREFIX SUMS (indices, increasing prefix values)

Key Observation
With negatives, a plain sliding window fails. Using prefix sums, we want the
smallest (i - j) with prefix[i] - prefix[j] >= k. A deque of candidate j's kept
in increasing prefix order lets us (a) pop the front once it satisfies k (shortest
for that i), and (b) pop the back when the new prefix is <= it (smaller and to the
right = strictly better). Each index enters and leaves the deque once.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Prefix sums are O(n) and every index is pushed/popped once -> O(n).
'''
