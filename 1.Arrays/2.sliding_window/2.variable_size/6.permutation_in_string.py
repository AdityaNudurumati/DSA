'''
6. Permutation in String (Medium)
Problem Statement

Given two strings s1 and s2, return True if s2 contains a PERMUTATION of s1 as a
contiguous substring (i.e. some window of s2 is an anagram of s1), else False.

Example
Input:
s1 = "ab", s2 = "eidbaooo"

Output:
True
Explanation:
s2 contains "ba" (index 3), which is a permutation of "ab".
'''

from collections import Counter

def checkInclusion(s1, s2):

    k = len(s1)
    if k > len(s2):
        return False

    need = Counter(s1)      # target letter frequencies
    window = Counter()      # frequencies in the current width-k window

    for i in range(len(s2)):

        window[s2[i]] += 1                  # add entering char

        if i >= k:                          # window too wide -> drop leftmost
            left_char = s2[i - k]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

        if i >= k - 1 and window == need:   # window is an anagram of s1
            return True

    return False


if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))   # Expected: True
    print(checkInclusion("ab", "eidboaoo"))    # Expected: False
    print(checkInclusion("adc", "dcda"))       # Expected: True
    print(checkInclusion("abc", "ab"))         # Expected: False

'''
Pattern
✅ Fixed-Size Sliding Window + Frequency Map (anagram detection)

Key Observation
A permutation of s1 is any window of length len(s1) whose letter-count map equals
s1's map. Slide a width-k window over s2, add/drop one char per step, and compare
maps; return True on the first match. (Same machinery as Count Anagrams, but it
STOPS at the first hit instead of counting.)

| Metric | Value                     |
| ------ | ------------------------- |
| Time   | O(n) (26-key map compare) |
| Space  | O(1) (<=26 keys)          |

Better Possible?
❌ No. Each character of s2 enters and leaves the window once -> O(n).
'''
