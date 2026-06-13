'''
2. Subarray Sums Divisible by K (Medium)
Problem Statement

Given an integer array nums and an integer k, return the number of contiguous
subarrays whose sum is divisible by k (sum % k == 0). The array may contain
negative numbers.

Example
Input:
nums = [4,5,0,-2,-3,1], k = 5

Output:
7
Explanation:
Seven subarrays have a sum divisible by 5, including the whole array and [5],
[5,0], [0], [-2,-3], [-3,1,4,... etc].
'''

def subarraysDivByK(nums, k):

    # remainder of the running prefix sum -> how many prefixes had that remainder
    seen = {0: 1}          # empty prefix has remainder 0, seen once
    running = 0
    count = 0

    for x in nums:
        running += x
        # python % already returns a non-negative remainder for positive k,
        # which correctly normalizes negative running sums
        r = running % k
        # two prefixes with the same remainder => the slice between is divisible by k
        count += seen.get(r, 0)
        seen[r] = seen.get(r, 0) + 1

    return count


if __name__ == "__main__":
    print(subarraysDivByK([4, 5, 0, -2, -3, 1], 5))    # Expected: 7
    print(subarraysDivByK([5], 9))                     # Expected: 0

'''
Pattern
✅ Prefix Sum Modulo + HashMap (count)

Key Observation
If two prefix sums leave the same remainder mod k, the subarray between them is
divisible by k. So we count, for each remainder, how many earlier prefixes
shared it. Python's % normalizes negatives, so no manual ((r % k) + k) % k fix
is needed.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(min(n, k)) |

Better Possible?
❌ No. O(n) time is optimal; space is bounded by the number of distinct remainders.
'''
