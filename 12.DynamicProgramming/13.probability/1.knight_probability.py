'''
1. Knight Probability in Chessboard (Medium)
Problem Statement

On an n x n chessboard, a knight starts at the cell (row, column) and makes
exactly k moves. Each move the knight chooses uniformly at random one of its 8
possible moves (even if that move would land off the board). The knight keeps
moving until it has made k moves or it has moved off the board.

Return the probability that the knight remains on the board after it has
stopped moving.

Input:
n = 3, k = 2, row = 0, column = 0

Output:
0.0625

Explanation:
There are two moves (to (1,2) and (2,1)) that keep the knight on the board.
From each of those, it has 2 moves staying on the board. So the probability
is (2/8) * (2/8) + (2/8) * (2/8) = 0.0625.
'''

from functools import lru_cache

# 8 possible knight moves
MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]


def knightProbability(n, k, row, column):
    # State: prob(r, c, steps) = probability of staying on the board for the
    #        remaining `steps` moves, starting from cell (r, c).
    # Transition: prob(r, c, steps) = sum over 8 moves of
    #             (1/8) * prob(r+dr, c+dc, steps-1).
    # Base: if (r, c) is off the board -> 0.0 (this branch failed).
    #       if steps == 0 and on board -> 1.0 (survived all moves).
    @lru_cache(maxsize=None)
    def prob(r, c, steps):
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0.0
        if steps == 0:
            return 1.0
        total = 0.0
        for dr, dc in MOVES:
            total += prob(r + dr, c + dc, steps - 1) / 8.0
        return total

    return round(prob(row, column, k), 5)


if __name__ == "__main__":
    print(knightProbability(3, 2, 0, 0))  # Expected: 0.0625
    print(knightProbability(1, 0, 0, 0))  # Expected: 1.0


'''
Pattern
✅ Probability DP (Random Walk)
The knight is a random walk on a grid; dp[r][c][steps] is the survival
probability with `steps` moves left. Each transition averages the 8 equally
likely next states, so it is a classic "expected/probability over random
steps" recurrence solved with memoization.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n^2 * k) |
| Space  | O(n^2 * k) |

Better Possible?
We must consider every (cell, remaining-step) state at least once, so
O(n^2 * k) time is optimal in the worst case. Space can be reduced to
O(n^2) by iterating step-by-step with two rolling probability grids instead
of caching all steps.
'''
