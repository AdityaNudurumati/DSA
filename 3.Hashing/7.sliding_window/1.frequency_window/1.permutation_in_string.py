'''
1. Permutation in String (Medium)
Problem Statement

Given two strings s1 and s2, return True if s2 contains a permutation of s1
(i.e. one of s1's permutations appears as a contiguous substring of s2).

In hashing terms: slide a fixed window of length len(s1) over s2 and check
whether the window's character-count map ever equals s1's count map.

Example
Input:
s1 = "ab", s2 = "eidbaooo"

Output:
True
Explanation:
s2 contains "ba", a permutation of "ab".
'''

from collections import Counter


def checkInclusion(s1, s2):

    n, m = len(s1), len(s2)
    if n > m:
        return False

    need = Counter(s1)              # target counts
    window = Counter(s2[:n])        # counts of the first fixed window

    if window == need:
        return True

    # slide the fixed-size window one char at a time
    for i in range(n, m):
        add = s2[i]                 # entering on the right
        drop = s2[i - n]            # leaving on the left

        window[add] += 1
        window[drop] -= 1
        if window[drop] == 0:
            del window[drop]        # keep map clean so == compares correctly

        if window == need:
            return True

    return False


if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))    # Expected: True
    print(checkInclusion("ab", "eidboaoo"))    # Expected: False

'''
Pattern
✅ Fixed-Size Sliding Window + Frequency Map

Key Observation
A permutation is just an anagram, so it has the SAME character counts. Maintain a
count map for a window of length len(s1) and compare it to s1's count map as the
window slides; deleting zeroed keys keeps the dict equality check O(alphabet).

| Metric | Value |
| ------ | ----- |
| Time   | O(m)  |
| Space  | O(1) (at most 26 keys) |

Better Possible?
❌ No — every char of s2 must be inspected at least once.
'''
