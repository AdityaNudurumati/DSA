'''
1. Find the Index of First Occurrence in a String / strStr (Easy)
Problem Statement

Given two strings haystack and needle, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Algorithm: Rabin-Karp using a polynomial rolling hash. Compare the hash of
each length-m window of the text to the pattern hash; only verify character
by character when the hashes match (to guard against collisions).

Example
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
'''

BASE = 256        # alphabet size for the polynomial hash
MOD = 1_000_000_007


def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    if m > n:
        return -1

    # highest_pow = BASE^(m-1) % MOD, used to remove the leading char.
    highest_pow = pow(BASE, m - 1, MOD)

    pattern_hash = 0
    window_hash = 0
    # Build the hash of the pattern and the first window together.
    for i in range(m):
        pattern_hash = (pattern_hash * BASE + ord(needle[i])) % MOD
        window_hash = (window_hash * BASE + ord(haystack[i])) % MOD

    for start in range(n - m + 1):
        # Hashes equal -> verify the actual substring (collision guard).
        if window_hash == pattern_hash and haystack[start:start + m] == needle:
            return start
        # Roll the window forward by one character in O(1).
        if start < n - m:
            window_hash = (window_hash - ord(haystack[start]) * highest_pow) % MOD
            window_hash = (window_hash * BASE + ord(haystack[start + m])) % MOD
            window_hash %= MOD
    return -1


if __name__ == "__main__":
    print(strStr("sadbutsad", "sad"))   # Expected: 0
    print(strStr("leetcode", "leeto"))  # Expected: -1


'''
Pattern
Rabin-Karp — treat each window as a base-256 number mod a large prime. Sliding
the window is O(1) (drop the leading digit, add the trailing digit), so the
whole scan is linear on average. Verify on hash hits to defeat collisions.

| Metric | Value                  |
| ------ | ---------------------- |
| Time   | O(n + m) avg, O(nm) wc |
| Space  | O(1)                   |

Better Possible? For a single pattern, KMP gives a worst-case O(n + m)
guarantee. Rabin-Karp shines for multi-pattern search and 2D matching where
hashing many patterns at once is cheap.
'''
