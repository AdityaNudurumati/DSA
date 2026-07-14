'''
2. Missing Number (Easy)   [LC268]
Problem Statement

Given an array nums containing n DISTINCT numbers from the range 0..n (so exactly
one number in 0..n is missing), return the missing number. O(n) time, O(1) space.

Cyclic-sort variant: here the range is 0..n, so value v belongs at index v.
After sorting, the first index i whose value != i is the missing number; if all
match, the missing one is n.

Example
Input:
nums = [3, 0, 1]

Output:
2
'''

def missingNumber(nums):

    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i]                       # value v -> index v (range 0..n)
        if nums[i] < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1                               # n (out of range) or in place

    for idx in range(n):
        if nums[idx] != idx:
            return idx
    return n                                     # 0..n-1 all present -> n missing


if __name__ == "__main__":
    print(missingNumber([3, 0, 1]))                       # Expected: 2
    print(missingNumber([0, 1]))                          # Expected: 2
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))     # Expected: 8

'''
Pattern
✅ Cyclic Sort (range 0..n)

Key Observation
Range 0..n means value v maps to index v. The one value that can't be placed
(n, which has no index n) leaves exactly one slot mismatched -> that index is the
answer. (XOR and sum-formula solutions also work; cyclic sort generalizes to the
"find all missing / duplicates" family.)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
✅ Same O(n)/O(1) via XOR or n*(n+1)/2 - sum; those avoid mutating the array.
'''
