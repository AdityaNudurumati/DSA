'''
4. Ransom Note (Easy)
Problem Statement

Given two strings ransomNote and magazine, return True if ransomNote can be
constructed using the letters of magazine. Each letter in magazine may be used
at most once.

Example
Input:
ransomNote = "aa", magazine = "aab"

Output:
True
'''

from collections import Counter

def canConstruct(ransomNote, magazine):

    need = Counter(ransomNote)   # letters required
    have = Counter(magazine)     # letters available

    # every required letter must be available in at least the needed amount
    for ch, cnt in need.items():
        if have[ch] < cnt:
            return False

    return True


if __name__ == "__main__":
    print(canConstruct("a", "b"))      # Expected: False
    print(canConstruct("aa", "aab"))   # Expected: True

'''
Pattern
✅ Character Frequency Counting (subset / containment)

Key Observation
ransomNote is buildable iff every letter's required count does not exceed its
available count in magazine. Counter subtraction expresses this cleanly.

| Metric | Value |
| ------ | ----- |
| Time   | O(n + m) |
| Space  | O(1)  |

Better Possible?
O(n + m) is optimal. Space is O(1) for a fixed 26-letter alphabet
(n, m = string lengths).
'''
