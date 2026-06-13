'''
1. First Unique Character in a String (Easy)
Problem Statement

Given a string s, find the first non-repeating character and return its index.
If every character repeats (or the string is empty), return -1.

Example
Input:  s = "leetcode"
Output: 0
Input:  s = "loveleetcode"
Output: 2
Input:  s = "aabb"
Output: -1
'''

from collections import Counter


def firstUniqChar(s):
    counts = Counter(s)                 # ordered counts: char -> frequency
    for i, ch in enumerate(s):          # scan left to right, indices ascending
        if counts[ch] == 1:             # first char seen exactly once
            return i                    # its index is the earliest unique
    return -1                           # no unique character found


if __name__ == "__main__":
    print(firstUniqChar("leetcode"))        # Expected: 0
    print(firstUniqChar("loveleetcode"))    # Expected: 2
    print(firstUniqChar("aabb"))            # Expected: -1

'''
Pattern
✅ Ordered Hashing (frequency map + insertion-order scan)

Key Observation
A Counter builds char -> frequency in one pass. Because we then scan the string in its
original (ordered) sequence, the first character whose count is 1 is guaranteed to be the
earliest unique one. Two linear passes, constant-size alphabet space.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(k) (k = distinct chars, <= alphabet size) |

Better Possible?
❌ Must read every character once, so O(n) time is optimal.
'''
