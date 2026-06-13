"""
973. K Closest Points to Origin (Medium)

Problem Statement
-----------------
Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance.
You may return the answer in any order.

Example
-------
Input:  points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Input:  points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]   (any order; sorted here for a deterministic print)
"""

import heapq


def k_closest(points, k):
    # Size-k MAX-heap keyed by squared distance (negate to simulate max-heap).
    # Skip sqrt: comparing squared distances preserves ordering.
    heap = []  # entries: (-dist_sq, x, y)
    for x, y in points:
        dist_sq = x * x + y * y
        heapq.heappush(heap, (-dist_sq, x, y))
        if len(heap) > k:
            heapq.heappop(heap)  # drop the farthest of the current k+1
    # Whatever remains are the k closest points.
    return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    # sort outputs because order is not guaranteed
    print(sorted(k_closest([[1, 3], [-2, 2]], 1)))            # Expected: [[-2, 2]]
    print(sorted(k_closest([[3, 3], [5, -1], [-2, 4]], 2)))   # Expected: [[-2, 4], [3, 3]]


"""
Pattern
-------
Top-K (K Closest). Maintain a size-k MAX-heap keyed by distance: push every
point, and once the heap exceeds k, pop the largest (farthest) element. After
the scan the heap holds exactly the k smallest distances. We negate the
squared distance because Python's heapq is a min-heap, and we avoid sqrt since
monotonic transforms do not change the ranking.

| Metric | Value      |
|--------|------------|
| Time   | O(n log k) |
| Space  | O(k)       |

Better Possible?
----------------
Quickselect (Hoare partition on distance) gives expected O(n) time and O(1)
extra space, at the cost of worst-case O(n^2) and an unsorted result. The
size-k heap is preferred for streaming input or when k << n, since it bounds
memory to O(k) and handles points arriving one at a time.
"""
