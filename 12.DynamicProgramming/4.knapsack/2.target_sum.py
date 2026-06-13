'''
2. Target Sum (Medium)
Problem Statement

You are given an integer array nums and an integer target.

You want to build an expression by adding one of the symbols '+' or '-' before
each integer in nums and then concatenating all the integers.

Return the number of different expressions that you can build, which evaluate
to target.

Input:
nums = [1, 1, 1, 1, 1]
target = 3

Output:
5

Explanation:
-1+1+1+1+1, +1-1+1+1+1, +1+1-1+1+1, +1+1+1-1+1, +1+1+1+1-1 all equal 3.
'''


def findTargetSumWays(nums, target):
    total = sum(nums)

    # Let P = sum of '+' numbers, N = sum of '-' numbers.
    # P - N = target and P + N = total  =>  P = (total + target) / 2.
    # So count subsets summing to subset_sum = (total + target) / 2.
    if abs(target) > total or (total + target) % 2 != 0:
        return 0

    subset_sum = (total + target) // 2

    # state: dp[s] = number of subsets that sum exactly to s.
    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # base: one way to make sum 0 (choose nothing)

    for num in nums:
        # transition: 0/1 knapsack count, iterate capacity DESCENDING.
        # dp[s] += dp[s - num]  (ways that finish at s by adding this num)
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[subset_sum]


if __name__ == "__main__":
    print(findTargetSumWays([1, 1, 1, 1, 1], 3))  # Expected: 5
    print(findTargetSumWays([1], 1))              # Expected: 1


'''
Pattern
✅ Knapsack DP — 0/1 Subset-Sum Count
We reduce the +/- assignment to "count subsets with a fixed sum" via the
algebra P = (total + target) / 2, then run a counting 0/1 knapsack with
capacity descending so each number is assigned exactly once.

| Metric | Value       |
| ------ | ----------- |
| Time   | O(n * sum)  |
| Space  | O(sum)      |

Better Possible?
❌ Not asymptotically.
Pseudo-polynomial in the subset sum; this is the standard optimal approach.
'''
