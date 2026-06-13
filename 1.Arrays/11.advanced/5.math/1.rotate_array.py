'''
1. Rotate Array (Medium)
Problem Statement

Given an integer array nums, rotate it to the right by k steps, in-place.

Example
Input:
nums = [1,2,3,4,5,6,7], k = 3

Output:
[5,6,7,1,2,3,4]
'''

def rotate(nums, k):

    n = len(nums)
    k %= n                       # rotating by n is a no-op

    # reverse-all, then reverse the two parts -> right rotation by k
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums


if __name__ == "__main__":
    print(rotate([1, 2, 3, 4, 5, 6, 7], 3))   # Expected: [5, 6, 7, 1, 2, 3, 4]
    print(rotate([-1, -100, 3, 99], 2))        # Expected: [3, 99, -1, -100]

'''
Pattern
✅ Three Reversals (math/array trick)

Key Observation
Reversing the whole array then re-reversing the first k and the rest places each
element at (i + k) mod n with no extra array.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
