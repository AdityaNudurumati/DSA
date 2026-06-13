'''
1. Count Pairs With Sum (Two Sum frequency variation) (Medium)
Problem Statement

Given an array nums and an integer target, count the number of unordered index
pairs (i, j) with i < j such that nums[i] + nums[j] == target. Duplicate values
matter: each distinct pair of indices counts separately.

Example
Input:
nums = [1, 5, 7, 1], target = 6

Output:
2     (pairs (0,1)=1+5 and (1,3)=5+1)
'''

from collections import Counter

def countPairs(nums, target):

    seen = Counter()   # value -> how many times it has appeared so far
    pairs = 0

    # for each number, every earlier occurrence of its complement forms a pair
    for x in nums:
        complement = target - x
        pairs += seen[complement]
        seen[x] += 1

    return pairs


if __name__ == "__main__":
    print(countPairs([1, 5, 7, 1], 6))     # Expected: 2
    print(countPairs([1, 1, 1, 1], 2))     # Expected: 6

'''
Pattern
✅ Element Frequency Counting (complement lookup with counts)

Key Observation
Scan left to right keeping a frequency map of values already seen. For each new
value x, the count of target - x in the map is exactly how many valid pairs it
closes, so we accumulate that count. This naturally handles duplicates.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
O(n) time is optimal as each element is visited once. A two-pointer approach on
a sorted array uses O(1) extra space but costs O(n log n) for the sort.
'''
