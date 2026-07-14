'''
7. Subarray Product Less Than K (Medium)
Problem Statement

Given an array of POSITIVE integers nums and an integer k, return the number of
contiguous subarrays whose product of all elements is STRICTLY LESS THAN k.

Example
Input:
nums = [10,5,2,6], k = 100

Output:
8
Explanation:
[10],[5],[2],[6],[10,5],[5,2],[2,6],[5,2,6]  (product < 100)
'''

def numSubarrayProductLessThanK(nums, k):

    if k <= 1:                 # no positive-integer product can be < 1
        return 0

    prod = 1
    left = 0
    count = 0

    for right in range(len(nums)):

        prod *= nums[right]                 # extend window on the right

        while prod >= k:                    # shrink until product < k again
            prod //= nums[left]
            left += 1

        # every subarray ENDING at 'right' inside [left..right] is valid;
        # there are (right - left + 1) of them
        count += right - left + 1

    return count


if __name__ == "__main__":
    print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))   # Expected: 8
    print(numSubarrayProductLessThanK([1, 2, 3], 0))          # Expected: 0
    print(numSubarrayProductLessThanK([1, 1, 1], 2))          # Expected: 6
    print(numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 7, 3], 19))  # Expected: 17

'''
Pattern
✅ Variable-Size Sliding Window (count via "subarrays ending at right")

Key Observation
All values are positive, so extending the window can only GROW the product and
shrinking can only SHRINK it -> monotonic, so a sliding window works. When the
window [left..right] has product < k, it contributes (right-left+1) new valid
subarrays: exactly the ones ending at 'right'. Guard k <= 1 (impossible).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. left and right each move forward at most n times -> O(n).
'''
