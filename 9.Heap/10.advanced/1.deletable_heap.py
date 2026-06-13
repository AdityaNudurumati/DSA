"""
1. Deletable Heap (Medium)

Problem Statement:
Design a min-heap that, in addition to the usual push() and pop(), supports
remove(x): deleting an ARBITRARY element x from the heap. A standard binary
heap only gives cheap access to the minimum, so removing an interior element
is awkward. Implement it with LAZY DELETION: record how many copies of each
value are pending removal, and physically discard a stale entry only when it
bubbles up to the top of the heap.

Example:
    Input:
        push 5, push 1, push 3, push 2
        remove(1)
        pop() , pop() , pop()
    Output:
        2, 3, 5            # 1 was lazily removed and is never returned
"""

import heapq
from collections import defaultdict


class DeletableHeap:
    def __init__(self):
        self._heap = []                  # the actual min-heap (may hold stale entries)
        self._pending = defaultdict(int)  # value -> count of deletions awaiting prune
        self._size = 0                   # number of logically-live elements

    def _prune(self):
        # Drop stale tops: any value at the root that has a pending deletion.
        while self._heap and self._pending[self._heap[0]] > 0:
            self._pending[self._heap[0]] -= 1
            heapq.heappop(self._heap)

    def push(self, x):
        heapq.heappush(self._heap, x)
        self._size += 1

    def remove(self, x):
        # Lazy: just mark one copy of x as deleted. Physical removal is deferred.
        self._pending[x] += 1
        self._size -= 1

    def pop(self):
        # Ensure the true minimum is exposed, then pop it.
        self._prune()
        if not self._heap:
            raise IndexError("pop from empty DeletableHeap")
        self._size -= 1
        return heapq.heappop(self._heap)

    def peek(self):
        self._prune()
        if not self._heap:
            raise IndexError("peek from empty DeletableHeap")
        return self._heap[0]

    def __len__(self):
        return self._size


if __name__ == "__main__":
    h = DeletableHeap()
    for v in (5, 1, 3, 2):
        h.push(v)
    h.remove(1)                 # 1 marked for lazy deletion
    print(h.pop())              # Expected: 2
    print(h.pop())              # Expected: 3
    print(h.pop())              # Expected: 5
    print(len(h))               # Expected: 0


"""
Pattern: Lazy Deletion on a binary heap.
Technique & why: A binary heap supports O(log n) push/pop of the extreme element
but has no fast handle on interior elements. Instead of paying O(n) to find and
sift-down an arbitrary value, we keep a 'pending deletions' multiset (value ->
count). remove(x) just increments that count in O(1). The stale entry stays
physically in the array but is skipped the moment it reaches the root: before any
pop/peek we _prune(), popping roots whose pending count is positive. This keeps
the amortized cost logarithmic because each element is pushed and physically
popped at most once.

| Metric          | Value     | Time      | Space |
|-----------------|-----------|-----------|-------|
| push            | O(log n)  | O(log n)  | O(1)  |
| remove(x) lazy  | O(1)      | O(1)      | O(1)  |
| pop / peek      | amortized | O(log n)* | O(1)  |
| total space     |           |           | O(n)  |

*Each prune step pops one stale entry; since every pushed element is pruned or
popped at most once, the total pruning work is amortized O(log n) per operation.

Better Possible?
For O(log n) WORST-CASE arbitrary deletion (not just amortized) use an INDEXED
heap: maintain a dict value->array-index and sift the removed slot up/down in
place. That removes the lazy-stale overhead but costs extra bookkeeping and only
matters when many deletions are interleaved or memory from stale entries is a
concern. For this push/remove/pop workload, lazy deletion is simpler and optimal.
"""
