'''
2. Group Anagrams (Medium)
Problem Statement

Given a list of strings, group together the ones that are anagrams of each other
(same letters, possibly reordered). Return the groups in any order.

Example
Input:
strs = ["eat","tea","tan","ate","nat","bat"]

Output (any order):
[["eat","tea","ate"], ["tan","nat"], ["bat"]]   # 3 groups
'''

from collections import defaultdict

def groupAnagrams(strs):

    groups = defaultdict(list)

    for s in strs:
        # signature = per-letter count tuple (26 buckets, 'a'..'z')
        # anagrams share the exact same letter counts, so they collide on this key.
        # O(len) to build vs O(len log len) for a sorted-letters key.
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        key = tuple(count)
        groups[key].append(s)

    return list(groups.values())


if __name__ == "__main__":
    result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # print sorted for a deterministic view
    print(sorted(sorted(g) for g in result))
    # Expected: [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
    print(len(result))
    # Expected: 3

'''
Pattern
✅ Grouping by a canonical-form signature (count tuple)

Key Observation
Two strings are anagrams iff their per-letter counts match. A 26-length count
tuple is the canonical signature and serves as the hashmap key. Building it is
O(len), beating the O(len log len) sorted-string key.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(N * K)       |
| Space  | O(N * K)       |

N = number of strings, K = max string length.

Better Possible?
❌ No.
'''
