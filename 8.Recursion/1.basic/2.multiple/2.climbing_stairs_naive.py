"""
2. Climbing Stairs (naive recursion) (Easy)

Problem Statement:
You are climbing a staircase with n steps. Each time you can climb either 1 or 2
steps. In how many distinct ways can you reach the top?
Solve with naive recursion (no memoization).

Example:
    Input:  n = 3   -> Output: 3   (1+1+1, 1+2, 2+1)
    Input:  n = 5   -> Output: 8
"""


def climb_stairs(n):
    # Base cases: 0 steps -> 1 empty way; 1 step -> 1 way.
    if n <= 1:
        return 1
    # Recursive case: last move is a 1-step or a 2-step -> sum both subproblems.
    return climb_stairs(n - 1) + climb_stairs(n - 2)


if __name__ == "__main__":
    print(climb_stairs(3))   # Expected: 3
    print(climb_stairs(5))   # Expected: 8


"""
Pattern: Multiple (Tree) Recursion.
Identical structure to Fibonacci: every state branches into "took 1 step" and
"took 2 steps", forming a binary recursion tree with heavy overlapping subproblems.

| Metric | Value |
| Time   | O(2^n) (exponential) |
| Space  | O(n) (recursion depth) |

Better Possible?
Yes: memoization or bottom-up DP reduces this to O(n) time and O(1) space (only the
previous two counts are needed). The memoized version lives in ../4.memoization/.
"""
