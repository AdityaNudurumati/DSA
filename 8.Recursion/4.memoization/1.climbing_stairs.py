'''
1. Climbing Stairs (Easy)   [LC70]
Problem Statement

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Input:
n = 3

Output:
3

Explanation:
1+1+1, 1+2, 2+1  ->  3 distinct ways.
'''

from functools import lru_cache


def climbStairs(n):
    # ways(i) = ways(i-1) + ways(i-2)  (last step is 1 or 2)
    @lru_cache(maxsize=None)
    def ways(i):
        if i <= 1:           # 0 or 1 step: exactly one way
            return 1
        return ways(i - 1) + ways(i - 2)

    return ways(n)


if __name__ == "__main__":
    print(climbStairs(3))   # Expected: 3
    print(climbStairs(5))   # Expected: 8
    print(climbStairs(45))  # Expected: 1836311903


'''
Pattern
✅ Recursive DP (Memoization)
The recurrence f(n)=f(n-1)+f(n-2) has overlapping subproblems; caching each
state i collapses the exponential tree into linear work.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
✅ Yes
Iterative bottom-up with two rolling variables gives O(n) time, O(1) space.
'''
