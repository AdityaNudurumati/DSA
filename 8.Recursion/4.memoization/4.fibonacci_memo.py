'''
4. Fibonacci (memoized) (Easy)
Problem Statement

The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1.

Given n, return F(n). Use memoization so the naive exponential recursion
becomes linear.

Input:
n = 50

Output:
12586269025

Explanation:
The 50th Fibonacci number.
'''

from functools import lru_cache


def fib(n):
    @lru_cache(maxsize=None)
    def f(k):
        if k < 2:            # F(0)=0, F(1)=1
            return k
        return f(k - 1) + f(k - 2)

    return f(n)


if __name__ == "__main__":
    print(fib(50))  # Expected: 12586269025
    print(fib(0))   # Expected: 0


'''
Pattern
✅ Recursive DP (Memoization)
Classic overlapping-subproblems example: naive recursion recomputes f(k)
exponentially; caching each k makes every value computed exactly once.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
✅ Yes
Iterative two-variable rollup gives O(1) space; Fast-doubling gives O(log n).
'''
