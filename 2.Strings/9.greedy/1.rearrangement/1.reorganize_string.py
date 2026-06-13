'''
1. Reorganize String (Medium)
Problem Statement

Given a string s, rearrange the characters so that no two adjacent characters
are the same.

Return any valid rearrangement. If it is impossible, return an empty string "".

Example
Input:  s = "aab"
Output: "aba"        (any valid arrangement, e.g. no two adjacent equal)

Input:  s = "aaab"
Output: ""           (impossible: 'a' appears too many times)
'''

import heapq
from collections import Counter


def reorganizeString(s):
    n = len(s)
    counts = Counter(s)

    # Greedy idea: always place the currently most-frequent char next.
    # Feasible only if the max count <= (n + 1) // 2.
    if max(counts.values()) > (n + 1) // 2:
        return ""

    # Max-heap on frequency (negate counts since heapq is a min-heap).
    heap = [(-cnt, ch) for ch, cnt in counts.items()]
    heapq.heapify(heap)

    result = []
    prev = None  # the char placed last turn, held back so it can't repeat

    while heap:
        cnt, ch = heapq.heappop(heap)  # most frequent available char
        result.append(ch)
        # Release the previously held char back into the heap now that a
        # different char sits between it and its earlier placement.
        if prev and prev[0] < 0:
            heapq.heappush(heap, prev)
        # Hold the current char with its decremented count for next turn.
        prev = (cnt + 1, ch)

    return "".join(result)


def is_valid(original, result):
    # Valid means: same multiset of chars AND no two adjacent equal.
    if Counter(original) != Counter(result):
        return False
    return all(result[i] != result[i + 1] for i in range(len(result) - 1))


if __name__ == "__main__":
    r1 = reorganizeString("aab")
    print(is_valid("aab", r1))            # Expected: True
    r2 = reorganizeString("aaab")
    print(r2 == "")                       # Expected: True


'''
Pattern
✅ Greedy Rearrangement with a Max-Heap
Place the most-frequent remaining char each step, holding back the just-used
char one turn so it cannot land adjacent to itself.
| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log k) |
| Space  | O(k)       |
(k = number of distinct characters, at most 26)
Better Possible?
❌ Not asymptotically. O(n) is achievable by filling even then odd indices
   from the most-frequent char, but the heap approach is the standard.
'''
