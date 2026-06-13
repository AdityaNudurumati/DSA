'''
1. Fibonacci - All Four Forms (Easy)
Problem Statement

The Fibonacci sequence is defined as:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)   for n >= 2

Compute fib(n). This single file shows the full DP progression on one problem:
naive recursion -> memoization (top-down) -> tabulation (bottom-up) -> O(1) space.

Input:
n = 10

Output:
55
'''

import sys


# -------------------------------------------------------------------
# FORM 1: Naive recursion
# state:      fib(n) = nth Fibonacci number
# transition: fib(n) = fib(n-1) + fib(n-2)
# base:       fib(0) = 0, fib(1) = 1
# Recomputes overlapping subproblems -> exponential blow-up O(2^n).
# -------------------------------------------------------------------
def fib_recursive(n):
    if n < 2:                       # base: fib(0)=0, fib(1)=1
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# -------------------------------------------------------------------
# FORM 2: Memoization (top-down)
# Same recurrence, but cache each fib(n) the first time we solve it,
# so every state is computed exactly once -> O(n) time, O(n) space.
# -------------------------------------------------------------------
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n < 2:                       # base
        return n
    if n in cache:                  # already solved this state
        return cache[n]
    # transition
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


# -------------------------------------------------------------------
# FORM 3: Tabulation (bottom-up)
# Build a table from the base cases upward; no recursion.
# dp[i] = dp[i-1] + dp[i-2]        -> O(n) time, O(n) space
# -------------------------------------------------------------------
def fib_tabulation(n):
    if n < 2:                       # base
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1             # base cases
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]   # transition
    return dp[n]


# -------------------------------------------------------------------
# FORM 4: Space-optimized (O(1) space)
# We only ever need the previous two values, so keep two variables.
# a = fib(i-2), b = fib(i-1)       -> O(n) time, O(1) space
# -------------------------------------------------------------------
def fib_optimized(n):
    if n < 2:                       # base
        return n
    a, b = 0, 1                     # fib(0), fib(1)
    for _ in range(2, n + 1):
        a, b = b, a + b             # slide the window forward
    return b


if __name__ == "__main__":
    sys.setrecursionlimit(10000)

    n = 10
    print(fib_recursive(n))    # Expected: 55
    print(fib_memo(n))         # Expected: 55
    print(fib_tabulation(n))   # Expected: 55
    print(fib_optimized(n))    # Expected: 55

    # edge: fib(0)
    print(fib_optimized(0))    # Expected: 0


'''
Pattern
Dynamic Programming - the foundational progression of one problem.
Fibonacci has optimal substructure (fib(n) built from smaller fibs) and
overlapping subproblems (fib(n-2) is reused), which is exactly when DP applies.
The four forms walk the standard climb:
  1) recursion  - correct but recomputes subproblems (exponential)
  2) memoization - cache states top-down to kill the recomputation
  3) tabulation  - fill the same states bottom-up, no recursion stack
  4) space-opt   - notice only the last two states matter, drop the table

| Metric | Recursion | Memo | Tabulation | Optimized |
| ------ | --------- | ---- | ---------- | --------- |
| Time   | O(2^n)    | O(n) | O(n)       | O(n)      |
| Space  | O(n)*     | O(n) | O(n)       | O(1)      |
(* recursion stack depth)

Better Possible?
Yes for time: a matrix-power / fast-doubling method computes fib(n) in
O(log n). But O(n) time with O(1) space is the standard, clean answer here.
'''
