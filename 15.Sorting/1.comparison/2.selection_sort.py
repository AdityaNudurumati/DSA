'''
2. Selection Sort (Easy)
Problem Statement

Sort an integer array in ascending order using Selection Sort.

Repeatedly select the minimum of the unsorted suffix and swap it into the next
position of the sorted prefix. After i passes the first i elements are final.

Example
Input:
nums = [5,2,8,1,9,3]

Output:
[1,2,3,5,8,9]
'''

def selectionSort(nums):

    n = len(nums)

    for i in range(n - 1):
        # find index of the minimum in nums[i..n-1]
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # swap it into the sorted-prefix boundary
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == "__main__":
    print(selectionSort([5, 2, 8, 1, 9, 3]))  # Expected: [1, 2, 3, 5, 8, 9]
    print(selectionSort([]))                   # Expected: []
    print(selectionSort([1]))                  # Expected: [1]
    print(selectionSort([3, 3, 1]))            # Expected: [1, 3, 3]

'''
Pattern
Selection Sort — pick the minimum each pass, place it at the front.
Always does ~n^2/2 comparisons regardless of input order, but at most n-1 swaps,
so it is useful when writes are far more expensive than reads. Unstable: a
long-range swap can jump an equal element past its peer.

| Metric | Value                       |
| ------ | --------------------------- |
| Time   | O(n^2) (all cases)          |
| Space  | O(1) in-place               |
| Stable | No                          |

Better Possible?
O(n log n) via merge/heap/quick sort. Selection sort's only edge is minimizing
the number of swaps (exactly n-1 in the worst case).
'''
