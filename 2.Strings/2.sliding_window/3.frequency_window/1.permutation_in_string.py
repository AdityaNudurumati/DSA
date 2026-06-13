'''
1. Permutation in String (Medium)
Problem Statement

Given two strings s1 and s2, return True if s2 contains a permutation of s1,
i.e. some substring of s2 (of length len(s1)) is an anagram of s1.

Example
Input:
s1 = "ab", s2 = "eidbaooo"

Output:
True
Explanation:
s2 contains the substring "ba", which is a permutation of "ab".
'''

from collections import Counter

def checkInclusion(s1, s2):

    k = len(s1)
    if k > len(s2):
        return False

    need = Counter(s1)      # target char frequencies
    window = Counter()      # frequencies in the current k-length window

    for right in range(len(s2)):

        window[s2[right]] += 1           # add entering char

        if right >= k - 1:
            if window == need:           # equal multiset => permutation found
                return True

            left_char = s2[right - k + 1]    # drop leftmost char
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

    return False


if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))   # Expected: True
    print(checkInclusion("ab", "eidboaoo"))   # Expected: False

'''
Pattern
✅ Frequency Window (fixed length, char-count map)

Key Observation
A permutation of s1 is any substring of length len(s1) whose char-count map
equals that of s1. Slide a fixed window of that length comparing counts.

| Metric | Value            |
| ------ | ---------------- |
| Time   | O(|s2|)          |
| Space  | O(1) (<=26 keys) |

Better Possible?
❌ No. Every window position must be checked once.
'''
