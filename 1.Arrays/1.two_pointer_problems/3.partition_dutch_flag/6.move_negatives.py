'''
6. Move Negative Numbers to One Side (Easy)
Problem Statement

Given an integer array nums, rearrange it in-place so that all negative numbers
come before all non-negative numbers. Order within each group need not be preserved.

Example
Input:
nums = [-1,2,-3,4,5,6,-7,8,9]

Output:
[-1,-3,-7,4,5,6,2,8,9]   (any arrangement with negatives first is valid)
'''

def moveNegatives(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        if nums[left] < 0:               # negative already on correct side
            left += 1
        elif nums[right] >= 0:           # non-negative already on correct side
            right -= 1
        else:                            # nums[left] >= 0, nums[right] < 0 -> swap
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


if __name__ == "__main__":
    print(moveNegatives([-1, 2, -3, 4, 5, 6, -7, 8, 9]))
    # Expected: negatives first, non-negatives after

'''
Pattern
✅ Opposite-Ends Partition (two pointers)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Note
This does NOT preserve relative order. Order-preserving versions need O(n) extra
space or a stable-partition (rotation) approach that is O(n²) in the worst case.
'''
