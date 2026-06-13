'''
5. Best Time to Buy and Sell Stock with Cooldown (Medium)
Problem Statement

You are given an array prices where prices[i] is the price of a stock on day i.

Find the maximum profit you can achieve with as many transactions as you like, with
the restriction: after you SELL a stock, you cannot buy on the next day (one-day
cooldown). You may hold at most one share at a time.

Example:
Input:  prices = [1,2,3,0,2]
Output: 3
Explanation: buy at 1, sell at 3 (+2), cooldown, buy at 0, sell at 2 (+2)?
Cooldown after the first sell blocks the immediate rebuy, so the optimal is
[buy, sell, cooldown, buy, sell] = (3-1) ... best total achievable = 3.

Input:  prices = [1]
Output: 0
Explanation: a single day, no transaction possible; profit = 0.
'''

def max_profit(prices):
    # STATE: three rolling scalars describing today's status:
    #   hold = best cash while holding a share
    #   sold = best cash on the day we just sold (next day is cooldown)
    #   rest = best cash while resting / cooled down (free to buy)
    # TRANSITION (for each price):
    #   prev_hold, prev_sold, prev_rest = hold, sold, rest
    #   hold = max(prev_hold, prev_rest - price)   # keep holding, or buy after a rest
    #   sold = prev_hold + price                   # sell today
    #   rest = max(prev_rest, prev_sold)           # stay resting, or finish cooldown
    # BASE: hold = -infinity, sold = 0, rest = 0.
    # ANSWER: max(sold, rest) — never end holding.
    if not prices:
        return 0

    hold = float("-inf")
    sold = 0
    rest = 0
    for price in prices:
        prev_hold, prev_sold, prev_rest = hold, sold, rest
        hold = max(prev_hold, prev_rest - price)
        sold = prev_hold + price
        rest = max(prev_rest, prev_sold)
    return max(sold, rest)


if __name__ == "__main__":
    print(max_profit([1, 2, 3, 0, 2]))  # Expected: 3
    print(max_profit([1]))               # Expected: 0


'''
Pattern
Stock DP (cooldown) — three-state state machine DP (hold / sold / rest).
Why: the cooldown couples consecutive days, so a sold state must funnel through rest
before hold can buy again. Three rolling scalars capture this in O(1) space.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. One pass with three scalars is optimal in both time and space.
'''
