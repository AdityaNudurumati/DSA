'''
3. Best Time to Buy and Sell Stock II (Medium)
Problem Statement

Given daily prices, you may buy and sell as many times as you like (but hold at most
one share at a time). Return the maximum total profit.

Example
Input:
prices = [7,1,5,3,6,4]

Output:
7
Explanation:
Buy at 1 sell at 5 (+4), buy at 3 sell at 6 (+3) -> 7.
'''

def maxProfit(prices):

    profit = 0

    # capture every upward step; summing positive diffs = sum of all profitable trades
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))   # Expected: 7
    print(maxProfit([1, 2, 3, 4, 5]))      # Expected: 4
    print(maxProfit([7, 6, 4, 3, 1]))      # Expected: 0

'''
Pattern
✅ Greedy (sum every positive day-to-day difference)

Key Observation
Any multi-day rise equals the sum of its consecutive daily gains, so grabbing every
positive step captures the maximum without tracking explicit buy/sell points.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
