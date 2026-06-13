'''
1. Best Time to Buy and Sell Stock (Easy)
Problem Statement

You are given an array prices where prices[i] is the price of a stock on day i.

You want to maximize profit by choosing a single day to buy one stock and a
different later day to sell it. Return the maximum profit. If no profit is
possible, return 0.

You may complete at most ONE transaction (buy once, sell once).

Example:
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation: buy on day 1 (price 1), sell on day 4 (price 6), profit = 6 - 1 = 5.

Input:  prices = [7,6,4,3,1]
Output: 0
Explanation: prices only fall, so no profitable transaction; profit = 0.
'''

def max_profit(prices):
    # STATE: scan left to right tracking the best (lowest) buy price seen so far
    #        and the best profit achievable if we sell today.
    # TRANSITION:
    #   min_price = min(min_price, price)               # cheapest day to have bought
    #   best      = max(best, price - min_price)        # sell today vs prior best
    # BASE: best = 0 (do nothing), min_price = +infinity before any day.
    if not prices:
        return 0

    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    print(max_profit([7, 6, 4, 3, 1]))      # Expected: 0


'''
Pattern
Stock DP (one transaction) — single-pass decision DP.
Why: the only state we need is the minimum price seen so far; the best sell-today
profit is a 1D rolling DP collapsed to two scalars (min_price, best).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. Every price must be inspected at least once, so O(n) time is optimal, and the
state is already reduced to O(1).
'''
