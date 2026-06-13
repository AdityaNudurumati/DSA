'''
3. Sort Characters By Frequency (Medium)
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

    # bucket sort: buckets[c] holds every character that occurs c times
    buckets = [[] for _ in range(len(s) + 1)]
    for ch, cnt in freq.items():
        buckets[cnt].append(ch)

    # walk buckets from highest count down, emitting each char count times
    result = []
    for cnt in range(len(s), 0, -1):
        for ch in buckets[cnt]:
            result.append(ch * cnt)

    return "".join(result)


if __name__ == "__main__":
    print(frequencySort("tree"))      # Expected: eert (or eetr)
    print(frequencySort("cccaaa"))    # Expected: cccaaa (or aaaccc)

'''
Pattern
✅ Character Frequency Counting (bucket sort by frequency)

Key Observation
Frequencies range from 1..n, so we can bucket characters by their count and read
the buckets from highest to lowest. This avoids any comparison-based sorting.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
O(n) time is optimal since the output itself has length n. Counter.most_common
also works but costs O(n + k log k) due to its internal heap/sort.
'''
