'''
480. Sliding Window Median (Hard)
Problem Statement

Given an integer array nums and a window size k, the window slides from the left
to the right one position at a time. Return the median of each window.
The median is the middle value of an ordered window (for even k, the average of
the two middle values).

Example
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]

Input:  nums = [1,2,3,4], k = 2
Output: [1.5,2.5,3.5]
'''

import heapq


def medianSlidingWindow(nums, k):
    small = []  # max-heap (negated) holding the lower half
    large = []  # min-heap holding the upper half
    # lazy-deletion bookkeeping: value -> count of elements scheduled to be removed
    to_remove = {}
    res = []

    def prune(heap):
        # drop stale roots that have already slid out of the window
        # max-heap stores negatives, so map back with the sign factor
        sign = -1 if heap is small else 1
        while heap and (sign * heap[0]) in to_remove and to_remove[sign * heap[0]] > 0:
            val = sign * heap[0]
            to_remove[val] -= 1
            heapq.heappop(heap)

    def balance():
        # keep small the same size as large or exactly one larger
        # use effective sizes (raw size minus pending deletions tracked via counters)
        if small_size[0] > large_size[0] + 1:
            heapq.heappush(large, -heapq.heappop(small))
            small_size[0] -= 1
            large_size[0] += 1
            prune(small)
        elif small_size[0] < large_size[0]:
            heapq.heappush(small, -heapq.heappop(large))
            large_size[0] -= 1
            small_size[0] += 1
            prune(large)

    # track logical sizes (valid, non-stale element counts) of each heap
    small_size = [0]
    large_size = [0]

    def add(num):
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
            small_size[0] += 1
        else:
            heapq.heappush(large, num)
            large_size[0] += 1
        balance()

    def remove(num):
        # schedule a lazy deletion and adjust the logical size of its heap
        to_remove[num] = to_remove.get(num, 0) + 1
        if small and num <= -small[0]:
            small_size[0] -= 1
            if num == -small[0]:
                prune(small)
        else:
            large_size[0] -= 1
            if large and num == large[0]:
                prune(large)
        balance()

    def median():
        if k % 2 == 1:
            return float(-small[0])
        return (-small[0] + large[0]) / 2.0

    for i, num in enumerate(nums):
        add(num)
        if i >= k - 1:
            res.append(median())
            remove(nums[i - k + 1])

    return res


if __name__ == "__main__":
    print(medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # Expected: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    print(medianSlidingWindow([1, 2, 3, 4], 2))
    # Expected: [1.5, 2.5, 3.5]

'''
Pattern
✅ Dual Heap (max-heap lower half + min-heap upper half) with Lazy Deletion

Key Observation
The median of a window comes from the heap roots, but a sliding window must also
*remove* the element leaving on the left — and arbitrary deletion is not a heap
operation. The trick is lazy deletion: schedule the outgoing value in a to_remove
map, adjust each heap's *logical* size immediately, and only physically pop a stale
value once it surfaces at a root. Balancing uses the logical sizes so the roots
always straddle the true median.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log k) |
| Space  | O(k)       |

Better Possible?
A balanced BST / order-statistics tree (or a SortedList) also gives O(n log k) but
with simpler deletion. For the heap-only approach, O(n log k) is the practical bound.
'''
