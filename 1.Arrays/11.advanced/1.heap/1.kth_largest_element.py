'''
1. Kth Largest Element in an Array (Medium) — heap approach
Problem Statement

Given an integer array nums and an integer k, return the k-th largest element.

(A Quick Select O(n)-average version lives in
 ../../1.two_pointer_problems/3.partition_dutch_flag/3.quick_select.py.
 This file shows the heap approach, which streams naturally and is easy to reason about.)

Example
Input:
nums = [3,2,1,5,6,4], k = 2

Output:
5
'''

import heapq

def findKthLargest(nums, k):

    # keep a min-heap of the k largest seen so far; its root is the k-th largest
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # drop the smallest, keep top k

    return heap[0]


if __name__ == "__main__":
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))              # Expected: 5
    print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))     # Expected: 4

'''
Pattern
✅ Min-heap of size k

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log k) |
| Space  | O(k)       |

Better Possible?
Quick Select is O(n) average (O(n²) worst). Heap wins when k is small or data streams.
'''
