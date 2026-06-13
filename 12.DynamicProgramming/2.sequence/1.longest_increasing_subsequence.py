'''
1. Longest Increasing Subsequence (Medium)
Problem Statement

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence derived from the array by deleting some or no
elements without changing the order of the remaining elements.

Example
Input:
nums = [10,9,2,5,3,7,101,18]

Output:
4
Explanation:
The longest increasing subsequence is [2,3,7,101], length 4.
'''

import bisect


def lengthOfLIS(nums):
    # Patience sorting (O(n log n)).
    #
    # State:  tails[i] = the smallest possible tail value of any strictly
    #         increasing subsequence of length i+1 seen so far.
    # Transition: for each x, find the leftmost tail >= x (bisect_left).
    #         - if none exists, x extends the longest run  -> append.
    #         - otherwise x replaces that tail, keeping the run as "low"
    #           as possible so future elements can extend it.
    # Base: tails starts empty; answer = len(tails) at the end.
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)  # bisect_left -> strictly increasing
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


if __name__ == "__main__":
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected: 4
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))            # Expected: 4
    print(lengthOfLIS([7, 7, 7, 7]))                  # Expected: 1

'''
Pattern
✅ Sequence DP — LIS family via patience sorting + binary search

Why this DP:
The classic O(n^2) LIS uses dp[i] = longest run ending at index i with
transition dp[i] = 1 + max(dp[j]) for j < i and nums[j] < nums[i].
Patience sorting compresses this: tails[] is monotonically increasing, so a
binary search replaces the inner max scan, giving O(n log n). len(tails) is
the LIS length (note: tails is NOT itself a valid subsequence, only its
length is meaningful).

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ No
O(n log n) is optimal for comparison-based LIS.
'''
