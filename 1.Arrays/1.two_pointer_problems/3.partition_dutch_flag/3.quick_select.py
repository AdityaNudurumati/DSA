'''
3. Quick Select — Kth Largest Element (Medium)
Problem Statement

Given an integer array nums and an integer k, return the k-th largest element.
It is the k-th largest in sorted order, not the k-th distinct element.

Use Quick Select (partition-based) for average O(n) instead of sorting.

Example
Input:
nums = [3,2,1,5,6,4], k = 2

Output:
5
'''

def partition(nums, low, high):

    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def findKthLargest(nums, k):

    # k-th largest = the element at sorted index (n - k)
    target = len(nums) - k

    low = 0
    high = len(nums) - 1

    while low <= high:

        p = partition(nums, low, high)

        if p == target:
            return nums[p]
        elif p < target:
            low = p + 1
        else:
            high = p - 1


if __name__ == "__main__":
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))            # Expected: 5
    print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))   # Expected: 4

'''
Pattern
✅ Partition + Selection (only recurse into the side that contains the answer)

| Metric | Value                            |
| ------ | -------------------------------- |
| Time   | O(n) average, O(n²) worst        |
| Space  | O(1) (iterative)                 |

Better Possible?
A heap gives O(n log k). Median-of-medians guarantees O(n) worst case but has a
large constant; randomized pivot is the practical choice.
'''
