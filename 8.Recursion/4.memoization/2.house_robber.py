'''
2. House Robber (Medium)   [LC198]
Problem Statement

You are a robber planning to rob houses along a street. Each house has a
certain amount of money. You cannot rob two adjacent houses (it triggers
the alarm).

Return the maximum amount of money you can rob tonight.

Input:
nums = [1,2,3,1]

Output:
4

Explanation:
Rob house 0 (1) and house 2 (3) -> 1 + 3 = 4.
'''

from functools import lru_cache


def rob(nums):
    n = len(nums)

    # best(i) = max money robbing from index i to the end
    @lru_cache(maxsize=None)
    def best(i):
        if i >= n:                       # no houses left
            return 0
        skip = best(i + 1)               # don't rob house i
        take = nums[i] + best(i + 2)     # rob house i, skip neighbor
        return max(skip, take)

    return best(0)


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))      # Expected: 4
    print(rob([2, 7, 9, 3, 1]))   # Expected: 12


'''
Pattern
✅ Recursive DP (Memoization)
At each house we choose take vs skip; states overlap because best(i) is
reached from both i-1 and i-2. Caching by index makes it linear.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
✅ Yes
Bottom-up with two rolling variables (prev, prevprev) gives O(1) space.
'''
