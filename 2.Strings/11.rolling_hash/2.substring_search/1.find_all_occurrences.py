'''
1. Find All Occurrences of a Pattern (Medium)
Problem Statement

Given a text and a pattern, return every start index in text where pattern
occurs (occurrences may overlap). This is Rabin-Karp: compute one hash of the
pattern, then slide a window of len(pattern) across text using a polynomial
rolling hash so each window's hash is updated in O(1). On a hash match we verify
the characters to guard against the rare collision.

We build prefix hashes of the text so any window hash is also available in O(1).

Example
Input:
text = "abababab", pat = "ab"

Output:
[0, 2, 4, 6]
Explanation:
"ab" starts at indices 0, 2, 4 and 6.
'''

BASE, MOD = 131, (1 << 61) - 1


def findAllOccurrences(text, pat):
    n, m = len(text), len(pat)
    if m == 0 or m > n:
        return []

    # hash of the pattern
    ph = 0
    for c in pat:
        ph = (ph * BASE + ord(c)) % MOD

    # prefix hashes of text + power table for O(1) window hashing
    h = [0] * (n + 1)
    p = [1] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * BASE + ord(text[i])) % MOD
        p[i + 1] = (p[i] * BASE) % MOD

    def window_hash(l, r):                 # hash of text[l:r)
        return (h[r] - h[l] * p[r - l]) % MOD

    res = []
    for i in range(0, n - m + 1):
        if window_hash(i, i + m) == ph:
            # verify to rule out a hash collision
            if text[i:i + m] == pat:
                res.append(i)
    return res


if __name__ == "__main__":
    print(findAllOccurrences("abababab", "ab"))  # Expected: [0, 2, 4, 6]
    print(findAllOccurrences("aaaaa", "aa"))      # Expected: [0, 1, 2, 3]

'''
Pattern
Substring Search via polynomial rolling hash (Rabin-Karp). Prefix hashing makes
every window's hash O(1), so the scan is linear; we only fall back to a direct
character compare on a hash hit, which is rare.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n + m) avg   |
| Space  | O(n)           |

Better Possible?
KMP / Z-algorithm give guaranteed worst-case O(n + m) with no collision risk;
those classics live in ../../4.pattern_matching/.
'''
