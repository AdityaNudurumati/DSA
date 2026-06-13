'''
3. Majority Element (Easy) — Divide & Conquer
Problem Statement

Given an array of size n, return the element that appears more than n/2 times.
You may assume the majority element always exists.

Example
Input:
nums = [2,2,1,1,1,2,2]

Output:
2
'''

def majorityElement(nums):

    def rec(lo, hi):
        # base case: a single element is the majority of its own range
        if lo == hi:
            return nums[lo]

        mid = (lo + hi) // 2
        left = rec(lo, mid)
        right = rec(mid + 1, hi)

        if left == right:
            return left

        # whichever candidate dominates this range wins
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
        return left if left_count > right_count else right

    return rec(0, len(nums) - 1)


if __name__ == "__main__":
    print(majorityElement([3, 2, 3]))                 # Expected: 3
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))     # Expected: 2

'''
Pattern
✅ Divide & Conquer (majority of halves)

Key Observation
The overall majority must be the majority of at least one half. Recurse, then verify
the two candidates by counting over the current range.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n log n)     |
| Space  | O(log n)       |

Better Possible?
✅ Yes — Boyer-Moore voting is O(n) time / O(1) space. This file shows the D&C lens.
'''
