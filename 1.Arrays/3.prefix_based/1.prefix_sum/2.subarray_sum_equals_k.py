'''
2. Subarray Sum Equals K (Medium)
Problem Statement

Given an integer array nums and an integer k, return the number of contiguous
subarrays whose sum equals k. Values can be negative.

Example
Input:
nums = [1,1,1], k = 2

Output:
2
Explanation:
[1,1] (indices 0-1) and [1,1] (indices 1-2).
'''

def subarraySum(nums, k):

    seen = {0: 1}       # prefix_sum -> how many times it has occurred
    running = 0
    count = 0

    for x in nums:
        running += x
        # a previous prefix of (running - k) means that gap sums to k
        count += seen.get(running - k, 0)
        seen[running] = seen.get(running, 0) + 1

    return count


if __name__ == "__main__":
    print(subarraySum([1, 1, 1], 2))        # Expected: 2
    print(subarraySum([1, 2, 3], 3))        # Expected: 2
    print(subarraySum([1, -1, 0], 0))       # Expected: 3

'''
Pattern
✅ Prefix Sum + Hashmap

Key Observation
sum(i..j) = prefix[j] - prefix[i-1]. Wanting that = k means we need a previous
prefix equal to (running - k). Count them with a hashmap in one pass.
(Sliding window fails here because negatives break monotonicity.)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
