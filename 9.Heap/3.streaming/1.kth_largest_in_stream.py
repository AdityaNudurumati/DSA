'''
703. Kth Largest Element in a Stream (Easy)
Problem Statement

Design a class to find the k-th largest element in a stream. Note that it is
the k-th largest element in sorted order, not the k-th distinct element.

Implement KthLargest(k, nums) with the initial stream nums, and a method
add(val) that appends val to the stream and returns the k-th largest element.

Example
Input:
k = 3, nums = [4, 5, 8, 2]
add(3) -> 4
add(5) -> 5
add(10) -> 5
add(9) -> 8
add(4) -> 8

Output:
4
5
5
8
8
'''

import heapq

class KthLargest:
    def __init__(self, k, nums):
        # keep a size-k MIN-heap of the k largest values seen so far;
        # its root (heap[0]) is therefore the k-th largest element.
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        # trim down to exactly k elements (drop the smallest extras)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)   # evict the smallest, keep top k
        return self.heap[0]            # root = k-th largest


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))    # Expected: 4
    print(kth.add(5))    # Expected: 5
    print(kth.add(10))   # Expected: 5
    print(kth.add(9))    # Expected: 8
    print(kth.add(4))    # Expected: 8

'''
Pattern
✅ Streaming — size-k min-heap maintained incrementally
The root of a min-heap holding the k largest values is the k-th largest; each
add() is one push plus an optional pop, so queries stay cheap as data streams in.

| Metric        | Value      |
| ------------- | ---------- |
| Time per add  | O(log k)   |
| Build (init)  | O(n)       |
| Space         | O(k)       |

Better Possible?
For a single static query Quick Select is O(n) average, but it can't be updated
incrementally. For a continuous stream the size-k heap is the natural choice.
'''
