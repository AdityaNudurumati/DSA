'''
3. Find All Numbers Disappeared in an Array (Easy)   [LC448]
Problem Statement

Given an array nums of n integers where nums[i] is in the range 1..n, some numbers
appear twice and others are missing. Return ALL the numbers in 1..n that do NOT
appear. O(n) time, O(1) extra space (the output list doesn't count).

Cyclic-sort each value to index v-1. Any index i whose value != i+1 is a missing
number (i+1).

Example
Input:
nums = [4, 3, 2, 7, 8, 2, 3, 1]

Output:
[5, 6]
'''

def findDisappearedNumbers(nums):

    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i] - 1                    # value v -> index v-1
        if nums[i] != nums[correct]:             # duplicates make this stop
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    return [idx + 1 for idx in range(n) if nums[idx] != idx + 1]


if __name__ == "__main__":
    print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))   # Expected: [5, 6]
    print(findDisappearedNumbers([1, 1]))                      # Expected: [2]
    print(findDisappearedNumbers([1, 2, 3, 4]))                # Expected: []

'''
Pattern
✅ Cyclic Sort (range 1..n, duplicates allowed)

Key Observation
After cyclic sort, correct slots hold i+1. Duplicates block their true slot, so
the slots meant for missing numbers stay wrong -> those indices reveal what's gone.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. (The negation-marking trick is the same O(n)/O(1); cyclic sort is clearer.)
'''
