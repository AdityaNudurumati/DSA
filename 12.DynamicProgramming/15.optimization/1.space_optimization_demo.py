'''
1. Space Optimization Demo: 0/1 Knapsack 2D vs 1D (Medium)
Problem Statement

Given item weights and values and a knapsack capacity cap, pick a subset of
items (each at most once) maximizing total value without exceeding cap.

This file solves the same instance two ways to show a classic DP space
optimization: a full 2D table dp[i][w] and a 1D rolling array dp[w]. Both must
produce the SAME answer; we print both to prove the optimization is correct.

Input:
weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
cap     = 7

Output:
2D: 9
1D: 9

Explanation:
Picking items with weights 3 and 4 (values 4 + 5 = 9) uses capacity 7 exactly
and is optimal. Items 1+5 give 1+7=8; 3+4 wins.
'''


def knapsack_2d(weights, values, cap):
    n = len(weights)
    # State: dp[i][w] = best value using the first i items with capacity w.
    # Transition: dp[i][w] = max(skip item i-1     -> dp[i-1][w],
    #                            take item i-1 if it fits
    #                                              -> dp[i-1][w-wt] + val)
    # Base: dp[0][*] = 0 (no items -> no value).
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i - 1], values[i - 1]
        for w in range(cap + 1):
            dp[i][w] = dp[i - 1][w]                      # skip
            if wt <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wt] + val)  # take
    return dp[n][cap]


def knapsack_1d(weights, values, cap):
    # Optimization: row i only depends on row i-1, so keep ONE array dp[w].
    # Transition (same recurrence): dp[w] = max(dp[w], dp[w-wt] + val).
    # Iterate w DOWNWARD so dp[w-wt] still holds the *previous* row's value
    # (using each item at most once -> the 0/1 constraint).
    # Base: dp[*] = 0.
    dp = [0] * (cap + 1)
    for wt, val in zip(weights, values):
        for w in range(cap, wt - 1, -1):
            dp[w] = max(dp[w], dp[w - wt] + val)
    return dp[cap]


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    cap = 7
    print("2D:", knapsack_2d(weights, values, cap))  # Expected: 9
    print("1D:", knapsack_1d(weights, values, cap))  # Expected: 9


'''
Pattern
✅ Space Optimization (rolling array on 0/1 Knapsack)
The 2D recurrence dp[i][w] reads only from the immediately previous row i-1.
Whenever a DP layer depends solely on the layer before it, the older layers are
dead weight, so we collapse the i-dimension into a single 1D array. The only
subtlety is iteration order: scanning capacity w downward guarantees dp[w-wt]
still reflects the previous item-row, preserving the "each item once" rule.

| Metric | 2D            | 1D            |
| ------ | ------------- | ------------- |
| Time   | O(n * cap)    | O(n * cap)    |
| Space  | O(n * cap)    | O(cap)        |

Better Possible?
❌ Not asymptotically for the optimal value. Time stays O(n * cap) (knapsack is
weakly NP-hard; this is pseudo-polynomial). Space is already reduced from
O(n*cap) to O(cap), the minimum needed to hold one capacity row. If you also
need the chosen items you must keep the 2D table (or re-derive via backtracking).
'''
