'''
1. Top K Frequent Elements (Medium)
Problem Statement

Given an integer array nums and an integer k, return the k most frequent
elements. The answer may be returned in any order.

Example
Input:
nums = [1, 1, 1, 2, 2, 3], k = 2

Output:
[1, 2]
'''

from collections import Counter

def topKFrequent(nums, k):

    freq = Counter(nums)

    # bucket sort: buckets[c] lists every value that occurs exactly c times
    buckets = [[] for _ in range(len(nums) + 1)]
    for val, cnt in freq.items():
        buckets[cnt].append(val)

    # walk buckets from highest frequency down, collecting until we have k values
    result = []
    for cnt in range(len(nums), 0, -1):
        for val in buckets[cnt]:
            result.append(val)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    print(sorted(topKFrequent([1, 1, 1, 2, 2, 3], 2)))   # Expected: [1, 2]
    print(sorted(topKFrequent([1], 1)))                  # Expected: [1]

'''
Pattern
✅ Top-K Frequency (bucket sort by frequency)

Key Observation
Counts range from 1..n, so index buckets by frequency and read them from the
highest bucket downward, gathering values until k are collected. No heap or full
sort is needed.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
O(n) is optimal. A heap-based approach costs O(n log k); bucket sort removes the
log factor by exploiting that frequencies are bounded by n.
'''
