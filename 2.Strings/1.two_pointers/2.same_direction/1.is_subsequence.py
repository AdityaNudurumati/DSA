'''
1. Is Subsequence (Easy)
Problem Statement

Given two strings s and t, return True if s is a subsequence of t.

A subsequence is formed by deleting zero or more characters from t without
changing the relative order of the remaining characters.

Example
Input:
s = "abc", t = "ahbgdc"

Output:
True
Explanation:
'a', 'b', 'c' appear in t in the same order.
'''

def isSubsequence(s, t):

    i = 0  # pointer into s

    # one pointer walks t; advance the s pointer only on a match
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1

    # matched every character of s
    return i == len(s)


if __name__ == "__main__":
    print(isSubsequence("abc", "ahbgdc"))  # Expected: True
    print(isSubsequence("axc", "ahbgdc"))  # Expected: False

'''
Pattern
Same Direction Two Pointers — both indices move forward through t; the s
index only advances when its current character is matched.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |  (n = len(t))
| Space  | O(1)  |

Better Possible?
No for a single query — t must be scanned once.
'''
