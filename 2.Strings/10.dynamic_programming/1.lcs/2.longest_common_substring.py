'''
2. Longest Common Substring (Medium)
Problem Statement

Given two strings a and b, return the length of the longest substring that
appears in both strings. A substring must be contiguous (unlike a
subsequence).

If there is no common substring, return 0.

Example

Input:
a = "abcde", b = "abfce"

Output:
2

Explanation:
The longest common substring is "ab", which has length 2.
'''

def longestCommonSubstring(a, b):
    m, n = len(a), len(b)

    # dp[i][j] = length of common substring ENDING at a[i-1] and b[j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                # extend the run that ended one char earlier in both
                dp[i][j] = dp[i - 1][j - 1] + 1
                best = max(best, dp[i][j])
            # mismatch resets the run to 0 (default value)

    return best


if __name__ == "__main__":
    print(longestCommonSubstring("abcde", "abfce"))  # Expected: 2
    print(longestCommonSubstring("abc", "abc"))       # Expected: 3
    print(longestCommonSubstring("abc", "def"))       # Expected: 0


'''
Pattern
✅ 2D DP over prefixes (substring variant of LCS)
Unlike LCS, a mismatch resets the run to 0 because substrings must be
contiguous; we track the global maximum over all (i, j).

| Metric | Value   |
| ------ | ------- |
| Time   | O(m*n)  |
| Space  | O(m*n)  |

Better Possible?
Space can be reduced to O(min(m, n)) with a rolling row.
Suffix automaton / suffix array gives O(m+n) but is far more complex.
'''
