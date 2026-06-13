'''
2. Matchsticks to Square (Medium)
Problem Statement

You are given an integer array matchsticks where matchsticks[i] is the length
of the i-th matchstick. You want to use ALL the matchsticks to make one square.
You may not break any stick, but you can link them, and each stick must be used
exactly once.

Return True if you can make this square, otherwise False.

Example
Input:
matchsticks = [1,1,2,2,2]
Output:
True
Explanation: Sides 2, 2, 1+1, 2 each equal 2.

Input:
matchsticks = [3,3,3,3,4]
Output:
False
'''

from functools import lru_cache


def makesquare(matchsticks):
    total = sum(matchsticks)
    n = len(matchsticks)

    # Need 4 sides; total must split evenly and there must be >= 4 sticks.
    if n < 4 or total % 4 != 0:
        return False

    side = total // 4
    # Any stick longer than the target side length makes it impossible.
    if max(matchsticks) > side:
        return False

    # Sorting descending lets large sticks fail fast (prune early).
    matchsticks.sort(reverse=True)

    # Bitmask DP: bit i set => stick i has been placed.
    # dp(mask) returns the "used length of the current (in-progress) side",
    # i.e. (placed total) % side, IF mask is reachable; else -1 (impossible).
    # We add sticks one at a time; the running fill modulo `side` tells us how
    # much of the current side is filled, so a new stick must not overflow it.
    @lru_cache(None)
    def dp(mask):
        if mask == (1 << n) - 1:
            return 0  # all placed, current side perfectly closed
        used = -1
        for i in range(n):
            if (mask >> i) & 1:
                continue
            nxt = dp(mask | (1 << i))
            if nxt < 0:
                continue
            # Placing stick i must fit into the side currently being filled.
            if nxt + matchsticks[i] <= side:
                used = (nxt + matchsticks[i]) % side
                return used
        return used

    return dp(0) == 0


if __name__ == "__main__":
    print(makesquare([1, 1, 2, 2, 2]))   # Expected: True
    print(makesquare([3, 3, 3, 3, 4]))   # Expected: False

'''
Pattern
Bitmask DP / backtracking over a used-stick subset

Bit trick & why
n is small, so the set of already-placed sticks is packed into one integer
`mask`: bit i set means stick i is used (check (mask >> i) & 1, place
mask | (1 << i)). The clever part: the *amount* filled on the current side is
not stored separately — it is recoverable as (sum of placed lengths) % side,
which dp returns. So one int fully describes the state and lru_cache memoizes
each subset once. Sorting descending + the per-stick "fits in current side"
test prunes hopeless branches early. A square is buildable iff dp(0) == 0
(everything placed with the last side closed exactly).

| Metric | Value          |
| ------ | -------------- |
| Time   | O(2^n * n)     |
| Space  | O(2^n)         |

Better Possible?
Pure DFS backtracking with bucket sums is also common and often faster in
practice with strong pruning, but the asymptotic subset state space stays
exponential. For these small inputs the bitmask DP is optimal and clean.
'''
