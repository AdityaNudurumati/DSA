'''
1. External Sort via K-Way Merge (Hard)
Problem Statement

Sort a dataset that is too large to fit entirely in memory. The classic
"external sort" approach:
  1) Split the input into chunks small enough to fit in memory.
  2) Sort each chunk in memory and write it out as a sorted "run".
  3) K-way merge all the sorted runs into one fully sorted output, reading
     only a little from each run at a time (a min-heap picks the next item).

Here we SIMULATE this in memory: chunks stand in for on-disk runs, and
heapq.merge performs the lazy k-way merge that streams from each run.

Example
Input:
data = [9, 3, 7, 1, 8, 2, 6, 4, 5, 0], chunk_size = 3

Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

import heapq

def external_sort(data, chunk_size):

    # Phase 1 — split into chunks and sort each chunk into a "run".
    # Sorting WITHIN a run is fine: a run fits in memory, so an in-memory
    # sort is allowed here (the external part is the merge across runs).
    runs = []
    for i in range(0, len(data), chunk_size):
        run = sorted(data[i:i + chunk_size])   # in-memory sort of one chunk
        runs.append(run)

    # Phase 2 — k-way merge the sorted runs with a min-heap.
    # heapq.merge is a lazy iterator: it only ever holds one item per run,
    # which is exactly how an external merge keeps memory bounded.
    return list(heapq.merge(*runs))


if __name__ == "__main__":
    print(external_sort([9, 3, 7, 1, 8, 2, 6, 4, 5, 0], 3))
    # Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(external_sort([5, 1, 4, 2, 8, 0, 2], 2))
    # Expected: [0, 1, 2, 2, 4, 5, 8]

    print(external_sort([], 3))
    # Expected: []

'''
Pattern
✅ External Sort = sort small runs in memory, then k-way merge (min-heap).

Why a heap merge: with R runs, the heap holds one front element per run, so it
picks the global minimum in O(log R) per emitted element while keeping memory
proportional to the number of runs — not the dataset size. That bounded memory
footprint is the whole point of external sorting.

| Metric | Value                                              |
| ------ | -------------------------------------------------- |
| Time   | O(n log n) total (run sorts + O(n log R) merge)    |
| Space  | O(R) for the merge heap (runs live "on disk")      |
| Stable | Yes — heapq.merge keeps run order for equal keys   |

Better Possible?
O(n log n) is optimal for comparison sorting. The external-sort win is not speed
but MEMORY: it sorts data larger than RAM. Real systems tune chunk_size to RAM
and may do multi-pass merges when the number of runs exceeds open-file limits.
'''
