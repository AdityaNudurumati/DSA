'''
1. Longest Substring Without Repeating Characters (Medium)
Problem Statement

Given a string s, find the length of the longest substring without repeating
characters.

Example
Input:
s = "abcabcbb"

Output:
3
Explanation:
The answer is "abc", length 3.
'''

def lengthOfLongestSubstring(s):

    last_seen = {}      # char -> most recent index
    left = 0
    best = 0

    for right, ch in enumerate(s):

        # if ch repeats inside the current window, jump left past it
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    print(lengthOfLongestSubstring("bbbbb"))      # Expected: 1
    print(lengthOfLongestSubstring("pwwkew"))     # Expected: 3

'''
Pattern
✅ Variable-Size Sliding Window + hashmap of last index

| Metric | Value           |
| ------ | --------------- |
| Time   | O(n)            |
| Space  | O(min(n, charset)) |

Better Possible?
❌ No. Each character is visited at most twice (enter, leave).
'''
