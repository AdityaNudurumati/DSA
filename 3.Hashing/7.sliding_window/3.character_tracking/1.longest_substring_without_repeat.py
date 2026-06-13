'''
1. Longest Substring Without Repeating Characters (Medium)
Problem Statement

Given a string s, return the length of the longest substring that contains no
repeating characters.

In hashing terms: keep a map of each character -> its last-seen index. When a
character repeats inside the current window, jump the left boundary just past its
previous position.

Example
Input:
s = "abcabcbb"

Output:
3
Explanation:
The longest substring without repeats is "abc", of length 3.
'''

def lengthOfLongestSubstring(s):

    last_seen = {}      # char -> most recent index where it appeared
    left = 0            # left edge of the current window
    best = 0

    for right, ch in enumerate(s):
        # if ch was seen inside the window, move left past that occurrence
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right                 # record/refresh position
        best = max(best, right - left + 1)    # window size

    return best


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))    # Expected: 3
    print(lengthOfLongestSubstring("bbbbb"))       # Expected: 1
    print(lengthOfLongestSubstring("pwwkew"))      # Expected: 3

'''
Pattern
✅ Variable Sliding Window + Last-Seen HashMap

Key Observation
A last-seen index map lets the left pointer leap directly to one past a repeat,
instead of crawling. The guard last_seen[ch] >= left avoids resurrecting a position
that already fell out of the window, so left never moves backward.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1) (at most alphabet size keys) |

Better Possible?
❌ No — each character is visited once.
'''
