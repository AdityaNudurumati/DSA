'''
1. Longest Duplicate Substring (Hard)
Problem Statement

Given a string s, return any duplicated substring that has the longest possible length
(it occurs at least twice in s). If no duplicated substring exists, return "".

The answer length is MONOTONIC: if a duplicate of length L exists, duplicates of every
shorter length exist too. So we binary-search the length and, for each candidate L, use a
rolling hash to test "is there a repeated substring of length L?" in O(n). To avoid false
positives from hash collisions we use a DOUBLE hash (two independent moduli) as the key.

Example
Input:
s = "banana"

Output:
"ana"
Explanation:
"ana" appears at index 1 and index 3; it is the longest such repeated substring.
'''

BASE1, MOD1 = 131, (1 << 61) - 1
BASE2, MOD2 = 137, (1 << 61) - 15         # second independent prime modulus


def longestDupSubstring(s):

    n = len(s)
    nums = [ord(c) for c in s]

    # precompute powers of both bases up to n
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    for i in range(n):
        pow1[i + 1] = (pow1[i] * BASE1) % MOD1
        pow2[i + 1] = (pow2[i] * BASE2) % MOD2

    def search(L):
        # return start index of some duplicated substring of length L, or -1
        if L == 0:
            return 0

        h1 = h2 = 0
        for i in range(L):                # hash of the first window
            h1 = (h1 * BASE1 + nums[i]) % MOD1
            h2 = (h2 * BASE2 + nums[i]) % MOD2

        seen = {(h1, h2): 0}              # double-hash -> earliest start index

        for start in range(1, n - L + 1):
            # roll: drop nums[start-1], append nums[start+L-1]
            h1 = (h1 * BASE1 - nums[start - 1] * pow1[L] + nums[start + L - 1]) % MOD1
            h2 = (h2 * BASE2 - nums[start - 1] * pow2[L] + nums[start + L - 1]) % MOD2
            key = (h1, h2)
            if key in seen:
                return start              # collision across two moduli => real match
            seen[key] = start

        return -1

    # binary search on length: largest L for which a duplicate exists
    lo, hi = 1, n - 1
    best_start, best_len = 0, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        idx = search(mid)
        if idx != -1:
            best_start, best_len = idx, mid   # record and try longer
            lo = mid + 1
        else:
            hi = mid - 1                       # too long, shrink

    return s[best_start:best_start + best_len]


if __name__ == "__main__":
    print(longestDupSubstring("banana"))   # Expected: ana
    print(repr(longestDupSubstring("abcd")))  # Expected: ''

'''
Pattern
✅ Binary Search on Length + Rolling Hash (double hashing)

Technique & why
"Has a duplicate substring of length L" is monotonic in L, so binary-search L in
O(log n) steps. Each check rolls a fixed-length window hash across the string in O(n) and
records seen window hashes in a dict; a repeat means a duplicate. Using TWO independent
moduli (a double hash) makes accidental collisions astronomically unlikely, so we can
trust a hash match without an extra O(L) verification.

| Metric | Value |
| ------ | ----- |
| Time   | O(n log n) |
| Space  | O(n) |

Better Possible?
❌ This is the standard near-optimal solution; suffix automaton / suffix array can reach
O(n) but are far more complex and rarely needed in interviews.
'''
