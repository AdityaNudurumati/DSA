"""
231. Power of Two (Easy)

Problem Statement:
Given an integer n, return True if it is a power of two, otherwise False.
An integer n is a power of two if there exists an integer x such that n == 2**x.

Example:
    Input:  n = 1
    Output: True          (2**0)
    Input:  n = 16
    Output: True          (2**4)
    Input:  n = 3
    Output: False
    Input:  n = 0
    Output: False
"""


def is_power_of_two(n: int) -> bool:
    # A power of two has exactly ONE set bit (e.g. 16 = 10000).
    # Subtracting 1 flips that bit to 0 and turns all lower bits to 1
    # (16-1 = 01111), so n & (n-1) clears the only set bit -> 0.
    # Must also be positive (0 and negatives are never powers of two).
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    print(is_power_of_two(1))   # Expected: True
    print(is_power_of_two(16))  # Expected: True
    print(is_power_of_two(3))   # Expected: False
    print(is_power_of_two(0))   # Expected: False


"""
Pattern: Mathematical Bit Tricks.
Bit trick: n & (n - 1) clears the lowest set bit. If a positive number has only
one set bit (the definition of a power of two), clearing it yields 0. This is an
O(1) test with no loop, no logarithm, and no floating-point rounding error.

| Metric | Value |
| Time   | O(1)  |
| Space  | O(1)  |

Better Possible? No. This is already a single constant-time bitwise operation;
it cannot be improved asymptotically.
"""
