'''
2. Soup Servings (Medium)
Problem Statement

There are two types of soup, A and B, that start with n mL each. On each turn,
one of four serving operations is chosen with equal probability (1/4):
  - serve 100 mL of A and 0 mL of B
  - serve 75 mL of A and 25 mL of B
  - serve 50 mL of A and 50 mL of B
  - serve 25 mL of A and 75 mL of B
If a soup does not have enough remaining, serve as much as possible.
We stop as soon as either soup is empty.

Return the probability that A is empty first, PLUS half the probability that A
and B become empty at the same time.

Input:
n = 50

Output:
0.62500

Explanation:
With n = 50 we have two operations that empty A first and one that empties
both simultaneously, giving 0.5 + 0.5 * 0.25 = 0.625.
'''

import math
from functools import lru_cache


def soupServings(n):
    # Large-n short circuit: as n grows the probability tends to 1 very fast
    # (within 1e-6 well before n ~ 4800), so for big n we return 1.0 directly.
    if n >= 4800:
        return 1.0

    # Scale by 25 mL units and round up, so the 4 operations become
    # (4,0), (3,1), (2,2), (1,3) in units. Servings = ceil(n / 25).
    units = math.ceil(n / 25)

    # State: prob(a, b) = required probability when `a` units of A and `b`
    #        units of B remain.
    # Transition: average over the 4 equally likely operations of the next
    #        state (clamping units at 0).
    # Base:
    #   a <= 0 and b <= 0 -> both empty simultaneously -> 0.5
    #   a <= 0            -> A empty first             -> 1.0
    #   b <= 0            -> B empty first             -> 0.0
    @lru_cache(maxsize=None)
    def prob(a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1.0
        if b <= 0:
            return 0.0
        return 0.25 * (prob(a - 4, b) +
                       prob(a - 3, b - 1) +
                       prob(a - 2, b - 2) +
                       prob(a - 1, b - 3))

    return round(prob(units, units), 5)


if __name__ == "__main__":
    print("%.5f" % soupServings(50))         # Expected: 0.62500
    print("%.5f" % soupServings(100000000))  # Expected: 1.00000


'''
Pattern
✅ Probability DP (Expected/Random Steps)
dp[a][b] is the probability of the desired outcome from a given remaining
(A, B) state, averaging over the 4 equally likely serving operations. This is
the canonical probability-DP recurrence (weighted sum of next-state
probabilities) solved by memoization, plus a convergence short-circuit for
large n.

| Metric | Value    |
| ------ | -------- |
| Time   | O(1)     |
| Space  | O(1)     |

Better Possible?
Because of the n >= 4800 short-circuit and the fixed 25 mL scaling, the number
of reachable states is bounded by a constant (~192 * 192), so both time and
space are effectively O(1). No asymptotic improvement is possible.
'''
