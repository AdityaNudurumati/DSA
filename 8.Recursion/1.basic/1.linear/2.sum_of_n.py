"""
2. Sum of First N Natural Numbers (Easy)

Problem Statement:
Given a non-negative integer n, compute the sum of the first n natural numbers
recursively: 1 + 2 + 3 + ... + n. By convention the sum for n = 0 is 0.

Return the running sum for a given n.

Example:
    Input:  n = 10
    Output: 55
    Input:  n = 0
    Output: 0
"""


def sum_of_n(n):
    # Base case: sum of zero numbers is 0.
    if n <= 0:
        return 0
    # Recursive case: total = n + sum(1..n-1)
    return n + sum_of_n(n - 1)


if __name__ == "__main__":
    print(sum_of_n(10))   # Expected: 55
    print(sum_of_n(0))    # Expected: 0


"""
Pattern: Linear Recursion.
One recursive call per level, reducing n by 1 each time and adding n to the result
of the smaller subproblem until n reaches the base case 0.

| Metric | Value |
| Time   | O(n)  |
| Space  | O(n) (recursion call stack) |

Better Possible?
Yes: the closed-form n*(n+1)/2 gives O(1) time and O(1) space. An iterative loop
is O(n) time but O(1) space. Recursion is used here purely to illustrate the pattern.
"""
