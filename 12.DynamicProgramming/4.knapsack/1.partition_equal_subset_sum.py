'''
1. Partition Equal Subset Sum (Medium)
Problem Statement

Given an integer array nums, return true if you can partition the array into
two subsets such that the sum of the elements in both subsets is equal, or
false otherwise.

Input:
nums = [1, 5, 11, 5]

Output:
True

Explanation:
The array can be partitioned as [1, 5, 5] and [11], both summing to 11.
'''


def canPartition(nums):
    total = sum(nums)

    # If total is odd it can never split into two equal halves.
    if total % 2 != 0:
        return False

    target = total // 2

    # state: dp[s] = True if some subset of items seen so far sums to s.
    # This is the 0/1 Subset-Sum knapsack with capacity = target.
    dp = [False] * (target + 1)
    dp[0] = True  # base: empty subset hits sum 0

    for num in nums:
        # transition: iterate DESCENDING so each item is used at most once.
        # dp[s] becomes reachable if dp[s - num] was reachable before this item.
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

    return dp[target]


if __name__ == "__main__":
    print(canPartition([1, 5, 11, 5]))  # Expected: True
    print(canPartition([1, 2, 3, 5]))   # Expected: False


'''
Pattern
✅ Knapsack DP — 0/1 Subset Sum (boolean)
Each number may be picked once, so we iterate capacity descending in the 1D
table. We ask: can we reach exactly total/2? If yes the rest forms the other
equal half.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n * sum) |
| Space  | O(sum)     |

Better Possible?
❌ Not asymptotically.
The problem is a pseudo-polynomial subset-sum; O(n * sum) is the standard
bound. A bitset trick can speed the constant factor but not the complexity.
'''
