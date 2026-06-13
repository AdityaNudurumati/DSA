'''
6. 4Sum (Medium)
Problem Statement

Given an integer array nums and an integer target, return all unique quadruplets
[a, b, c, d] such that:

a + b + c + d = target

The solution must not contain duplicate quadruplets.

Example
Input:
nums = [1,0,-1,0,-2,2]
target = 0

Output:
[[-2,-1,1,2],
 [-2,0,0,2],
 [-1,0,0,1]]
'''

def fourSum(nums, target):

    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):

        # skip duplicate first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):

            # skip duplicate second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:

                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

    return result


if __name__ == "__main__":
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
    # Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

'''
Pattern
✅ Sorting + Two Pointers (two fixed indices + opposite-ends inner loop)

| Metric | Value                   |
| ------ | ----------------------- |
| Time   | O(n³)                   |
| Space  | O(1) (excluding output) |

Better Possible?
❌ No known better than O(n³) for the general k-Sum with k = 4.
Generalizes to kSum recursively.
'''
