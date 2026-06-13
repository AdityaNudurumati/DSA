'''
5. Quick Sort (Medium)
Problem Statement

Sort an integer array in ascending order using Quick Sort with Lomuto partition.

Partition picks a pivot (here the last element) and rearranges the range so every
value <= pivot sits before it and every value > pivot sits after it, returning the
pivot's final index. Quick Sort then recurses on the two sides, in place.

Note: a standalone Lomuto partition / quick-select also lives in
../../1.Arrays/1.two_pointer_problems/3.partition_dutch_flag/.

Example
Input:
nums = [5,2,8,1,9,3]

Output:
[1,2,3,5,8,9]
'''

def partition(nums, low, high):

    pivot = nums[high]
    i = low - 1                 # boundary of the "<= pivot" region

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

    # ranges of size 0 or 1 are already sorted
    if low < high:
        p = partition(nums, low, high)
        quickSort(nums, low, p - 1)
        quickSort(nums, p + 1, high)

    return nums


if __name__ == "__main__":
    print(quickSort([5, 2, 8, 1, 9, 3]))  # Expected: [1, 2, 3, 5, 8, 9]
    print(quickSort([]))                   # Expected: []
    print(quickSort([1]))                  # Expected: [1]
    print(quickSort([3, 3, 1]))            # Expected: [1, 3, 3]

'''
Pattern
Quick Sort — partition around a pivot (Lomuto), recurse on each side.
Each partition is O(n) and places the pivot at its final index; balanced splits
give log n depth -> O(n log n). A sorted input with last-element pivot degenerates
to O(n^2). Partition swaps non-adjacent elements, so it is unstable.

| Metric | Value                              |
| ------ | ---------------------------------- |
| Time   | O(n log n) average, O(n^2) worst   |
| Space  | O(log n) recursion (average)       |
| Stable | No                                 |

Better Possible?
Randomized or median-of-three pivots make the O(n^2) case astronomically unlikely.
Merge sort guarantees O(n log n) but needs O(n) space; heap sort is in-place and
worst-case O(n log n) but has poorer cache behavior.
'''
