'''
1. Continuous Subarray Sum (Medium)
Problem Statement

Given an integer array nums and an integer k, return True if there is a contiguous
subarray of length >= 2 whose sum is a multiple of k (i.e. sum % k == 0).

Example
Input:
nums = [23,2,4,6,7], k = 6

Output:
True
Explanation:
[2,4] sums to 6, a multiple of 6.
'''

def checkSubarraySum(nums, k):

    # remainder of the running prefix sum -> the EARLIEST index it appeared
    seen = {0: -1}
    running = 0

    for i, x in enumerate(nums):
        running += x
        r = running % k

        if r in seen:
            # same remainder twice => the slice between them sums to a multiple of k
            if i - seen[r] >= 2:
                return True
        else:
            seen[r] = i        # keep earliest index to maximize window length

    return False


if __name__ == "__main__":
    print(checkSubarraySum([23, 2, 4, 6, 7], 6))    # Expected: True
    print(checkSubarraySum([23, 2, 6, 4, 7], 6))    # Expected: True  (whole array sums to 42)
    print(checkSubarraySum([23, 2, 6, 4, 7], 13))   # Expected: False

'''
Pattern
✅ Prefix Sum Modulo + HashMap

Key Observation
If two prefix sums share the same remainder mod k, the subarray between them is
divisible by k. Store the earliest index per remainder and require a gap of >= 2.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(min(n, k)) |

Better Possible?
❌ No.

Related: Subarray Sums Divisible by K (counts them) -> ../../../1.Arrays/6.hashing/3.prefix_hashing/
'''
