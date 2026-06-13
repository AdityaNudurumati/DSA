"""
2. Huffman Encoding (Medium)

Problem Statement:
Given symbols with their frequencies, build an optimal prefix-free (Huffman) code by
repeatedly merging the two least-frequent nodes into a parent whose weight is their
sum. Return the total weighted code length = sum(freq * depth), which equals the sum
of all internal-node weights produced during merging.

Greedy idea: the two rarest symbols should sit deepest in the tree, so merge the two
smallest weights each step. A min-heap delivers them in O(log n).

Example:
    Input:  freqs = [5, 9, 12, 13, 16, 45]
    Output: 224
    Input:  freqs = [10, 20, 30]
    Output: 90
"""

import heapq


def huffman_total_length(freqs):
    if len(freqs) <= 1:            # single symbol -> 1-bit code -> depth 0 sum is 0
        return 0

    heap = list(freqs)            # leaf weights
    heapq.heapify(heap)

    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)   # two smallest weights
        b = heapq.heappop(heap)
        merged = a + b            # internal node weight
        total += merged           # each internal weight = bits contributed at that level
        heapq.heappush(heap, merged)

    return total


def huffman_code_lengths(freqs):
    """Return {freq: code_length} so we can print each symbol's code length."""
    if len(freqs) <= 1:
        return {f: 1 for f in freqs}

    # Each heap entry: (weight, set_of_original_freqs_under_this_node)
    heap = [(f, (i,)) for i, f in enumerate(freqs)]
    heapq.heapify(heap)
    depth = {i: 0 for i in range(len(freqs))}  # code length per symbol index

    while len(heap) > 1:
        wa, ia = heapq.heappop(heap)
        wb, ib = heapq.heappop(heap)
        for i in ia + ib:                       # everyone below gains one bit
            depth[i] += 1
        heapq.heappush(heap, (wa + wb, ia + ib))

    return {freqs[i]: depth[i] for i in range(len(freqs))}


if __name__ == "__main__":
    print(huffman_total_length([5, 9, 12, 13, 16, 45]))  # Expected: 224
    print(huffman_total_length([10, 20, 30]))            # Expected: 90

    # Per-symbol code lengths (multiset-friendly print)
    lengths = huffman_code_lengths([5, 9, 12, 13, 16, 45])
    print(sorted(lengths.items()))  # Expected: [(5, 4), (9, 4), (12, 3), (13, 3), (16, 3), (45, 1)]


"""
Pattern: Greedy + Heap (Huffman coding)
    Optimal prefix code via repeated merge of the two smallest weights. The min-heap
    is what makes "two smallest" cheap. Summing every internal-node weight gives the
    total weighted depth without explicitly walking the tree, because a symbol's
    frequency is re-added once per ancestor it passes under.

| Metric | Value      |
|--------|------------|
| Time   | O(n log n) |  n-1 merges, each O(log n)
| Space  | O(n)       |  heap (+ index sets for code lengths)

Better Possible?
    O(n log n) is optimal for unsorted input. If frequencies arrive pre-sorted, a
    two-queue technique builds the tree in O(n). Tracking per-symbol code lengths via
    index sets costs extra O(n) per merge in the worst case; a parent-pointer tree
    avoids that if only lengths (not the running total) are wanted.
"""
