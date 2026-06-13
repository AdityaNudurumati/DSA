'''
1. Maximum Sum Circular Subarray (Medium)
Problem Statement

Given a circular integer array nums, return the maximum possible sum of a non-empty
subarray. Circular means the subarray may wrap from the end back to the front, but
each element is used at most once.

Example
Input:
nums = [5,-3,5]

Output:
10
Explanation:
Wrap around: [5, 5] using the two 5s = 10.
'''

def maxSubarraySumCircular(nums):

    total = 0

    # standard Kadane for the maximum subarray
    cur_max = 0
    best_max = float("-inf")

    # inverse Kadane for the minimum subarray
    cur_min = 0
    best_min = float("inf")

    for x in nums:
        cur_max = max(x, cur_max + x)
        best_max = max(best_max, cur_max)

        cur_min = min(x, cur_min + x)
        best_min = min(best_min, cur_min)

        total += x

    # all-negative: the wrap case (total - best_min) would be empty -> invalid
    if best_max < 0:
        return best_max

    # answer is either the normal max, or total minus the worst middle slice (wrap)
    return max(best_max, total - best_min)


if __name__ == "__main__":
    print(maxSubarraySumCircular([1, -2, 3, -2]))  # Expected: 3
    print(maxSubarraySumCircular([5, -3, 5]))       # Expected: 10
    print(maxSubarraySumCircular([-3, -2, -3]))     # Expected: -2
    print(maxSubarraySumCircular([3, -2, 2, -3]))   # Expected: 3

'''
Pattern
✅ Kadane (max) + Inverse Kadane (min), combined

Key Observation
A wrapping subarray = total - (a non-wrapping subarray in the middle). To maximize
the wrap, minimize the middle slice -> total - best_min. Guard the all-negative
case, where total - best_min would correspond to an empty subarray.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
