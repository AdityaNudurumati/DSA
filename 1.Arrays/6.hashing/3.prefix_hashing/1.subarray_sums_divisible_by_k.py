'''
1. Subarray Sums Divisible by K (Medium)
Problem Statement

Given an integer array nums and an integer k, return the number of contiguous
subarrays whose sum is divisible by k.

Example
Input:
nums = [4,5,0,-2,-3,1], k = 5

Output:
7
'''

def subarraysDivByK(nums, k):

    count = {0: 1}      # remainder of a prefix sum -> how many times it occurred
    running = 0
    result = 0

    for x in nums:
        running += x
        r = running % k         # Python's % is always in [0, k) for k > 0
        # two prefixes with the same remainder bound a subarray divisible by k
        result += count.get(r, 0)
        count[r] = count.get(r, 0) + 1

    return result


if __name__ == "__main__":
    print(subarraysDivByK([4, 5, 0, -2, -3, 1], 5))   # Expected: 7
    print(subarraysDivByK([5], 9))                     # Expected: 0

'''
Pattern
✅ Prefix Sum + Remainder Hashing

Key Observation
sum(i..j) % k == 0  iff  prefix[j] and prefix[i-1] share the same remainder mod k.
Count equal-remainder prefixes with a hashmap. Python's % keeps remainders
non-negative, so negative numbers need no special handling.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(k)  |

Better Possible?
❌ No.
'''
