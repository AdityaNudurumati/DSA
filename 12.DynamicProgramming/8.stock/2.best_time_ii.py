'''
2. Best Time to Buy and Sell Stock II (Medium)
Problem Statement

You are given an array prices where prices[i] is the price of a stock on day i.

On each day you may buy and/or sell. You can hold at most one share at a time, but
you may complete AS MANY transactions as you like (infinite transactions). You may
even buy and sell on the same day.

Return the maximum profit you can achieve.

Example:
Input:  prices = [7,1,5,3,6,4]
Output: 7
Explanation: buy at 1 sell at 5 (+4), buy at 3 sell at 6 (+3); total = 7.

Input:  prices = [1,2,3,4,5]
Output: 4
Explanation: buy at 1, sell at 5 = 4 (equivalently capture every upward step).
'''

def max_profit(prices):
    # STATE: two scalars, cash (not holding) and hold (holding one share).
    # TRANSITION (for each price):
    #   cash = max(cash, hold + price)   # sell today, or stay in cash
    #   hold = max(hold, cash - price)   # buy today, or keep holding
    # BASE: cash = 0, hold = -infinity (cannot hold before any day).
    # NOTE: because transactions are unlimited, this is exactly the sum of every
    #       positive day-to-day gain.
    cash = 0
    hold = float("-inf")
    for price in prices:
        cash = max(cash, hold + price)
        hold = max(hold, cash - price)
    return cash


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected: 7
    print(max_profit([1, 2, 3, 4, 5]))      # Expected: 4


'''
Pattern
Stock DP (infinite transactions) — state machine DP with two states (cash/hold).
Why: with no transaction cap, the optimal strategy reduces to summing every upward
step; the cash/hold rolling DP expresses this in O(1) state.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. A single pass with O(1) state is optimal; each price must be read once.
'''
