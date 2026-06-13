"""
746. Min Cost Climbing Stairs (Easy)

Problem Statement:
You are given an integer array cost where cost[i] is the cost of step i.
Once you pay the cost, you can climb either one or two steps. You may start
from step index 0 or step index 1. Return the minimum cost to reach the top
of the floor (just past the last step).

Example:
    Input:  [10, 15, 20]
    Output: 15         # start at index 1, pay 15, take 2 steps to the top

    Input:  [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6          # step on indices 0,2,4,6,7,9 -> 1*6 = 6
"""


def min_cost_climbing_stairs(cost) -> int:
    # State: dp[i] = minimum cost to STAND on step i.
    # Transition: dp[i] = cost[i] + min(dp[i-1], dp[i-2]).
    # Base: dp[0] = cost[0], dp[1] = cost[1] (free start at index 0 or 1).
    # Answer: min(dp[n-1], dp[n-2]) -- top is reachable from either last step.
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return 0  # already at/past top from a free start

    prev2 = cost[0]        # dp[i-2]
    prev = cost[1]         # dp[i-1]
    for i in range(2, n):
        cur = cost[i] + min(prev, prev2)
        prev2, prev = prev, cur

    return min(prev, prev2)


if __name__ == "__main__":
    print(min_cost_climbing_stairs([10, 15, 20]))                          # Expected: 15
    print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected: 6


"""
Pattern: LINEAR DP (1D) -- Climbing-Stairs cost minimization.
The cost to stand on step i depends only on the two steps below it
(dp[i] = cost[i] + min(dp[i-1], dp[i-2])), the classic dp[i] = f(dp[i-1],
dp[i-2]) recurrence. Bottom-up tabulation collapsed to two rolling variables
fits perfectly; memoization would add call overhead for no benefit since the
states are visited in natural left-to-right order.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. Each step must be considered once for an O(n) lower bound, and the two
rolling variables keep space at O(1).
"""
