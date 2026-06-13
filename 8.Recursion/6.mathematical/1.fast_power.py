'''
1. Pow(x, n) (Medium)
Problem Statement

Implement pow(x, n), which calculates x raised to the power n (x^n).

Handle negative exponents (x^-n = 1 / x^n) and n = 0 (returns 1).

Input:
x = 2.0, n = 10

Output:
1024.0

Explanation:
2^10 = 1024
'''

def myPow(x, n):
    # Negative exponent -> invert base and flip sign of n.
    if n < 0:
        x = 1 / x
        n = -n
    return fast_power(x, n)


def fast_power(x, n):
    # Base case: anything^0 = 1.
    if n == 0:
        return 1.0
    # Exponentiation by squaring: x^n = (x^(n/2))^2.
    half = fast_power(x, n // 2)
    if n % 2 == 0:
        return half * half
    # Odd exponent: one extra factor of x.
    return half * half * x


if __name__ == "__main__":
    print(myPow(2, 10))   # Expected: 1024.0
    print(myPow(2.0, -2)) # Expected: 0.25
    print(myPow(2, 0))    # Expected: 1.0


'''
Pattern
✅ Fast Power (Exponentiation by Squaring)
Halve the exponent each step using x^n = (x^(n/2))^2, so we do O(log n)
multiplications instead of O(n). Negative n handled by inverting the base.
| Metric | Value    |
| ------ | -------- |
| Time   | O(log n) |
| Space  | O(log n) |  (recursion stack depth)
Better Possible?
❌ No
Each squaring halves the exponent, so log n multiplications is optimal.
Space can be reduced to O(1) with an iterative version.
'''
