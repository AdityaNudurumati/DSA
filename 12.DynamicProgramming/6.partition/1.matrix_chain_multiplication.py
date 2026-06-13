'''
1. Matrix Chain Multiplication (Hard)
Problem Statement

You are given an array dims of length n+1 describing a chain of n matrices,
where matrix i has dimensions dims[i-1] x dims[i].

Multiplying an a x b matrix by a b x c matrix costs a * b * c scalar
multiplications. Matrix multiplication is associative, so the order of
multiplication does not change the result but does change the cost.

Find the minimum number of scalar multiplications needed to compute the
full chain product.

Example
Input:
dims = [1, 2, 3, 4]

Output:
18
Explanation:
Matrices A(1x2), B(2x3), C(3x4).
((AB)C) costs 1*2*3 + 1*3*4 = 6 + 12 = 18  (optimal).
'''

from functools import lru_cache


def matrixChainOrder(dims):
    n = len(dims) - 1  # number of matrices
    if n <= 1:
        return 0

    # State: dp(i, j) = min cost to multiply matrices i..j (1-indexed).
    # Matrix k spans dims[k-1] x dims[k].
    # Transition: try every split k in [i, j-1]; the two sub-products are
    #   dims[i-1] x dims[k]  and  dims[k] x dims[j], merged at cost
    #   dims[i-1] * dims[k] * dims[j].
    #   dp(i, j) = min over k of dp(i, k) + dp(k+1, j) + dims[i-1]*dims[k]*dims[j]
    # Base: i == j  -> single matrix, cost 0.
    @lru_cache(None)
    def dp(i, j):
        if i == j:
            return 0
        best = float("inf")
        for k in range(i, j):
            cost = dp(i, k) + dp(k + 1, j) + dims[i - 1] * dims[k] * dims[j]
            best = min(best, cost)
        return best

    return dp(1, n)


if __name__ == "__main__":
    print(matrixChainOrder([1, 2, 3, 4]))           # Expected: 18
    print(matrixChainOrder([10, 20, 30, 40, 30]))   # Expected: 30000
    print(matrixChainOrder([40, 20, 30, 10, 30]))   # Expected: 26000

'''
Pattern
Partition DP (Interval DP)

Which DP & Why
We choose a partition point k inside the interval [i, j], recursively solve the
left chain (i..k) and right chain (k+1..j), then pay to combine the two
resulting matrices. Optimal-substructure over an interval with an inner split
loop is the textbook partition / interval DP signature.

| Metric | Value  |
| ------ | ------ |
| Time   | O(n^3) |
| Space  | O(n^2) |

Better Possible?
The O(n^3) DP is the standard interval-DP solution. Hu-Shing's algorithm solves
it in O(n log n) but is far more intricate and rarely needed in practice, so the
cubic DP is the optimal practical answer.
'''
