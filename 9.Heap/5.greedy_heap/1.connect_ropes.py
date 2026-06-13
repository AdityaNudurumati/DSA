"""
1. Minimum Cost to Connect Ropes (Easy)

Problem Statement:
You are given an array of rope lengths. Connecting two ropes of lengths a and b
costs a + b, and produces a single rope of length a + b. Repeatedly connect ropes
until only one rope remains. Return the minimum total cost.

Greedy idea: always connect the two SHORTEST ropes first, because longer ropes get
added into the running cost on every subsequent merge, so we want to delay touching
them. A min-heap hands us the two smallest in O(log n).

Example:
    Input:  [4, 3, 2, 6]
    Output: 29
    Input:  [1, 2, 3, 4, 5]
    Output: 33
    Input:  [5]
    Output: 0   (single rope, nothing to connect)
"""

import heapq


def connect_ropes(lengths):
    if len(lengths) <= 1:          # 0 or 1 rope -> no merges needed
        return 0

    heap = list(lengths)           # copy so caller's list is untouched
    heapq.heapify(heap)            # O(n) build min-heap

    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)    # two smallest currently available
        b = heapq.heappop(heap)
        cost = a + b
        total += cost              # pay to merge them
        heapq.heappush(heap, cost) # merged rope re-enters the pool

    return total


if __name__ == "__main__":
    print(connect_ropes([4, 3, 2, 6]))     # Expected: 29
    print(connect_ropes([1, 2, 3, 4, 5]))  # Expected: 33
    print(connect_ropes([5]))              # Expected: 0


"""
Pattern: Greedy + Heap (Huffman-style merging)
    Each step makes the locally optimal choice (merge the two smallest), and a
    min-heap supplies that choice cheaply. The exchange argument proves this is
    globally optimal: any rope merged early is summed into the cost at every later
    merge, so keeping large ropes out of early merges minimizes their multiplier.

| Metric | Value      |
|--------|------------|
| Time   | O(n log n) |  n-1 merges, each O(log n)
| Space  | O(n)       |  the heap

Better Possible?
    No. The output depends on every element, so Omega(n) is a floor, and the
    repeated extract-min inherently costs O(n log n) here. If the inputs were
    already given in sorted order, a two-queue merge can achieve O(n).
"""
