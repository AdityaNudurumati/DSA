'''
632. Smallest Range Covering Elements from K Lists (Hard)
Problem Statement

You have k lists of sorted integers in non-decreasing order. Find the smallest
range [a, b] that includes at least one number from each of the k lists. The
range [a, b] is smaller than [c, d] if b - a < d - c, or a < c when the widths
are equal.

Example
Input:
lists = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

Output:
[20,24]
'''

import heapq

def smallestRange(lists):
    # heap of current fronts: (value, list index, index within that list)
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists)]
    heapq.heapify(heap)

    cur_max = max(lst[0] for lst in lists)   # max of the current window
    best = [heap[0][0], cur_max]             # candidate range [min, max]

    while True:
        val, i, j = heapq.heappop(heap)      # current minimum of the window
        if cur_max - val < best[1] - best[0]:
            best = [val, cur_max]
        # advance in the list that held the minimum; if exhausted, we are done
        if j + 1 == len(lists[i]):
            return best
        nxt = lists[i][j + 1]
        cur_max = max(cur_max, nxt)
        heapq.heappush(heap, (nxt, i, j + 1))


if __name__ == "__main__":
    print(smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))  # Expected: [20, 24]
    print(smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))                       # Expected: [1, 1]

'''
Pattern
K-Way Merge — keep a min-heap of one front from each list plus a running max.
The window [heap-min, cur_max] always contains one element per list; advancing
the minimum slides this window to find the tightest covering range.

Why: a valid range must span the current min and max across all lists. Shrinking
is only possible by raising the smallest value, so we pop the min and pull its
list's next element, updating cur_max. We stop the moment any list is exhausted,
since no further window can cover that list.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(N log k)    | (N = total elements)
| Space  | O(k)          |

Better Possible?
❌ No. Every element may need to be examined once, and each heap op is O(log k),
so O(N log k) is optimal for this merge-driven approach.
'''
