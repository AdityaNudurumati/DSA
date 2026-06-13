'''
2. Minimum Window Substring (Hard)
Problem Statement

Given strings s and t, return the smallest substring of s that contains every
character of t (including duplicates). If no such window exists, return "".

Example
Input:
s = "ADOBECODEBANC", t = "ABC"

Output:
"BANC"
'''

from collections import Counter

def minWindow(s, t):

    if not s or not t:
        return ""

    need = Counter(t)
    missing = len(t)        # total chars still required (with multiplicity)

    left = 0
    best_start, best_len = 0, float("inf")

    for right, ch in enumerate(s):

        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        # window now valid -> shrink from the left as much as possible
        while missing == 0:

            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1

            need[s[left]] += 1
            if need[s[left]] > 0:       # removed a character we actually need
                missing += 1
            left += 1

    return "" if best_len == float("inf") else s[best_start:best_start + best_len]


if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
    print(minWindow("a", "a"))                 # Expected: "a"
    print(minWindow("a", "aa"))                # Expected: ""

'''
Pattern
✅ Variable-Size Sliding Window + need-count hashmap

Key Observation
Expand right until the window is valid, then shrink left to minimize while still
valid. The "missing" counter makes validity an O(1) check.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(|s| + |t|)   |
| Space  | O(|t|)         |

Better Possible?
❌ No. Linear scan with each pointer moving forward only.
'''
