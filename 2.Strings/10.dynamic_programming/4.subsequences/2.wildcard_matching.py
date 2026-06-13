'''
2. Wildcard Matching (Hard)
Problem Statement

Given an input string s and a pattern p, return True if p matches the entire
string s. The pattern supports two wildcards:
  '?' matches any single character.
  '*' matches any sequence of characters, including the empty sequence.

Example

Input:
s = "adceb", p = "*a*b"

Output:
True

Explanation:
The first '*' matches the empty string, 'a' matches 'a', the second '*'
matches "dce", and 'b' matches 'b'.
'''

def isMatch(s, p):
    m, n = len(s), len(p)

    # dp[i][j] = True if s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # a leading run of '*' can match the empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' matches empty (dp[i][j-1]) or one more char (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # single-char match consumes both
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]


if __name__ == "__main__":
    print(isMatch("aa", "a"))       # Expected: False
    print(isMatch("aa", "*"))       # Expected: True
    print(isMatch("cb", "?a"))      # Expected: False
    print(isMatch("adceb", "*a*b"))  # Expected: True


'''
Pattern
✅ 2D matching DP over prefixes
'*' branches into "match empty" or "consume one more character"; '?' and a
literal match advance both pointers diagonally.

| Metric | Value   |
| ------ | ------- |
| Time   | O(m*n)  |
| Space  | O(m*n)  |

Better Possible?
Space reduces to O(n) with two rows.
A greedy two-pointer scan runs in O(m+n) average time and O(1) space.
'''
