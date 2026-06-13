'''
6. Squares of a Sorted Array (Easy)
Problem Statement

Given a sorted integer array nums (can contain negative numbers).

Return an array of the squares of each number sorted in non-decreasing order.

Example
Input:
nums = [-4,-1,0,3,10]

Output:
[0,1,9,16,100]
'''

def sortedSquares(nums):

    n = len(nums)

    result = [0] * n

    left = 0
    right = n - 1

    pos = n - 1

    while left <= right:

        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1

        pos -= 1

    return result


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 3, 10]))  # Expected: [0, 1, 9, 16, 100]

'''
Pattern
✅ Two Pointers from Ends

Why?
Largest square can come from:
-10 → 100
10  → 100

Need to compare both ends.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better?
❌ No

Output array itself requires O(n).
'''