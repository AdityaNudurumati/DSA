'''
4. Partition Around Pivot (Medium)
Problem Statement

Given an array nums and a pivot value, rearrange it in-place so that:
- all elements LESS than pivot come first,
- then all elements EQUAL to pivot,
- then all elements GREATER than pivot.

Relative order within groups need not be preserved.

Example
Input:
nums = [9,12,3,5,14,10,10], pivot = 10

Output:
[9,3,5,10,10,12,14]   (any arrangement with <10 | ==10 | >10 is valid)
'''

def partitionAroundPivot(nums, pivot):

    low = 0                  # boundary of the "< pivot" region
    mid = 0
    high = len(nums) - 1     # boundary of the "> pivot" region

    while mid <= high:

        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] > pivot:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

        else:  # equal to pivot
            mid += 1

    return nums


if __name__ == "__main__":
    print(partitionAroundPivot([9, 12, 3, 5, 14, 10, 10], 10))
    # Expected: values <10 first, then 10s, then >10  e.g. [9, 3, 5, 10, 10, 14, 12]

'''
Pattern
✅ Dutch National Flag generalized to an arbitrary pivot value

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Single in-place pass.
'''
