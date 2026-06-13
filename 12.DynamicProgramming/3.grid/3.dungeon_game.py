"""
174. Dungeon Game (Hard)

Problem Statement:
A knight starts at the top-left of a dungeon grid and must reach the princess
at the bottom-right, moving only right or down. Each cell adds (or subtracts)
health. If the knight's health drops to 0 or below at any point, he dies.
Return the minimum initial health needed to guarantee he survives the trip.

Example:
    Input:  [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    Output: 7

    Input:  [[0]]
    Output: 1
"""


def calculate_minimum_hp(dungeon):
    m, n = len(dungeon), len(dungeon[0])

    # Work BACKWARDS: dp[r][c] = minimum health needed *upon entering* (r, c)
    # so the knight survives the rest of the journey to the bottom-right.
    # The forward direction fails because future losses change what is "safe".
    dp = [[0] * n for _ in range(m)]

    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if (r, c) == (m - 1, n - 1):
                # Base: must end with at least 1 HP after the last cell.
                need = 1 - dungeon[r][c]
            else:
                down = dp[r + 1][c] if r + 1 < m else float("inf")
                right = dp[r][c + 1] if c + 1 < n else float("inf")
                # Transition: pick the cheaper next cell, then back out this
                # cell's health change; clamp to at least 1.
                need = min(down, right) - dungeon[r][c]
            dp[r][c] = max(need, 1)

    return dp[0][0]


if __name__ == "__main__":
    print(calculate_minimum_hp([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # Expected: 7
    print(calculate_minimum_hp([[0]]))                                       # Expected: 1


"""
Pattern: GRID DP — tabulation, computed in reverse.
Why: forward accumulation is non-optimal because a large gain now cannot offset
a future cliff that already killed the knight. Defining the state as the health
needed to enter a cell and filling from the destination outward makes the
recurrence dp[r][c] = max(1, min(dp[r+1][c], dp[r][c+1]) - dungeon[r][c]).

| Metric | Value      |
|--------|------------|
| Time   | O(m * n)   |
| Space  | O(m * n)   |

Better Possible?
Time is optimal. Space reduces to O(n) with a rolling row processed
right-to-left, bottom-to-top.
"""
