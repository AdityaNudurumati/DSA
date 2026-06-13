'''
2. Group Anagrams (Medium)
Problem Statement

Given an array of strings strs, group the anagrams together. Return the groups in
any order.

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
        # anagrams share the same sorted-letter signature
        key = tuple(sorted(s))
        groups[key].append(s)

    return list(groups.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected (any order): [['eat','tea','ate'], ['tan','nat'], ['bat']]
    print(groupAnagrams([""]))    # Expected: [['']]
    print(groupAnagrams(["a"]))   # Expected: [['a']]

'''
Pattern
✅ Frequency / Signature Hashing

Key Observation
A canonical signature (sorted letters, or a 26-count tuple) is identical for
anagrams, so it groups them directly in a hashmap.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(n * k log k)| (k = max word length; counts version is O(n*k))
| Space  | O(n * k)      |

Better Possible?
Using a 26-length count tuple as the key drops the log k sort factor.
'''
