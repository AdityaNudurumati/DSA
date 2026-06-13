'''
1. Delete and Earn (Medium)   [LC740]
Problem Statement

You are given an integer array nums. You want to maximize the points you
earn by performing the following operation any number of times:

  Pick any nums[i], earn nums[i] points, then you MUST delete every element
  equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn.

Input:
nums = [3, 4, 2]

Output:
6

Explanation:
Take 4 (earn 4, delete every 3 and 5). Then take 2 (earn 2).
Total = 4 + 2 = 6.
'''

from collections import Counter


def deleteAndEarn(nums):
    # Reduction: taking value v earns (v * count[v]) but forbids v-1 and v+1.
    # That is exactly House Robber over the value axis: gain[v] cannot be
    # combined with the adjacent value gain[v-1]/gain[v+1].
    if not nums:
        return 0

    counts = Counter(nums)
    lo, hi = min(nums), max(nums)

    # gain[v] = total points if we take value v (= v * how many v's exist)
    # state: take(v) = best earnings considering values from v up to hi
    # transition: take v  -> gain[v] + best(v+2)   (v+1 is deleted)
    #             skip v  -> best(v+1)
    # base: v > hi -> 0
    prev2 = 0   # best(v+2)
    prev1 = 0   # best(v+1)
    for v in range(hi, lo - 1, -1):
        gain = v * counts.get(v, 0)
        take = gain + prev2
        skip = prev1
        cur = max(take, skip)
        prev2, prev1 = prev1, cur

    return prev1


if __name__ == "__main__":
    print(deleteAndEarn([3, 4, 2]))              # Expected: 6
    print(deleteAndEarn([2, 2, 3, 3, 3, 4]))     # Expected: 9


'''
Pattern
✅ Decision DP (Include / Exclude  -> House Robber reduction)
Each distinct value is a "house"; its money is value * frequency, and picking
a value forbids its numeric neighbors (v-1, v+1). Iterating over the value
range turns the problem into House Robber on a line of consecutive values.
| Metric | Value          |
| ------ | -------------- |
| Time   | O(n + k)       |
| Space  | O(n)           |
(k = max(nums) - min(nums), counts dominate the linear scan.)
Better Possible?
✅ Yes / depends
Using two rolling variables already gives O(1) extra space beyond the counter.
If values are huge but sparse, sort distinct values and only roll across
neighbors (handle gaps as resets) to avoid scanning the full range k.
'''
