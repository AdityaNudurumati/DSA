'''
5. Move Zeroes (Easy)
Problem Statement

Given an integer array nums, move all 0s to the end while maintaining the relative order of non-zero elements.

Do this in-place.

Example
Input:
nums = [0,1,0,3,12]

Output:
[1,3,12,0,0]
'''

def moveZeroes(nums):

    slow = 0

    for fast in range(len(nums)):

        if nums[fast] != 0:

            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)  # Expected: [1, 3, 12, 0, 0]

'''
Pattern
✅ Slow / Fast Pointer

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better?
❌ No

Optimal.
'''