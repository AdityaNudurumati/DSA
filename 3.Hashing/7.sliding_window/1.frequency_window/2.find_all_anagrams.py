'''
2. Find All Anagrams in a String (Medium)
Problem Statement

Given strings s and p, return a list of the start indices of all substrings of s
that are anagrams of p, in ascending order.

In hashing terms: slide a fixed window of length len(p) over s and record every
start index where the window's character-count map equals p's count map.

Example
Input:
s = "cbaebabacd", p = "abc"

Output:
[0, 6]
Explanation:
"cba" starts at 0 and "bac" starts at 6 are anagrams of "abc".
'''

from collections import Counter


def findAnagrams(s, p):

    n, m = len(p), len(s)
    res = []
    if n > m:
        return res

    need = Counter(p)               # target counts
    window = Counter(s[:n])         # first fixed window

    if window == need:
        res.append(0)

    # slide the fixed-size window across s
    for i in range(n, m):
        add = s[i]                  # entering on the right
        drop = s[i - n]             # leaving on the left

        window[add] += 1
        window[drop] -= 1
        if window[drop] == 0:
            del window[drop]        # drop zeroed key so equality stays exact

        if window == need:
            res.append(i - n + 1)   # window start index

    return res


if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))    # Expected: [0, 6]
    print(findAnagrams("abab", "ab"))           # Expected: [0, 1, 2]

'''
Pattern
✅ Fixed-Size Sliding Window + Frequency Map

Key Observation
Anagrams share identical character counts. Keep a count map for a window of length
len(p); each time it matches p's map, the window start is an answer. Pruning zeroed
keys keeps the dict comparison bounded by the alphabet size.

| Metric | Value |
| ------ | ----- |
| Time   | O(m)  |
| Space  | O(1) (at most 26 keys) |

Better Possible?
❌ No — output itself can be O(m); the scan is already linear.
'''
