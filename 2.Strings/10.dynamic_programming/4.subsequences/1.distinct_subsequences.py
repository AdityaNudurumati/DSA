'''
1. Distinct Subsequences (Hard)
Problem Statement

Given two strings s and t, return the number of distinct subsequences of s
that equal t. A subsequence keeps relative order but can skip characters.

Example

Input:
s = "rabbbit", t = "rabbit"

Output:
3

Explanation:
There are 3 ways to pick "rabbit" from "rabbbit" by choosing which of the
three 'b' characters to keep.
'''

def numDistinct(s, t):
    m, n = len(s), len(t)

    # dp[i][j] = number of ways t[:j] appears as a subsequence of s[:i]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # empty t matches any prefix of s exactly one way (delete everything)
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # always option: skip s[i-1]
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                # plus: use s[i-1] to match t[j-1]
                dp[i][j] += dp[i - 1][j - 1]

    return dp[m][n]


if __name__ == "__main__":
    print(numDistinct("rabbbit", "rabbit"))  # Expected: 3
    print(numDistinct("babgbag", "bag"))     # Expected: 5


'''
Pattern
✅ 2D counting DP over prefixes
For each character of s we either skip it or, when it matches the current
target char, also add the ways that used it. Empty target is the base case
with exactly one way.

| Metric | Value   |
| ------ | ------- |
| Time   | O(m*n)  |
| Space  | O(m*n)  |

Better Possible?
Space reduces to O(n) with a 1D array iterated right-to-left.
Time O(m*n) is optimal for the general case.
'''
