"""
1. Fibonacci (naive double recursion) (Easy)

Problem Statement:
The Fibonacci sequence is defined as fib(0) = 0, fib(1) = 1, and
fib(n) = fib(n-1) + fib(n-2) for n >= 2.
Compute fib(n) using the naive double-recursion definition (no memoization).

Example:
    Input:  n = 0   -> Output: 0
    Input:  n = 1   -> Output: 1
    Input:  n = 10  -> Output: 55
"""


def fib(n):
    # Base cases: fib(0) = 0, fib(1) = 1.
    if n < 2:
        return n
    # Recursive case: two calls per level -> multiple (tree) recursion.
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(0))    # Expected: 0
    print(fib(1))    # Expected: 1
    print(fib(10))   # Expected: 55


"""
Pattern: Multiple (Tree) Recursion.
Each call spawns two recursive calls, building a binary recursion tree. The same
subproblems are recomputed many times, which is the inefficiency this naive form shows.

| Metric | Value |
| Time   | O(2^n) (exponential, golden-ratio ~ O(1.618^n)) |
| Space  | O(n) (max recursion depth along one path) |

Better Possible?
Yes, dramatically. Memoization or bottom-up DP gives O(n) time / O(n) space
(O(1) space if only the last two values are kept). A matrix-power / fast-doubling
method reaches O(log n). The memoized version lives in ../4.memoization/.
"""
