'''
1. Bubble Sort (Easy)
Problem Statement

Sort an integer array in ascending order using Bubble Sort.

Repeatedly walk the array swapping adjacent out-of-order pairs. After pass k the
largest k elements have "bubbled" to the end. Track whether any swap happened in a
pass; if none did, the array is already sorted and we can stop early.

Example
Input:
nums = [5,2,8,1,9,3]

Output:
[1,2,3,5,8,9]
'''

def bubbleSort(nums):

    n = len(nums)

    # each pass fixes the largest remaining element at position n-1-i
    for i in range(n - 1):
        swapped = False
        # last i elements are already in place, so stop at n-1-i
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        # no swaps in a full pass => already sorted, early exit
        if not swapped:
            break

    return nums


if __name__ == "__main__":
    print(bubbleSort([5, 2, 8, 1, 9, 3]))  # Expected: [1, 2, 3, 5, 8, 9]
    print(bubbleSort([]))                   # Expected: []
    print(bubbleSort([1]))                  # Expected: [1]
    print(bubbleSort([3, 3, 1]))            # Expected: [1, 3, 3]

'''
Pattern
Bubble Sort — adjacent swaps, with early-exit flag.
Each pass pushes the next-largest value to its final slot; the swapped flag turns
an already-sorted input into a single O(n) pass. Stable (only swaps on strict >).

| Metric | Value                                  |
| ------ | -------------------------------------- |
| Time   | O(n^2) worst/avg, O(n) best (sorted)   |
| Space  | O(1) in-place                          |
| Stable | Yes                                    |

Better Possible?
For random data merge/heap/quick sort give O(n log n). Bubble sort is only
competitive when the array is tiny or nearly sorted (early exit -> O(n)).
'''
