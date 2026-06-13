'''
6. Best Time to Buy and Sell Stock with Transaction Fee (Medium)
Problem Statement

You are given an array prices where prices[i] is the price of a stock on day i, and
an integer fee representing a transaction fee.

Find the maximum profit you can achieve with as many transactions as you like, but
you must pay the transaction fee for each transaction. You may hold at most one share
at a time. (Charge the fee once per buy/sell round trip.)

Example:
Input:  prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: buy at 1, sell at 8 (profit 8-1-2 = 5), buy at 4, sell at 9
(profit 9-4-2 = 3); total = 8.

Input:  prices = [1,3,7,5,10,3], fee = 3
Output: 6
Explanation: buy at 1, sell at 10 (10-1-3 = 6); a single round trip is best = 6.
'''

def max_profit(prices, fee):
    # STATE: two rolling scalars.
    #   cash = best cash while NOT holding a share
    #   hold = best cash while holding a share (price already paid)
    # TRANSITION (for each price); charge the fee on selling:
    #   cash = max(cash, hold + price - fee)   # sell today (pay fee), or stay flat
    #   hold = max(hold, cash - price)         # buy today, or keep holding
    # BASE: cash = 0, hold = -infinity.
    if not prices:
        return 0

    cash = 0
    hold = float("-inf")
    for price in prices:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash


if __name__ == "__main__":
    print(max_profit([1, 3, 2, 8, 4, 9], 2))   # Expected: 8
    print(max_profit([1, 3, 7, 5, 10, 3], 3))   # Expected: 6


'''
Pattern
Stock DP (transaction fee) — two-state state machine DP (cash / hold).
Why: like infinite transactions, but each completed round trip costs a fee; charging
it on the sell transition keeps the cash/hold rolling DP in O(1) space.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. A single linear pass with O(1) state is optimal.
'''
