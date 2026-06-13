'''
5. Sort Characters By Frequency (Medium)
Problem Statement

Given a string s, sort it in decreasing order based on the frequency of the
characters. Return any valid answer (ties may be ordered arbitrarily).

Example
Input:
s = "tree"

Output:
"eert"   (or "eetr" — 'e' twice first, then 'r' and 't' in either order)
'''

from collections import Counter

def frequencySort(s):

    freq = Counter(s)

    # order characters by descending count, then repeat each char count times
    result = []
    for ch, cnt in freq.most_common():
        result.append(ch * cnt)

    return "".join(result)


if __name__ == "__main__":
    print(frequencySort("tree"))      # Expected: eert (or eetr)
    print(frequencySort("cccaaa"))    # Expected: cccaaa (or aaaccc)

'''
Pattern
✅ Character Frequency Counting (count then order by frequency)

Key Observation
Count characters, then emit each character repeated by its count in
descending-frequency order. Counter.most_common does the ranking.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(n + k log k)|
| Space  | O(n)          |

Better Possible?
Bucket sort by frequency (buckets indexed 1..n) removes the log k factor,
giving O(n) time. k = number of distinct characters.
'''
