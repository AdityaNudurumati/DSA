'''
1. Valid Anagram (Easy)
Problem Statement

Given two strings s and t, return True if t is an anagram of s, and False
otherwise. An anagram uses exactly the same letters with the same counts, just
in a different order.

Example
Input:
s = "anagram", t = "nagaram"

Output:
True
'''

from collections import Counter

def isAnagram(s, t):

    # different lengths can never be anagrams
    if len(s) != len(t):
        return False

    # two strings are anagrams iff their letter frequency maps match exactly
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))   # Expected: True
    print(isAnagram("rat", "car"))           # Expected: False

'''
Pattern
✅ Character Frequency Counting

Key Observation
Build a frequency map (Counter) of each string and compare them. Equal counts
for every character means the strings are anagrams.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
Space is O(1) for a fixed alphabet (at most 26 lowercase letters). Sorting both
strings also works but costs O(n log n) time.
'''
