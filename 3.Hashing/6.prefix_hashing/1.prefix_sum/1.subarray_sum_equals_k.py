'''
1. Subarray Sum Equals K (Medium)
Problem Statement

Given an integer array nums and an integer k, return the total number of
contiguous subarrays whose elements sum to exactly k. The array may contain
negative numbers, so a sliding window will not work here.

Example
Input:
nums = [1,1,1], k = 2

Output:
2
Explanation:
The subarrays [1,1] (indices 0..1) and [1,1] (indices 1..2) each sum to 2.
'''

def subarraySum(nums, k):

    # prefix-sum value -> how many times it has occurred so far
    seen = {0: 1}          # empty prefix has sum 0, seen once
    running = 0
    count = 0

    for x in nums:
        running += x
        # a subarray summing to k ends here for every earlier prefix == running - k
        count += seen.get(running - k, 0)
        # record this prefix sum for future indices
        seen[running] = seen.get(running, 0) + 1

    return count


if __name__ == "__main__":
    print(subarraySum([1, 1, 1], 2))     # Expected: 2
    print(subarraySum([1, 2, 3], 3))     # Expected: 2
    print(subarraySum([1, -1, 0], 0))    # Expected: 3

'''
Pattern
✅ Prefix Sum + HashMap (count)

Key Observation
If prefix[j] - prefix[i] == k then the subarray (i, j] sums to k. So while
scanning, for each running prefix we ask how many earlier prefixes equal
running - k. A hashmap of prefix-sum frequencies answers this in O(1).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Negatives rule out two-pointer/sliding window; O(n) time is optimal.
'''
