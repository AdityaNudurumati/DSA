'''
1. Longest Common Subsequence (Medium)
Problem Statement

Given two strings text1 and text2, return the length of their longest
common subsequence. A subsequence keeps the relative order of characters
but does not have to be contiguous.

If there is no common subsequence, return 0.

Example

Input:
text1 = "abcde", text2 = "ace"

Output:
3

Explanation:
The longest common subsequence is "ace", which has length 3.
'''

def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)

    # dp[i][j] = LCS length of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                # matching chars extend the diagonal best
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # drop one char from either string, keep the better
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    print(longestCommonSubsequence("abcde", "ace"))  # Expected: 3
    print(longestCommonSubsequence("abc", "abc"))     # Expected: 3
    print(longestCommonSubsequence("abc", "def"))     # Expected: 0


'''
Pattern
✅ 2D DP over prefixes (LCS)
We compare prefixes of both strings; a match extends the diagonal,
a mismatch takes the best of dropping one character from either side.

| Metric | Value   |
| ------ | ------- |
| Time   | O(m*n)  |
| Space  | O(m*n)  |

Better Possible?
Space can be reduced to O(min(m, n)) by keeping only two rows.
Time O(m*n) is optimal for the general case.
'''
