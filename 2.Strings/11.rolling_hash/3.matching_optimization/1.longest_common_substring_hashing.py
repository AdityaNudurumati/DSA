'''
1. Longest Common Substring via Hashing (Hard)
Problem Statement

Given two strings a and b, find the LONGEST string that appears as a (contiguous)
substring of BOTH. Return that common substring (any one if several share the
max length), or "" if they share nothing.

Approach: binary-search on the LENGTH L. "Do a and b share a common substring of
length L?" is monotonic. To check it, hash every length-L window of a into a set,
then hash every length-L window of b and look for a match. Polynomial rolling
hashes make each window O(1); we verify a hit to dodge collisions.

Example
Input:
a = "abcde", b = "cdefg"

Output:
"cde"
Explanation:
"cde" (length 3) is the longest run present in both strings.
'''

BASE, MOD = 131, (1 << 61) - 1


def _prefix(s):
    # returns (prefix-hash array, power array) for O(1) window hashing
    n = len(s)
    h = [0] * (n + 1)
    p = [1] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * BASE + ord(s[i])) % MOD
        p[i + 1] = (p[i] * BASE) % MOD
    return h, p


def _has_common(a, b, ha, pa, hb, pb, L):
    # is there a shared substring of length L? return its start in `a` or -1
    if L == 0:
        return 0
    if L > len(a) or L > len(b):
        return -1

    def wa(l):                              # hash of a[l:l+L]
        return (ha[l + L] - ha[l] * pa[L]) % MOD

    def wb(l):
        return (hb[l + L] - hb[l] * pb[L]) % MOD

    # map each hash of a length-L window of `a` to one start index
    seen = {}
    for i in range(0, len(a) - L + 1):
        seen.setdefault(wa(i), i)

    for j in range(0, len(b) - L + 1):
        i = seen.get(wb(j))
        if i is not None and a[i:i + L] == b[j:j + L]:   # verify
            return i
    return -1


def longestCommonSubstring(a, b):
    ha, pa = _prefix(a)
    hb, pb = _prefix(b)

    lo, hi = 0, min(len(a), len(b))         # search the LENGTH
    start, best_len = 0, 0

    while lo <= hi:
        mid = (lo + hi) // 2
        idx = _has_common(a, b, ha, pa, hb, pb, mid)
        if idx != -1:
            start, best_len = idx, mid      # works — remember and try longer
            lo = mid + 1
        else:
            hi = mid - 1

    return a[start:start + best_len]


if __name__ == "__main__":
    r1 = longestCommonSubstring("abcde", "cdefg")
    print(r1, len(r1))                       # Expected: cde 3
    r2 = longestCommonSubstring("abc", "xyz")
    print(repr(r2), len(r2))                 # Expected: '' 0

'''
Pattern
String Matching Optimization: Binary Search on Length + rolling hash. Each
length check hashes all windows of both strings in O(n + m); binary search adds
a log factor over the answer length. Prefix hashing keeps window hashing O(1).

| Metric | Value                  |
| ------ | ---------------------- |
| Time   | O((n + m) log min(n,m))|
| Space  | O(n + m)               |

Better Possible?
A generalized suffix automaton / suffix array solves it in O(n + m) but is much
heavier to implement; binary-search + hashing is the practical interview choice.
'''
