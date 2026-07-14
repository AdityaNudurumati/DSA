'''
5. First Missing Positive (Hard)   [LC41]
Problem Statement

Given an unsorted integer array nums (any integers, positive/negative/zero),
return the SMALLEST missing POSITIVE integer. Must run in O(n) time and O(1)
extra space.

Cyclic sort, ignoring values outside 1..n (they can't be the first missing
positive within this array's reach). Then the first index i with nums[i] != i+1
gives answer i+1; if all match, the answer is n+1.

Example
Input:
nums = [3, 4, -1, 1]

Output:
2
'''

def firstMissingPositive(nums):

    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i] - 1
        # only place values in the valid range 1..n
        if 0 <= correct < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for idx in range(n):
        if nums[idx] != idx + 1:
            return idx + 1
    return n + 1


if __name__ == "__main__":
    print(firstMissingPositive([3, 4, -1, 1]))    # Expected: 2
    print(firstMissingPositive([1, 2, 0]))         # Expected: 3
    print(firstMissingPositive([7, 8, 9, 11, 12])) # Expected: 1

'''
Pattern
✅ Cyclic Sort (ignore out-of-range values)

Key Observation
The first missing positive of an n-length array must lie in 1..n+1. So values
<=0 or >n are irrelevant - skip them and cyclic-sort the rest. The first slot that
isn't holding i+1 is the answer. This is the classic "O(n) time, O(1) space" hard
problem, and cyclic sort makes it clean.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. O(n)/O(1) is the optimal bound this problem is famous for.
'''
