'''
1. Group Shifted Strings (Medium)
Problem Statement

A string can be "shifted" by advancing every letter by the same amount (with wrap
'z'->'a'), e.g. "abc" -> "bcd" -> ... Group all strings that belong to the same
shifting sequence. Return the groups in any order.

Example
Input:
strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

Output (any order):
[["abc","bcd","xyz"], ["acef"], ["az","ba"], ["a","z"]]
'''

from collections import defaultdict

def groupStrings(strings):

    groups = defaultdict(list)

    for s in strings:
        # signature = gaps between consecutive letters, mod 26 (wrap-around)
        # shifted strings share the same gap sequence
        key = tuple((ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s)))
        groups[key].append(s)

    return list(groups.values())


if __name__ == "__main__":
    result = groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
    # print sorted for a deterministic view
    print(sorted(sorted(g) for g in result))
    # Expected: [['a', 'z'], ['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba']]

'''
Pattern
✅ Grouping by a shift-invariant signature

Key Observation
Two strings are shifts of each other iff the differences between consecutive
characters (mod 26) are identical. That gap tuple is the hashmap key.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(total chars)|
| Space  | O(total chars)|

Better Possible?
❌ No.
'''
