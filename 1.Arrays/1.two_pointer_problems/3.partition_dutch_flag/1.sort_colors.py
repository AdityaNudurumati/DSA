'''
1. Sort Colors (Medium)
Problem Statement

Given an array nums with n objects colored red, white, or blue, represented by the
integers 0, 1, and 2, sort them in-place so equal colors are adjacent and ordered
0 -> 1 -> 2. Do it in one pass without a counting/library sort.

Example
Input:
nums = [2,0,2,1,1,0]

Output:
[0,0,1,1,2,2]
'''

def sortColors(nums):

    low = 0                  # boundary: everything before low is 0
    mid = 0                  # current element under inspection
    high = len(nums) - 1     # boundary: everything after high is 2

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # don't advance mid: the swapped-in value is unexamined

    return nums


if __name__ == "__main__":
    print(sortColors([2, 0, 2, 1, 1, 0]))  # Expected: [0, 0, 1, 1, 2, 2]

'''
Pattern
✅ Dutch National Flag (3-way partition)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Single pass, in-place — optimal.
'''
