'''
2. Group Anagrams (Medium)
Problem Statement

Given an array of strings strs, group the anagrams together. Two words belong to
the same group if one is a rearrangement of the other. Return the groups in any
order.

Example
Input:
strs = ["eat","tea","tan","ate","nat","bat"]

Output:
[["eat","tea","ate"],["tan","nat"],["bat"]]
'''

from collections import defaultdict

def groupAnagrams(strs):

    groups = defaultdict(list)

    for s in strs:
        # a 26-length count tuple is the same for every anagram -> use as key
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)

    return list(groups.values())


if __name__ == "__main__":
    result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(len(result))   # Expected: 3
    print(result)        # Expected (any order): [['eat','tea','ate'], ['tan','nat'], ['bat']]

'''
Pattern
✅ Character Frequency Counting (canonical signature)

Key Observation
A canonical signature (here a 26-count tuple) is identical for all anagrams, so
hashing on it groups them in one pass.

| Metric | Value    |
| ------ | -------- |
| Time   | O(n * k) |
| Space  | O(n * k) |

Better Possible?
This count-tuple key already avoids the O(k log k) sort that the
sorted(s) signature would cost. n = number of words, k = max word length.
'''
