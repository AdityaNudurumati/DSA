"""
1. Factorial (Easy)

Problem Statement:
Compute the factorial of a non-negative integer n using recursion.
n! = n * (n-1) * (n-2) * ... * 1, with the convention that 0! = 1.

Return n! for a given n.

Example:
    Input:  n = 5
    Output: 120
    Input:  n = 0
    Output: 1
"""


def factorial(n):
    # Base case: 0! and 1! are both 1.
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))   # Expected: 120
    print(factorial(0))   # Expected: 1


"""
Pattern: Linear Recursion.
Each call makes exactly one recursive call on a strictly smaller input (n -> n-1),
peeling off one factor per level until the base case 0!/1! = 1 is reached.

| Metric | Value |
| Time   | O(n)  |
| Space  | O(n) (recursion call stack) |

Better Possible?
An iterative loop achieves the same O(n) time with O(1) space, avoiding stack
overhead and recursion-depth limits. Recursion here is for clarity, not speed.
"""
