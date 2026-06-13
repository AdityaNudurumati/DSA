'''
5. Combination Sum IV (Medium)
Problem Statement

Given an array of distinct integers nums and a target integer target, return
the number of possible combinations that add up to target.

Here different ORDERINGS are counted as different combinations (so this is
really counting ordered sequences / permutations). Numbers may be reused.

Input:
nums = [1, 2, 3]
target = 4

Output:
7

Explanation:
(1,1,1,1) (1,1,2) (1,2,1) (2,1,1) (2,2) (1,3) (3,1) — 7 ordered combinations.
'''


def combinationSum4(nums, target):
    # state: dp[t] = number of ORDERED sequences of nums summing to t.
    dp = [0] * (target + 1)
    dp[0] = 1  # base: empty sequence makes 0

    # Target loop OUTSIDE, num loop inside => counts permutations (order
    # matters): for each total we try every number as the last element.
    for t in range(1, target + 1):
        for num in nums:
            # transition: dp[t] += dp[t - num] for each num that can be last.
            if num <= t:
                dp[t] += dp[t - num]

    return dp[target]


if __name__ == "__main__":
    print(combinationSum4([1, 2, 3], 4))  # Expected: 7
    print(combinationSum4([9], 3))        # Expected: 0


'''
Pattern
✅ Knapsack DP — Unbounded Knapsack (ordered / permutation count)
This is the mirror of Coin Change II: here the TARGET loop is outer and the
number loop inner, so different orderings are counted separately. Each dp[t]
sums ways formed by appending any num as the final element.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(target * n)  |
| Space  | O(target)      |

Better Possible?
❌ Not asymptotically.
Every (target, num) pair must be examined to count ordered sequences;
O(target * n) is optimal for this DP.
'''
