'''
3. First Unique Character in a String (Easy)
Problem Statement

Given a string s, return the index of the first character that appears exactly
once. If no such character exists, return -1.

Example
Input:
s = "leetcode"

Output:
0
'''

from collections import Counter

def firstUniqChar(s):

    # count every character first
    freq = Counter(s)

    # scan left to right; the first char with count 1 is the answer
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1


if __name__ == "__main__":
    print(firstUniqChar("leetcode"))       # Expected: 0
    print(firstUniqChar("loveleetcode"))   # Expected: 2
    print(firstUniqChar("aabb"))           # Expected: -1

'''
Pattern
✅ Character Frequency Counting

Key Observation
One pass builds the counts; a second left-to-right pass returns the first index
whose count is 1, preserving original order.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
O(n) time is optimal (every char must be examined). Space is O(1) for a fixed
alphabet of 26 letters.
'''
