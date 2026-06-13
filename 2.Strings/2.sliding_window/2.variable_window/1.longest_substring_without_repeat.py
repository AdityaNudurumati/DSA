'''
1. Longest Substring Without Repeating Characters (Medium)
Problem Statement

Given a string s, find the length of the longest substring that contains no
repeating characters.

Example
Input:
s = "abcabcbb"

Output:
3
Explanation:
The answer is "abc", with length 3.
'''

def lengthOfLongestSubstring(s):

    seen = {}        # char -> last index it appeared at
    left = 0         # left edge of the current valid window
    best = 0

    for right in range(len(s)):

        c = s[right]
        # if c repeats inside the window, jump left past its previous spot
        if c in seen and seen[c] >= left:
            left = seen[c] + 1

        seen[c] = right
        best = max(best, right - left + 1)   # window [left..right] is valid

    return best


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))   # Expected: 3
    print(lengthOfLongestSubstring("bbbbb"))      # Expected: 1
    print(lengthOfLongestSubstring("pwwkew"))     # Expected: 3

'''
Pattern
✅ Variable-Size Sliding Window

Key Observation
Grow the window to the right; when a duplicate enters, snap the left edge to
just past the duplicate's previous index. Each char is visited at most twice.

| Metric | Value           |
| ------ | --------------- |
| Time   | O(n)            |
| Space  | O(min(n, charset)) |

Better Possible?
❌ No. Linear time is optimal for scanning the string.
'''
