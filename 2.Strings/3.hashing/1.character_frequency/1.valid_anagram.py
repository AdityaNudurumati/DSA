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

    # two strings are anagrams iff their letter counts match exactly
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))   # Expected: True
    print(isAnagram("rat", "car"))           # Expected: False

'''
Pattern
✅ Character Frequency Counting

Key Observation
Anagrams have identical per-character counts, so comparing two Counters answers
the question directly.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
Space is O(1) for fixed alphabets (at most 26 lowercase letters). Sorting both
strings also works but costs O(n log n) time.
'''
