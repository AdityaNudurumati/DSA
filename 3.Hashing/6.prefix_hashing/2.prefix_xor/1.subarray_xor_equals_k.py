'''
1. Subarray XOR Equals K (Medium)
Problem Statement

Given an integer array nums and an integer k, return the number of contiguous
subarrays whose elements XOR together to exactly k.

Example
Input:
nums = [4,2,2,6,4], k = 6

Output:
4
Explanation:
The subarrays [4,2], [4,2,2,6,4], [2,2,6] and [6] each XOR to 6.
'''

def subarrayXor(nums, k):

    # prefix-xor value -> how many times it has occurred so far
    seen = {0: 1}          # empty prefix has xor 0, seen once
    running = 0
    count = 0

    for x in nums:
        running ^= x
        # xor(i, j] == k  <=>  prefix[i] == prefix[j] ^ k
        count += seen.get(running ^ k, 0)
        # record this prefix xor for future indices
        seen[running] = seen.get(running, 0) + 1

    return count


if __name__ == "__main__":
    print(subarrayXor([4, 2, 2, 6, 4], 6))    # Expected: 4
    print(subarrayXor([5, 6, 7, 8, 9], 5))    # Expected: 2

'''
Pattern
✅ Prefix XOR + HashMap

Key Observation
XOR is self-inverse, so the xor of subarray (i, j] equals prefix[j] ^ prefix[i].
We want this to equal k, i.e. prefix[i] == prefix[j] ^ k. Counting earlier
prefixes equal to running ^ k gives the answer, mirroring the prefix-sum trick.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. O(n) time and space is optimal for arbitrary values.
'''
