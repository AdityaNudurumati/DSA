'''
2. Quick Sort Partition (Medium)
Problem Statement

Implement Quick Sort using the Lomuto partition scheme.

Partition picks a pivot (here, the last element) and rearranges the range so that
all values <= pivot come before it and all values > pivot come after it, then
returns the pivot's final index. Quick Sort recurses on the two sides.

Example
Input:
nums = [9,3,7,1,8,2,5]

Output:
[1,2,3,5,7,8,9]
'''

def partition(nums, low, high):

    pivot = nums[high]
    i = low - 1            # boundary of the "<= pivot" region

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    # place pivot just after the "<= pivot" region
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quickSort(nums, low=0, high=None):

    if high is None:
        high = len(nums) - 1

    if low < high:
        p = partition(nums, low, high)
        quickSort(nums, low, p - 1)
        quickSort(nums, p + 1, high)

    return nums


if __name__ == "__main__":
    print(quickSort([9, 3, 7, 1, 8, 2, 5]))  # Expected: [1, 2, 3, 5, 7, 8, 9]

'''
Pattern
✅ Partition (Lomuto) + Divide & Conquer

| Metric | Value                              |
| ------ | ---------------------------------- |
| Time   | O(n log n) average, O(n²) worst    |
| Space  | O(log n) recursion (average)       |

Better Possible?
Worst case avoided with a randomized / median-of-three pivot.
Merge sort gives guaranteed O(n log n) but needs O(n) space.
'''
