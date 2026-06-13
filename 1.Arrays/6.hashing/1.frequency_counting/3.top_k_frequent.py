'''
3. Top K Frequent Elements (Medium)
Problem Statement

Given an integer array nums and an integer k, return the k most frequent elements.
Return them in any order.

Example
Input:
nums = [1,1,1,2,2,3], k = 2

Output:
[1,2]
'''

from collections import Counter

def topKFrequent(nums, k):

    count = Counter(nums)
    n = len(nums)

    # bucket sort: index = frequency, value = list of numbers with that frequency
    buckets = [[] for _ in range(n + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(n, 0, -1):       # walk from most frequent down
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))   # Expected (any order): [1, 2]
    print(topKFrequent([1], 1))                   # Expected: [1]

'''
Pattern
✅ Frequency Counting + Bucket Sort

Key Observation
Frequencies range from 1..n, so bucket by frequency to read off the top k in O(n)
without sorting. (A heap gives O(n log k).)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ Not asymptotically; O(n) is optimal here.
'''
