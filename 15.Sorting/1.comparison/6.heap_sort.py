'''
6. Heap Sort (Medium)
Problem Statement

Sort an integer array in ascending order using Heap Sort, in place.

Build a max-heap over the whole array so the largest element is at the root
(index 0). Repeatedly swap the root with the last unsorted slot, shrink the heap by
one, and sift the new root down to restore the heap property. The sorted suffix
grows from the back to the front.

Example
Input:
nums = [5,2,8,1,9,3]

Output:
[1,2,3,5,8,9]
'''

def heapify(nums, n, i):
    # sift nums[i] down within the heap of size n
    largest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)   # recurse on the affected subtree


def heapSort(nums):

    n = len(nums)

    # build a max-heap bottom-up from the last parent down to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # repeatedly move the max (root) to the end, then re-heapify the rest
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        heapify(nums, end, 0)

    return nums


if __name__ == "__main__":
    print(heapSort([5, 2, 8, 1, 9, 3]))  # Expected: [1, 2, 3, 5, 8, 9]
    print(heapSort([]))                   # Expected: []
    print(heapSort([1]))                  # Expected: [1]
    print(heapSort([3, 3, 1]))            # Expected: [1, 3, 3]

'''
Pattern
Heap Sort — build a max-heap, then extract the max repeatedly.
Building the heap is O(n); each of the n-1 extractions does an O(log n) sift-down,
giving O(n log n) overall with O(1) extra space. Swapping the root to the back
reorders equal elements arbitrarily, so it is unstable.

| Metric | Value                |
| ------ | -------------------- |
| Time   | O(n log n) all cases |
| Space  | O(1) in-place        |
| Stable | No                   |

Better Possible?
Time is optimal for comparison sorts. Heap sort uniquely combines guaranteed
O(n log n) with O(1) space, but its scattered memory access makes quick sort
usually faster in practice; merge sort is the choice when stability is required.
'''
