'''
7. 3Sum (Medium)
Problem Statement

Given an integer array nums, return all unique triplets:
[a, b, c]
such that:

a + b + c = 0
The solution must not contain duplicate triplets.

Example
Input:
nums = [-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],
 [-1,0,1]]
'''

def threeSum(nums):

    nums.sort()

    result = []

    n = len(nums)

    for i in range(n - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total == 0:

                result.append(
                    [nums[i], nums[left], nums[right]]
                )

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1, -1, 2], [-1, 0, 1]]

'''
Pattern
✅ Sorting + Two Pointers

| Metric | Value                   |
| ------ | ----------------------- |
| Time   | O(n²)                   |
| Space  | O(1) (excluding output) |

Better?
For general 3Sum:
❌ No known better algorithm than O(n²).

This is considered optimal.
'''