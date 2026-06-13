'''
3. Regular Expression Matching (Hard)
Problem Statement

Given an input string s and a pattern p, return True if p matches the entire
string s. The pattern supports:
  '.' matches any single character.
  '*' matches zero or more of the PRECEDING element.

Example

Input:
s = "ab", p = ".*"

Output:
True

Explanation:
".*" means "zero or more of any character", which matches "ab" entirely.
'''

def isMatch(s, p):
    m, n = len(s), len(p)

    # dp[i][j] = True if s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # patterns like a*, a*b*, .* can match the empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' = zero of preceding element -> drop "x*"
                dp[i][j] = dp[i][j - 2]
                # or one more, if preceding element matches s[i-1]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # single-char match consumes both
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]


if __name__ == "__main__":
    print(isMatch("aa", "a"))                    # Expected: False
    print(isMatch("aa", "a*"))                   # Expected: True
    print(isMatch("ab", ".*"))                   # Expected: True
    print(isMatch("mississippi", "mis*is*p*."))  # Expected: False


'''
Pattern
✅ 2D matching DP over prefixes
'*' pairs with its preceding token: "zero occurrences" skips two pattern
chars, "one more" consumes a string char when the preceding token matches.
'.' and literals advance diagonally.

| Metric | Value   |
| ------ | ------- |
| Time   | O(m*n)  |
| Space  | O(m*n)  |

Better Possible?
Space reduces to O(n) with two rows.
Time O(m*n) is the standard optimal bound for this DP.
'''
