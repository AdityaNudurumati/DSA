'''
1. Longest Palindromic Substring in O(n) — Manacher's Algorithm
Problem Statement

Given a string s, return its longest palindromic substring, but do it in
linear time. Manacher's algorithm computes, for every center, the radius of
the palindrome there while reusing previously computed radii via a mirror,
giving O(n) overall. If several share the max length, any is acceptable.

Example
Input:  s = "babad"
Output: "bab"        (or "aba")

Input:  s = "cbbd"
Output: "bb"

Input:  s = "a"
Output: "a"
'''

def longestPalindrome(s):

    if not s:
        return ""

    # Transform "abc" -> "^#a#b#c#$" so every palindrome becomes odd-length.
    # ^ and $ are unique sentinels so we never run off the ends.
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n          # p[i] = radius of palindrome centered at t[i]
    center = right = 0   # current rightmost palindrome: its center and right edge

    for i in range(1, n - 1):
        mirror = 2 * center - i   # i's mirror position around `center`

        if i < right:
            # reuse the mirror's radius, but don't expand past the right edge
            p[i] = min(right - i, p[mirror])

        # attempt to expand the palindrome centered at i
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # if it expands past the current right edge, recenter
        if i + p[i] > right:
            center, right = i, i + p[i]

    # find the largest radius and its center in the transformed string
    max_len, center_index = max((p[i], i) for i in range(n))
    # map back to original string: start = (center_index - max_len) // 2
    start = (center_index - max_len) // 2
    return s[start:start + max_len]


if __name__ == "__main__":
    print(longestPalindrome("babad"))  # Expected: aba  (bab also valid)
    print(longestPalindrome("cbbd"))   # Expected: bb
    print(longestPalindrome("a"))      # Expected: a

'''
Pattern
✅ Manacher's Algorithm

Insert separators so all palindromes are odd-length, then sweep left to right
keeping the rightmost palindrome (center, right). For each i, seed p[i] from
its mirror inside that range so work is never repeated; only expansion beyond
the right edge costs new comparisons, giving amortized O(n).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No — must read every character at least once, so O(n) time is optimal.
This is the linear-time upgrade over ../1.expand_around_center/ (O(n²)).
'''
