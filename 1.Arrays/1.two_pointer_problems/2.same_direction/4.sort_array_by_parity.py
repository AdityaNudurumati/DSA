'''
4. Sort Array By Parity (Easy)
Problem Statement

Given an integer array nums, move all the even integers to the front and all the
odd integers to the back. Any order within each group is acceptable. Do it in-place.

Example
Input:
nums = [3,1,2,4]

Output:
[2,4,3,1]   (any arrangement with evens first is valid)
'''

def sortArrayByParity(nums):

    slow = 0   # next position to place an even number

    for fast in range(len(nums)):

        if nums[fast] % 2 == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums


if __name__ == "__main__":
    print(sortArrayByParity([3, 1, 2, 4]))  # Expected: evens first, e.g. [2, 4, 3, 1]

'''
Pattern
✅ Slow / Fast Pointer (partition by parity)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Single pass is optimal.
'''
