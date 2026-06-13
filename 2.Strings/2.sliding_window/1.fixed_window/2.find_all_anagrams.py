'''
2. Find All Anagrams in a String (Medium)
Problem Statement

Given two strings s and p, return a list of the start indices of all
substrings of s that are anagrams of p. The window length is fixed at len(p),
so this is a fixed-size window with a frequency check.

Example
Input:
s = "cbaebabacd", p = "abc"

Output:
[0, 6]
Explanation:
"cba" starts at index 0 and "bac" starts at index 6 are anagrams of "abc".
'''

from collections import Counter

def findAnagrams(s, p):

    k = len(p)
    if k > len(s):
        return []

    need = Counter(p)        # target char frequencies
    window = Counter()       # frequencies in the current k-length window
    result = []

    for right in range(len(s)):

        window[s[right]] += 1            # add entering char

        if right >= k - 1:
            if window == need:           # same multiset of chars => anagram
                result.append(right - k + 1)

            left_char = s[right - k + 1] # drop leftmost char
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]    # keep Counter clean for == check

    return result


if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))   # Expected: [0, 6]
    print(findAnagrams("abab", "ab"))          # Expected: [0, 1, 2]

'''
Pattern
✅ Fixed-Size Sliding Window + Frequency Map

Key Observation
An anagram is just a permutation, so two substrings are anagrams iff their
char-count maps are equal. Slide a window of length len(p) and compare counts.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n)           |
| Space  | O(1) (<=26 keys) |

Better Possible?
❌ No. Linear scan is required to inspect every window.
'''
