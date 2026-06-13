'''
2. Longest Happy Prefix (Hard)
Problem Statement

A "happy prefix" is a non-empty prefix of a string which is also a suffix
(excluding the whole string itself). Given a string s, return the longest
happy prefix; return "" if no such prefix exists.

Algorithm: Z-Algorithm. Compute the Z-array of s. A prefix of length L is also
a suffix when some position i satisfies i + Z[i] == n and Z[i] == n - i.
Scanning left to right, the first such i gives the longest happy prefix.
(The KMP/LPS failure function would solve this equivalently.)

Example
Input:  s = "level"
Output: "l"
Input:  s = "ababab"
Output: "abab"
Input:  s = "leetcodeleet"
Output: "leet"
'''


def z_array(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def longest_happy_prefix(s):
    n = len(s)
    z = z_array(s)
    # Walk from the smallest start index (longest candidate) outward.
    # A prefix==suffix means the match starting at i reaches the end.
    for i in range(1, n):
        if i + z[i] == n and z[i] == n - i:
            return s[:n - i]  # this prefix length is n - i
    return ""


if __name__ == "__main__":
    print(longest_happy_prefix("level"))         # Expected: l
    print(longest_happy_prefix("ababab"))        # Expected: abab
    print(longest_happy_prefix("leetcodeleet"))  # Expected: leet


'''
Pattern
Z-Algorithm — the Z-array tells us, for each index, how much of the prefix is
re-matched there. The earliest index whose match runs exactly to the end of
the string is a prefix that is also a suffix, and being earliest makes it the
longest. (KMP's lps[-1] gives the same answer.)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible? No. Both Z and KMP achieve the optimal O(n); a brute-force
prefix/suffix comparison would be O(n^2).
'''
