'''
1. Online Stock Span (Medium)
Problem Statement

Design an algorithm that collects daily price quotes for a stock and returns
the span of the stock's price for the current day.

The span of the stock's price on a given day is the maximum number of
consecutive days (ending on that day, going backwards) for which the price
was less than or equal to the price on the current day.

Implement the StockSpanner class with a next(price) method that feeds prices
one at a time and returns the span for that day.

Example
Input:
prices = [100, 80, 60, 70, 60, 75, 85]   (fed one by one via next())

Output:
[1, 1, 1, 2, 1, 4, 6]
Explanation:
100 -> 1 (no earlier day <= 100 in the streak)
80  -> 1
60  -> 1
70  -> 2 (today 70, plus yesterday 60)
60  -> 1
75  -> 4 (75,60,70,60)
85  -> 6 (85,75,60,70,60,80)
'''

class StockSpanner:
    def __init__(self):
        # Monotonic (strictly decreasing) stack of (price, span).
        # Each entry already absorbs the spans of the smaller prices behind it.
        self.stack = []

    def next(self, price):
        span = 1
        # Collapse every earlier price that is <= today's price,
        # accumulating their spans into today's span.
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    spanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    result = [spanner.next(p) for p in prices]
    print(result)  # Expected: [1, 1, 1, 2, 1, 4, 6]


'''
Pattern
✅ Monotonic Stack of (value, span)

Why: A plain rescan back from each day is O(n) per query → O(n^2). By keeping a
strictly decreasing stack where each kept price carries the total span of the
shorter prices it already swallowed, every price is pushed and popped at most
once, so all next() calls together are amortized O(1).

| Metric | Value |
| ------ | ----- |
| Time   | O(1) amortized per next(), O(n) total |
| Space  | O(n)  |

Better Possible?
❌ No

Each price must be processed once; amortized O(1) per call is optimal.
'''
