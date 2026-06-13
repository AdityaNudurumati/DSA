'''
3. Insertion Sort (Easy)
Problem Statement

Sort an integer array in ascending order using Insertion Sort.

Grow a sorted prefix one element at a time: take the next element (the "key") and
shift larger prefix elements right until the key lands in its correct slot.

Example
Input:
nums = [5,2,8,1,9,3]

Output:
[1,2,3,5,8,9]
'''

def insertionSort(nums):

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        # shift everything > key one slot right to open a gap
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        # drop key into the gap
        nums[j + 1] = key

    return nums


if __name__ == "__main__":
    print(insertionSort([5, 2, 8, 1, 9, 3]))  # Expected: [1, 2, 3, 5, 8, 9]
    print(insertionSort([]))                   # Expected: []
    print(insertionSort([1]))                  # Expected: [1]
    print(insertionSort([3, 3, 1]))            # Expected: [1, 3, 3]

'''
Pattern
Insertion Sort — insert each element into the already-sorted prefix.
The while-loop stops on the first element <= key (strict >), so equal elements
keep their order: stable. On nearly-sorted data each insert shifts almost nothing,
giving O(n) best case, which makes it a common base case inside quick/merge sort.

| Metric | Value                                  |
| ------ | -------------------------------------- |
| Time   | O(n^2) worst/avg, O(n) best (sorted)   |
| Space  | O(1) in-place                          |
| Stable | Yes                                    |

Better Possible?
O(n log n) for general input. Insertion sort wins for small or nearly-sorted
arrays and is the typical cutoff used by hybrid sorts (e.g. Timsort).
'''
