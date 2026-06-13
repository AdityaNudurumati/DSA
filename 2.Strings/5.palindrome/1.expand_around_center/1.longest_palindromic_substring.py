'''
1. Longest Palindromic Substring (Medium)
Problem Statement

Given a string s, return the longest substring of s that is a palindrome.
A palindrome reads the same forward and backward. If several have the same
maximum length, returning any one of them is acceptable.

Example
Input:  s = "babad"
Output: "bab"        (or "aba")

Input:  s = "cbbd"
Output: "bb"
'''

def longestPalindrome(s):

    if not s:
        return ""

    start, end = 0, 0   # best palindrome boundaries found so far [start, end]

    # expand outward while characters match; returns the matched bounds (l+1, r-1)
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1   # last valid (inclusive) bounds

    for i in range(len(s)):
        # odd-length palindrome centered at i
        l1, r1 = expand(i, i)
        # even-length palindrome centered between i and i+1
        l2, r2 = expand(i, i + 1)

        # keep whichever center produced the longer palindrome
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


if __name__ == "__main__":
    print(longestPalindrome("babad"))  # Expected: bab
    print(longestPalindrome("cbbd"))   # Expected: bb

'''
Pattern
✅ Expand Around Center

Every palindrome has a center: a single char (odd length) or a gap between
two chars (even length). There are 2n-1 centers; expanding outward from each
and tracking the longest match finds the answer without extra space.

| Metric | Value |
| ------ | ----- |
| Time   | O(n²) |
| Space  | O(1)  |

Better Possible?
✅ Yes — Manacher's algorithm solves it in O(n). See ../2.manacher/
'''
