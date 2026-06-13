'''
2. Delete Operation for Two Strings (Medium)
Problem Statement

Given two strings word1 and word2, return the minimum number of deletions
required to make the two strings equal. In one step you may delete exactly
one character from either string.

Example

Input:
word1 = "sea", word2 = "eat"

Output:
2

Explanation:
Delete 's' from "sea" to get "ea", then delete 't' from "eat" to get "ea".
'''

def minDeletionDistance(word1, word2):
    m, n = len(word1), len(word2)

    # dp[i][j] = LCS length of word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = dp[m][n]
    # delete everything outside the common subsequence in both strings
    return (m - lcs) + (n - lcs)


if __name__ == "__main__":
    print(minDeletionDistance("sea", "eat"))        # Expected: 2
    print(minDeletionDistance("leetcode", "etco"))  # Expected: 4


'''
Pattern
✅ 2D DP over prefixes (LCS reduction)
The characters we keep form the longest common subsequence; everything
else in each string must be deleted, so the answer is m + n - 2*LCS.

| Metric | Value   |
| ------ | ------- |
| Time   | O(m*n)  |
| Space  | O(m*n)  |

Better Possible?
Space reduces to O(min(m, n)) with a rolling row.
Time O(m*n) is optimal for the general case.
'''
