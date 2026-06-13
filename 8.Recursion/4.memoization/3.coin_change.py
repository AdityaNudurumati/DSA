'''
3. Coin Change (Medium)   [LC322]
Problem Statement

You are given coins of different denominations and a total amount. Return
the fewest number of coins needed to make up that amount. If the amount
cannot be made up by any combination of coins, return -1.

You may use each coin denomination an unlimited number of times.

Input:
coins = [1,2,5]
amount = 11

Output:
3

Explanation:
11 = 5 + 5 + 1  ->  3 coins.
'''

from functools import lru_cache


def coinChange(coins, amount):
    INF = float("inf")

    # fewest(rem) = min coins to make remaining amount rem
    @lru_cache(maxsize=None)
    def fewest(rem):
        if rem == 0:                     # exact change made
            return 0
        if rem < 0:                      # overshot
            return INF
        # try each coin, take the best (+1 for the coin used)
        return min((fewest(rem - c) + 1 for c in coins), default=INF)

    result = fewest(amount)
    return result if result != INF else -1


if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))  # Expected: 3
    print(coinChange([2], 3))         # Expected: -1
    print(coinChange([1], 0))         # Expected: 0


'''
Pattern
✅ Recursive DP (Memoization)
The remaining amount is the state; the same remainder is reachable via many
coin orders, so caching fewest(rem) avoids recomputing overlapping subtrees.
| Metric | Value          |
| ------ | -------------- |
| Time   | O(amount * k)  |
| Space  | O(amount)      |
(k = number of coin denominations)
Better Possible?
❌ No
Every reachable amount must be evaluated at least once; bottom-up DP shares
the same O(amount * k) bound, only swapping recursion for iteration.
'''
