'''
3. 0/1 Knapsack (Medium)
Problem Statement

Given weights and values of n items, put these items in a knapsack of
capacity cap to get the maximum total value. Each item may be chosen at most
once (0/1).

Return the maximum value achievable without exceeding the capacity.

Input:
weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
cap     = 7

Output:
9

Explanation:
Take items with weights 3 and 4 (values 4 + 5 = 9), total weight 7.
'''


def knapsack01(weights, values, cap):
    # state: dp[c] = max value achievable using a capacity of exactly <= c
    #         among the items processed so far.
    dp = [0] * (cap + 1)

    for i in range(len(weights)):
        w, v = weights[i], values[i]
        # transition: iterate capacity DESCENDING so item i is used at most once.
        # dp[c] = max(dp[c], dp[c - w] + v)
        for c in range(cap, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)

    # base: dp[0] = 0 (no capacity -> no value), initialized above.
    return dp[cap]


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    cap = 7
    print(knapsack01(weights, values, cap))  # Expected: 9


'''
Pattern
✅ Knapsack DP — Classic 0/1 Knapsack (max value)
Each item is taken once, so the 1D table is updated with capacity descending
to prevent reusing an item within the same iteration.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n * cap) |
| Space  | O(cap)     |

Better Possible?
❌ Not asymptotically.
0/1 knapsack is NP-hard in general; the O(n * cap) pseudo-polynomial DP is the
standard exact solution.
'''
