'''
4. Best Time to Buy and Sell Stock IV (Hard)
Problem Statement

You are given an integer k and an array prices where prices[i] is the price of a
stock on day i.

Find the maximum profit you can achieve. You may complete AT MOST k transactions.
You may not engage in multiple transactions simultaneously (sell before buying again).

Example:
Input:  k = 2, prices = [2,4,1]
Output: 2
Explanation: buy at 2 (day 0), sell at 4 (day 1) = 2. A second transaction adds
nothing.

Input:  k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: buy at 2 sell at 6 = 4, then buy at 0 sell at 3 = 3; total = 7.
'''

def max_profit(k, prices):
    # If k is large enough to cover every up-step, the cap is irrelevant -> treat as
    # infinite transactions (sum of positive deltas).
    n = len(prices)
    if n == 0 or k == 0:
        return 0
    if k >= n // 2:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

    # STATE: for each transaction slot t in 1..k:
    #   buy[t]  = best cash while holding a share within transaction t
    #   sell[t] = best cash after completing up to t transactions (flat)
    # TRANSITION (for each price, t from 1..k):
    #   buy[t]  = max(buy[t],  sell[t-1] - price)
    #   sell[t] = max(sell[t], buy[t]   + price)
    # BASE: buy[t] = -infinity, sell[t] = 0 (sell[0] stays 0 = no transaction).
    buy = [float("-inf")] * (k + 1)
    sell = [0] * (k + 1)
    for price in prices:
        for t in range(1, k + 1):
            buy[t] = max(buy[t], sell[t - 1] - price)
            sell[t] = max(sell[t], buy[t] + price)
    return sell[k]


if __name__ == "__main__":
    print(max_profit(2, [2, 4, 1]))            # Expected: 2
    print(max_profit(2, [3, 2, 6, 5, 0, 3]))   # Expected: 7


'''
Pattern
Stock DP (k transactions) — general state machine DP with a transaction dimension.
Why: state is (transactions used, holding?). We keep buy[t]/sell[t] arrays and roll
them over days. When k >= n/2 the cap can never bind, so we fall back to the O(n)
infinite-transaction sum.

| Metric | Value    |
| ------ | -------- |
| Time   | O(n * k) |
| Space  | O(k)     |

Better Possible?
The general case needs O(n*k); the k >= n/2 shortcut already collapses to O(n). Space
is reduced from O(n*k) to O(k) via rolling arrays — optimal for this formulation.
'''
