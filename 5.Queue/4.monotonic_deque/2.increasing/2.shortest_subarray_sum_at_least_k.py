'''
862. Shortest Subarray with Sum at Least K (Hard)
Problem Statement

Given an integer array nums (values may be negative) and an integer k, return the
length of the shortest non-empty contiguous subarray whose sum is at least k.
If no such subarray exists, return -1.

Example
Input:
nums = [2,-1,2], k = 3

Output:
3
(the whole array sums to 3, the shortest subarray with sum >= 3)
'''

from collections import deque

def shortestSubarray(nums, k):

    n = len(nums)
    # prefix[i] = sum of first i elements; subarray (l, r) sum = prefix[r] - prefix[l]
    prefix = [0] * (n + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x

    dq = deque()        # candidate left endpoints; prefix values increasing
    best = n + 1        # sentinel larger than any valid length

    for r in range(n + 1):

        # shrink from front: prefix[r] - prefix[dq[0]] >= k -> record and pop
        # (a closer right end can't beat this length, so this left is done)
        while dq and prefix[r] - prefix[dq[0]] >= k:
            best = min(best, r - dq.popleft())

        # keep prefix increasing: a left with prefix >= current is never better
        while dq and prefix[dq[-1]] >= prefix[r]:
            dq.pop()

        dq.append(r)

    return best if best <= n else -1


if __name__ == "__main__":
    print(shortestSubarray([1], 1))                  # Expected: 1
    print(shortestSubarray([1, 2], 4))               # Expected: -1
    print(shortestSubarray([2, -1, 2], 3))           # Expected: 3
    print(shortestSubarray([84, -37, 32, 40, 95], 167))  # Expected: 3

'''
Pattern
✅ Prefix sums + Monotonic Deque (increasing)

Key Observation
With negatives, a plain sliding window fails. Work on prefix sums: we want the
shortest r-l with prefix[r] - prefix[l] >= k. Keep candidate lefts in a deque of
increasing prefix values. Pop the front whenever the constraint is met (no later
r needs that left), and pop the back whenever a new prefix is <= a stored one
(that older, larger prefix can never give a better or longer-reaching start).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  | (each index enters and leaves the deque once)
| Space  | O(n)  | (prefix array + deque)

Better Possible?
❌ No. O(n) is optimal; a heap variant would add a log factor.
'''
