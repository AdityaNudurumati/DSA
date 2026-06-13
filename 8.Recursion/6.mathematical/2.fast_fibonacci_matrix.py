'''
2. Fast Fibonacci via Matrix Exponentiation (Medium)
Problem Statement

Compute the n-th Fibonacci number in O(log n) time.

Uses the identity:
    | 1 1 |^n   =  | F(n+1)  F(n)   |
    | 1 0 |        | F(n)    F(n-1) |

So raising the 2x2 base matrix to the n-th power yields F(n) in the
top-right (or bottom-left) cell. The matrix power is done by squaring.

Input:
n = 10

Output:
55

Explanation:
F = 0,1,1,2,3,5,8,13,21,34,55  ->  F(10) = 55
'''

def multiply(A, B):
    # Standard 2x2 matrix multiplication.
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0],
         A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0],
         A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def matrix_power(M, n):
    # Base case: M^0 = identity matrix.
    if n == 0:
        return [[1, 0], [0, 1]]
    # Exponentiation by squaring on matrices: M^n = (M^(n/2))^2.
    half = matrix_power(M, n // 2)
    squared = multiply(half, half)
    if n % 2 == 0:
        return squared
    return multiply(squared, M)


def fib(n):
    # F(0) = 0 directly; matrix power gives F(n) in cell [0][1].
    if n == 0:
        return 0
    result = matrix_power([[1, 1], [1, 0]], n)
    return result[0][1]


if __name__ == "__main__":
    print(fib(10))  # Expected: 55
    print(fib(50))  # Expected: 12586269025
    print(fib(0))   # Expected: 0


'''
Pattern
✅ Matrix Exponentiation
A linear recurrence (Fibonacci) is encoded as repeated multiplication by a
constant 2x2 matrix; raising that matrix to the n-th power by squaring gives
F(n) in O(log n) matrix multiplications instead of O(n) additions.
| Metric | Value    |
| ------ | -------- |
| Time   | O(log n) |
| Space  | O(log n) |  (recursion stack depth)
Better Possible?
❌ Not asymptotically
Fast-doubling does the same O(log n) with fewer multiplications, but the
big-O is identical. Naive iteration is O(n); naive recursion is O(2^n).
'''
