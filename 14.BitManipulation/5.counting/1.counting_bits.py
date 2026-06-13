'''
1. Counting Bits (Easy)
Problem Statement

Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Input:
n = 2

Output:
[0, 1, 1]

Example:
Input:  n = 5
Output: [0, 1, 1, 2, 1, 2]
'''

def countBits(n):
    # Bit trick: i has the same set bits as (i >> 1) plus the lowest bit (i & 1).
    # Dropping the last bit (i >> 1) is a number we already solved, so:
    #   dp[i] = dp[i >> 1] + (i & 1)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


if __name__ == "__main__":
    print(countBits(2))  # Expected: [0, 1, 1]
    print(countBits(5))  # Expected: [0, 1, 1, 2, 1, 2]


'''
Pattern
Bit Counting (DP on bits): dp[i] = dp[i >> 1] + (i & 1).
Why it works: i >> 1 removes the lowest bit, leaving a smaller index whose
popcount is already computed; (i & 1) re-adds whatever that lowest bit was.
This turns an O(n log n) "count each number" into one O(1) step per number.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
No. The output array itself is size n + 1, so O(n) time and space are optimal.
'''
