'''
5. Segregate Even and Odd (Easy)
Problem Statement

Given an integer array nums, rearrange it in-place so that all even numbers come
before all odd numbers. Order within each group need not be preserved.

Example
Input:
nums = [12,34,45,9,8,90,3]

Output:
[12,34,8,90,45,9,3]   (any arrangement with evens first is valid)
'''

def segregateEvenOdd(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        if nums[left] % 2 == 0:          # even already on correct side
            left += 1
        elif nums[right] % 2 == 1:       # odd already on correct side
            right -= 1
        else:                            # nums[left] odd, nums[right] even -> swap
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


if __name__ == "__main__":
    print(segregateEvenOdd([12, 34, 45, 9, 8, 90, 3]))
    # Expected: evens first, odds after

'''
Pattern
✅ Opposite-Ends Partition (two pointers)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Single pass, in-place.
'''
