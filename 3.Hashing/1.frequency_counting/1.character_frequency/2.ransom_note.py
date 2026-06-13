'''
2. Ransom Note (Easy)
Problem Statement

Given two strings ransomNote and magazine, return True if ransomNote can be
constructed using the letters of magazine, and False otherwise. Each letter in
magazine may be used at most once.

Example
Input:
ransomNote = "aa", magazine = "aab"

Output:
True
'''

from collections import Counter

def canConstruct(ransomNote, magazine):

    # count how many of each letter the magazine supplies
    available = Counter(magazine)

    # every letter the note needs must be covered by the available counts
    need = Counter(ransomNote)
    for ch, cnt in need.items():
        if available[ch] < cnt:
            return False

    return True


if __name__ == "__main__":
    print(canConstruct("a", "b"))     # Expected: False
    print(canConstruct("aa", "aab"))  # Expected: True

'''
Pattern
✅ Character Frequency Counting

Key Observation
Count the letters the magazine offers, then confirm each letter required by the
note has enough supply. A single letter shortfall makes construction impossible.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n + m)       |
| Space  | O(1)           |

Better Possible?
Space is O(1) for a fixed alphabet (26 lowercase letters). n and m are the
lengths of the note and magazine; counting both is already optimal.
'''
