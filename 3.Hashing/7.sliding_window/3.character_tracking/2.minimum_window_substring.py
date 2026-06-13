'''
2. Minimum Window Substring (Hard)
Problem Statement

Given strings s and t, return the shortest substring of s that contains every
character of t (including duplicates). If no such window exists, return "".

In hashing terms: a "need" count map of t plus a running "have" count for the
window; expand right to satisfy all needs, then shrink left to minimize.

Example
Input:
s = "ADOBECODEBANC", t = "ABC"

Output:
"BANC"
Explanation:
"BANC" is the shortest substring covering A, B, and C.
'''

from collections import Counter


def minWindow(s, t):

    if not t or not s:
        return ""

    need = Counter(t)            # required count per char
    required = len(need)         # number of distinct chars fully satisfied target
    have = {}                    # current window counts
    formed = 0                   # how many distinct chars meet their required count

    best_len = float("inf")
    best_left = 0
    left = 0

    for right, ch in enumerate(s):
        have[ch] = have.get(ch, 0) + 1

        # this char just reached exactly its needed count
        if ch in need and have[ch] == need[ch]:
            formed += 1

        # window is valid -> try shrinking from the left
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left

            lch = s[left]
            have[lch] -= 1
            if lch in need and have[lch] < need[lch]:
                formed -= 1      # window broke a requirement
            left += 1

    return "" if best_len == float("inf") else s[best_left:best_left + best_len]


if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))    # Expected: BANC
    print(minWindow("a", "a"))                  # Expected: a
    print(minWindow("a", "aa"))                 # Expected:

'''
Pattern
✅ Variable Sliding Window + need/have Count Maps

Key Observation
Track how many distinct required chars are fully satisfied (formed vs required).
Expand right until the window is valid, then greedily shrink left while it stays
valid, recording the smallest valid window. Each pointer moves at most n steps.

| Metric | Value |
| ------ | ----- |
| Time   | O(s + t) |
| Space  | O(s + t) |

Better Possible?
❌ No — linear in the input lengths is optimal.
'''
