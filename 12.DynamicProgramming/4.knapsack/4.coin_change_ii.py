'''
4. Coin Change II (Medium)
Problem Statement

You are given an integer amount and an array coins of distinct coin
denominations. Return the number of combinations that make up that amount.
You may use an unlimited number of each coin. Combinations are unordered
(2 + 1 + 1 is the same combination as 1 + 2 + 1).

If that amount cannot be made up by any combination of the coins, return 0.

Input:
amount = 5
coins = [1, 2, 5]

Output:
4

Explanation:
5 = 5
5 = 2 + 2 + 1
5 = 2 + 1 + 1 + 1
5 = 1 + 1 + 1 + 1 + 1
'''


def change(amount, coins):
    # state: dp[a] = number of UNORDERED combinations summing to a.
    dp = [0] * (amount + 1)
    dp[0] = 1  # base: one way to make 0 (use no coins)

    # Coin loop OUTSIDE, amount loop inside => counts combinations, not
    # permutations (each coin denomination is considered in a fixed order).
    for coin in coins:
        # transition: unbounded knapsack, iterate amount ASCENDING so a coin
        # can be reused. dp[a] += dp[a - coin]
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


if __name__ == "__main__":
    print(change(5, [1, 2, 5]))  # Expected: 4
    print(change(3, [2]))        # Expected: 0
    print(change(10, [10]))      # Expected: 1


'''
Pattern
✅ Knapsack DP — Unbounded Knapsack (combination count)
The coin loop is the OUTER loop and the amount loop the INNER loop. Iterating
amount ascending lets a coin be reused (unbounded); putting coins outside means
each combination is counted once regardless of order.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n * amount)  |
| Space  | O(amount)      |

Better Possible?
❌ Not asymptotically.
Counting requires touching every (coin, amount) state; O(n * amount) is
optimal for this DP.
'''
