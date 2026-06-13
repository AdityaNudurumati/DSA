'''
2. Remove Duplicates from Sorted Array (Easy)
Problem Statement

Given a sorted integer array nums, remove the duplicates in-place such that each unique element appears only once.

Return the number of unique elements k.

The first k elements of the array should contain the unique values.
Input:
nums = [1,1,2]

Output:
k = 2

nums becomes:
[1,2,_]
Input:
nums = [0,0,1,1,1,2,2,3,3,4]

Output:
k = 5

nums becomes:
[0,1,2,3,4,_,_,_,_,_]

'''

def removeDuplicates(nums):

    slow = 1

    for fast in range(1, len(nums)):

        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicates(nums)
    print(k)            # Expected: 5
    print(nums[:k])     # Expected: [0, 1, 2, 3, 4]

'''
Best Pattern
✅ Slow / Fast Pointer
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No

Need to visit every element.
Optimal.
'''