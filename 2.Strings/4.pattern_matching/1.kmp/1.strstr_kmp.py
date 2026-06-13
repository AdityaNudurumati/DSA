'''
1. Find the Index of First Occurrence in a String / strStr (Easy)
Problem Statement

Given two strings haystack and needle, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Algorithm: KMP (Knuth-Morris-Pratt) using an LPS (Longest Proper
Prefix which is also Suffix) array so the text is never re-scanned.

Example
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
'''


def build_lps(pattern):
    # lps[i] = length of the longest proper prefix of pattern[:i+1]
    # that is also a suffix. This tells us how far to fall back on mismatch.
    lps = [0] * len(pattern)
    k = 0  # length of the previous longest prefix-suffix
    for i in range(1, len(pattern)):
        # Fall back while the current char breaks the prefix match.
        while k and pattern[i] != pattern[k]:
            k = lps[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        lps[i] = k
    return lps


def strStr(haystack, needle):
    if not needle:
        return 0

    lps = build_lps(needle)
    k = 0  # number of chars of needle currently matched

    for i in range(len(haystack)):
        # On mismatch, jump back using the LPS instead of restarting.
        while k and haystack[i] != needle[k]:
            k = lps[k - 1]
        if haystack[i] == needle[k]:
            k += 1
        # Full match found; start index is i - (len(needle) - 1).
        if k == len(needle):
            return i - len(needle) + 1
    return -1


if __name__ == "__main__":
    print(strStr("sadbutsad", "sad"))   # Expected: 0
    print(strStr("leetcode", "leeto"))  # Expected: -1


'''
Pattern
KMP — precompute the LPS array of the pattern, then slide through the text
once. On a mismatch we shift the pattern by the longest known border, so the
text pointer never moves backwards (no re-scanning).

| Metric | Value    |
| ------ | -------- |
| Time   | O(n + m) |
| Space  | O(m)     |

Better Possible? No. Reading the text at least once is O(n); KMP already
matches that lower bound for exact single-pattern search.
'''
