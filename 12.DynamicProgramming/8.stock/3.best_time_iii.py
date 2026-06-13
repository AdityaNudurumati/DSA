'''
3. Best Time to Buy and Sell Stock III (Hard)
Problem Statement

You are given an array prices where prices[i] is the price of a stock on day i.

Find the maximum profit you can achieve. You may complete AT MOST TWO transactions.
You may not engage in multiple transactions simultaneously (you must sell the stock
before you buy again).

Example:
Input:  prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: buy at 0 (day 4) sell at 3 (day 6) = 3, then buy at 1 sell at 4 = 3;
total = 6.

Input:  prices = [1,2,3,4,5]
Output: 4
Explanation: a single buy at 1 / sell at 5 already gives 4; the second
transaction adds nothing.
'''

def max_profit(prices):
    # STATE: four scalars tracking the best cash after each event:
    #   buy1  = best cash after first buy   (we hold, one buy spent)
    #   sell1 = best cash after first sell  (flat, one transaction done)
    #   buy2  = best cash after second buy  (we hold again)
    #   sell2 = best cash after second sell (flat, two transactions done)
    # TRANSITION (for each price):
    #   buy1  = max(buy1,  -price)
    #   sell1 = max(sell1, buy1 + price)
    #   buy2  = max(buy2,  sell1 - price)
    #   sell2 = max(sell2, buy2 + price)
    # BASE: buy1 = buy2 = -infinity, sell1 = sell2 = 0.
    buy1 = buy2 = float("-inf")
    sell1 = sell2 = 0
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    return sell2


if __name__ == "__main__":
    print(max_profit([3, 3, 5, 0, 0, 3, 1, 4]))  # Expected: 6
    print(max_profit([1, 2, 3, 4, 5]))            # Expected: 4


'''
Pattern
Stock DP (two transactions) — state machine DP, k=2 specialized.
Why: capping transactions adds a "transactions used" dimension. For k=2 we unroll it
into four rolling scalars (buy1/sell1/buy2/sell2) processed left to right.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. Time is linear and the state is fixed at four scalars; both are optimal.
'''
