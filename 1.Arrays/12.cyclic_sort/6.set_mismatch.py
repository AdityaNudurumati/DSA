'''
6. Set Mismatch (Easy)   [LC645]
Problem Statement

You have a set that should contain 1..n, but one number got DUPLICATED (replacing
a missing one). Given the array nums, return [duplicated, missing]. O(n) time,
O(1) extra space.

Cyclic-sort each value to index v-1. The one index i with nums[i] != i+1 holds the
duplicated value, and the number that should be there (i+1) is the missing one.

Example
Input:
nums = [1, 2, 2, 4]

Output:
[2, 3]
'''

def findErrorNums(nums):

    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for idx in range(n):
        if nums[idx] != idx + 1:
            return [nums[idx], idx + 1]      # [duplicated, missing]
    return [-1, -1]


if __name__ == "__main__":
    print(findErrorNums([1, 2, 2, 4]))   # Expected: [2, 3]
    print(findErrorNums([1, 1]))          # Expected: [1, 2]
    print(findErrorNums([2, 2]))          # Expected: [2, 1]

'''
Pattern
✅ Cyclic Sort (one duplicate replaces one missing)

Key Observation
Exactly one slot ends up wrong: it holds the duplicated value, while its expected
value (index+1) is the missing one. One pass over the sorted array yields both.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. O(n)/O(1); sum/XOR math is an alternative with the same bounds.
'''
