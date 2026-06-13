'''
3. Remove Element (Easy)
Problem Statement

Given an integer array nums and an integer val, remove all occurrences of val
in-place. Return the number of elements k that are not equal to val.

The first k elements of nums should hold the kept values (order can vary).

Example
Input:
nums = [3,2,2,3]
val = 3

Output:
k = 2
nums becomes: [2,2,_,_]
'''

def removeElement(nums, val):

    slow = 0

    for fast in range(len(nums)):

        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    k = removeElement(nums, 3)
    print(k)            # Expected: 2
    print(nums[:k])     # Expected: [2, 2]

'''
Pattern
✅ Slow / Fast Pointer

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Must inspect every element.
'''
