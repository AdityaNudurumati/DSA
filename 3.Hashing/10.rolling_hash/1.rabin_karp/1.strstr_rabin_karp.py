'''
1. Find the Index of the First Occurrence in a String / strStr (Easy)
Problem Statement

Given two strings haystack and needle, return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.

Here we solve it through the HASHING lens: instead of comparing the pattern char-by-char
at every position, we keep a polynomial rolling hash of the current window and slide it
along the haystack in O(1) per step (Rabin-Karp).

Example
Input:
haystack = "sadbutsad", needle = "sad"

Output:
0
Explanation:
"sad" occurs at index 0 and index 6; the first is index 0.
'''

BASE = 131
MOD = (1 << 61) - 1                      # large prime-ish modulus -> very low collision rate


def strStr(haystack, needle):

    n, m = len(haystack), len(needle)

    if m == 0:
        return 0                          # empty needle matches at index 0
    if m > n:
        return -1                         # pattern longer than text -> impossible

    # precompute BASE^(m-1) % MOD, used to drop the leftmost char when rolling
    high = pow(BASE, m - 1, MOD)

    # hash of the pattern, and hash of the first window of haystack
    target = 0
    window = 0
    for i in range(m):
        target = (target * BASE + ord(needle[i])) % MOD
        window = (window * BASE + ord(haystack[i])) % MOD

    for start in range(n - m + 1):
        # hashes match -> verify char-by-char to rule out a (rare) collision
        if window == target and haystack[start:start + m] == needle:
            return start

        # roll the window forward: drop haystack[start], append haystack[start+m]
        if start + m < n:
            window = (window - ord(haystack[start]) * high) % MOD   # remove leftmost
            window = (window * BASE + ord(haystack[start + m])) % MOD  # shift + add new

    return -1


if __name__ == "__main__":
    print(strStr("sadbutsad", "sad"))     # Expected: 0
    print(strStr("leetcode", "leeto"))    # Expected: -1

'''
Pattern
✅ Rabin-Karp — polynomial rolling hash

Technique & why
Hash the m-length pattern once. Keep a rolling hash of each m-length window of the text;
sliding from one window to the next costs O(1) by subtracting the leftmost char's
contribution (times BASE^(m-1)) and folding in the new char. Only when window hash ==
pattern hash do we spend O(m) verifying, which avoids naive O(nm) comparisons in the
common case.

| Metric | Value |
| ------ | ----- |
| Time   | O(n + m) average, O(nm) worst (adversarial collisions) |
| Space  | O(1) (besides the slice used for verification) |

Better Possible?
❌ Not asymptotically for average-case search; KMP gives guaranteed O(n + m) worst-case
but Rabin-Karp shines when matching many patterns / reusing hashes.
'''
