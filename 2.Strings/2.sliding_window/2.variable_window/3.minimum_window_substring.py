'''
3. Minimum Window Substring (Hard)
Problem Statement

Given strings s and t, return the smallest substring of s that contains every
character of t (including duplicates). If no such window exists, return "".

Example
Input:
s = "ADOBECODEBANC", t = "ABC"

Output:
"BANC"
Explanation:
"BANC" is the shortest substring of s covering A, B and C.
'''

from collections import Counter

def minWindow(s, t):

    if not t or not s:
        return ""

    need = Counter(t)        # required char counts
    required = len(need)     # distinct chars we still must satisfy
    formed = 0               # distinct chars currently satisfied

    window = {}
    left = 0
    best_len = float("inf")
    best_left = 0

    for right in range(len(s)):

        c = s[right]                       # grow window to the right
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            formed += 1

        # window is valid: try to shrink from the left for a smaller one
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left

            lc = s[left]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                formed -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_left:best_left + best_len]


if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))   # Expected: BANC
    print(minWindow("a", "a"))                 # Expected: a
    print(minWindow("a", "aa"))                # Expected:

'''
Pattern
✅ Variable-Size Sliding Window (need / have counts)

Key Observation
Expand right until the window covers all of t (formed == required), then
contract left as far as possible while still valid, recording the best window.

| Metric | Value             |
| ------ | ----------------- |
| Time   | O(|s| + |t|)      |
| Space  | O(|s| + |t|)      |

Better Possible?
❌ No. Each pointer crosses the string once; linear is optimal.
'''
