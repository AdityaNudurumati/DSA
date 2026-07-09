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

Time Complexity: O(n)

Why?

The fast pointer visits each element exactly once.

for fast in range(1, len(nums))

If there are n elements:

fast runs from 1 to n-1
Total iterations = n-1

Each iteration performs only constant-time operations:

nums[fast] != nums[fast - 1]   # O(1)
nums[slow] = nums[fast]        # O(1)
slow += 1                      # O(1)

So:

O(1) + O(1) + ... (n times)
= O(n)
Example
nums = [0,0,1,1,1,2,2,3,3,4]

10 elements → roughly 10 checks.

If there were:

100 elements  → 100 checks
1000 elements → 1000 checks
10000 elements → 10000 checks

The work grows linearly.

✅ Time Complexity = O(n)

Space Complexity: O(1)

Are we creating another list?

❌ No

Are we using a dictionary?

❌ No

Are we using a set?

❌ No

We only use a few variables:

slow
fast

Whether the array has:

10 elements
1000 elements
1,000,000 elements

we still use the same amount of extra memory.

So:

Extra Space = O(1)

This is called in-place modification because we're changing the original array instead of creating a new one.

Summary
Complexity	Value
Time	O(n)
Space	O(1)
Why is it optimal?

To know whether an element is a duplicate, you must look at every element at least once.

So:

Better than O(n) time? ❌ Impossible
Better than O(1) space? ❌ Impossible (constant space is already the minimum)

Therefore this solution is optimal. ✅
'''