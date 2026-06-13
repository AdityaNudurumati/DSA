'''
1. Longest Duplicate Substring (Hard)
Problem Statement

Given a string s, find the LONGEST substring that occurs at least twice in s
(occurrences may overlap). If no duplicated substring exists, return "".

The trick: binary-search on the answer's LENGTH. "Is there a duplicate of
length L?" is monotonic — if length L duplicates, so does any shorter length.
For a fixed L we slide a rolling hash over every window of size L and look for
a repeated hash. To avoid hash collisions giving a wrong answer we use DOUBLE
hashing (two independent base/mod pairs) — a clash on both is astronomically
unlikely.

Example
Input:
s = "banana"

Output:
"ana"
Explanation:
"ana" appears at index 1 and index 3 — the longest such repeat.
'''

# two independent (base, mod) pairs => double hashing crushes collisions
BASE1, MOD1 = 131, (1 << 61) - 1
BASE2, MOD2 = 137, 1_000_000_007


def _search(s, L):
    # is there a duplicate substring of length L? return its start index or -1
    n = len(s)
    if L == 0:
        return 0
    if L > n:
        return -1

    # precompute BASE^L for removing the leftmost char of the window
    p1 = pow(BASE1, L, MOD1)
    p2 = pow(BASE2, L, MOD2)

    h1 = h2 = 0
    for i in range(L):
        h1 = (h1 * BASE1 + ord(s[i])) % MOD1
        h2 = (h2 * BASE2 + ord(s[i])) % MOD2

    seen = {(h1, h2): 0}          # combined hash -> start index of first sight

    for i in range(L, n):
        # roll: drop s[i-L], add s[i]
        h1 = (h1 * BASE1 - ord(s[i - L]) * p1 + ord(s[i])) % MOD1
        h2 = (h2 * BASE2 - ord(s[i - L]) * p2 + ord(s[i])) % MOD2
        key = (h1, h2)
        if key in seen:
            return i - L + 1
        seen[key] = i - L + 1

    return -1


def longestDupSubstring(s):
    lo, hi = 1, len(s) - 1      # search the LENGTH of the duplicate
    start, best_len = -1, 0

    while lo <= hi:
        mid = (lo + hi) // 2
        idx = _search(s, mid)
        if idx != -1:
            # length mid works — try longer, remember this answer
            start, best_len = idx, mid
            lo = mid + 1
        else:
            hi = mid - 1

    return s[start:start + best_len] if start != -1 else ""


if __name__ == "__main__":
    print(longestDupSubstring("banana"))   # Expected: ana
    print(longestDupSubstring("abcd"))      # Expected:

'''
Pattern
Double Hashing + Binary Search on Length. The "yes/no for length L" question
is monotonic, so binary search picks the answer length in O(log n) rounds; each
round slides a rolling hash in O(n). Two hash pairs make a false match between
distinct substrings practically impossible.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
A suffix automaton / suffix array solves it in O(n) but is far more code; the
hashing approach is the standard interview answer.
'''
