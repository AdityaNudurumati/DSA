'''
1. Traveling Salesman Problem (Hard)
Problem Statement

You are given an n x n matrix dist where dist[i][j] is the cost of travelling
directly from city i to city j. Starting at city 0, you must visit every city
exactly once and then return to city 0.

Return the minimum total cost of such a round trip (shortest Hamiltonian cycle).

Input:
dist = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]

Output:
80

Explanation:
The optimal tour is 0 -> 1 -> 3 -> 2 -> 0 with cost 10 + 25 + 30 + 15 = 80.
'''

from functools import lru_cache


def tsp(dist):
    n = len(dist)
    FULL = (1 << n) - 1

    # State: dp(mask, last) = min cost to have visited exactly the cities in
    #        `mask`, currently standing at city `last` (last is in mask).
    # Transition: try every unvisited city nxt:
    #        dp(mask, last) = min over nxt of dist[last][nxt]
    #                         + dp(mask | 1<<nxt, nxt)
    # Base: when all cities visited (mask == FULL) we must close the cycle, so
    #        the cost left is dist[last][0] (return to the start city 0).
    @lru_cache(maxsize=None)
    def dp(mask, last):
        if mask == FULL:
            return dist[last][0]

        best = float("inf")
        for nxt in range(n):
            if (mask >> nxt) & 1:        # already visited
                continue
            cand = dist[last][nxt] + dp(mask | (1 << nxt), nxt)
            if cand < best:
                best = cand
        return best

    # Start at city 0 with only city 0 visited.
    return dp(1 << 0, 0)


if __name__ == "__main__":
    dist = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]
    print(tsp(dist))  # Expected: 80


'''
Pattern
✅ Bitmask DP (Traveling Salesman)
The set of already-visited cities is a subset of n items, so we encode it in an
n-bit mask. Pairing the mask with the current city (`last`) gives an exact,
overlapping subproblem dp[mask][last] that we memoize — this collapses the
factorial (n-1)! tour enumeration into 2^n * n states.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(2^n * n^2) |
| Space  | O(2^n * n) |

Better Possible?
❌ Not in general. TSP is NP-hard; no known polynomial algorithm exists.
The Held-Karp bitmask DP above (O(2^n * n^2)) is the standard exact optimum and
is far better than the brute-force O(n!). For larger n one resorts to
approximation / heuristic methods rather than an exact speedup.
'''
