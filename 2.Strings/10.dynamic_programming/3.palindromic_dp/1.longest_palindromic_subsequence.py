'''
1. Longest Palindromic Subsequence (Medium)
Problem Statement

Given a string s, return the length of the longest palindromic subsequence
in s. A subsequence keeps relative order but need not be contiguous, and it
reads the same forwards and backwards.

Example

Input:
s = "bbbab"

Output:
4

Explanation:
The longest palindromic subsequence is "bbbb", which has length 4.
'''

def longestPalindromeSubseq(s):
    n = len(s)

    # dp[i][j] = LPS length within s[i..j]
    dp = [[0] * n for _ in range(n)]

    # single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # expand over increasing range lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # matching ends wrap the best inner range
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # drop one end, keep the better side
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


if __name__ == "__main__":
    print(longestPalindromeSubseq("bbbab"))  # Expected: 4
    print(longestPalindromeSubseq("cbbd"))   # Expected: 2


'''
Pattern
✅ Interval DP over [i..j] ranges
We grow palindromes outward: equal ends add 2 to the best inner range,
unequal ends drop whichever end helps less. (Equivalently, LCS of s and
its reverse.)

| Metric | Value   |
| ------ | ------- |
| Time   | O(n^2)  |
| Space  | O(n^2)  |

Better Possible?
Space reduces to O(n) with a rolling 1D array.
Time O(n^2) is optimal for this formulation.
'''
