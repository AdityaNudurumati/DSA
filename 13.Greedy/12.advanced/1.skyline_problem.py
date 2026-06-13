'''
1. The Skyline Problem (Hard)
Problem Statement

A city's skyline is the outer contour formed by all its buildings when viewed from a
distance. Each building is given as [left, right, height]. Return the skyline as a list
of "key points" [x, h] sorted by x, where each key point is the left endpoint of a
horizontal segment in the silhouette. The last key point has height 0 to mark the end of
the rightmost building. No two consecutive key points may share the same height.

Example
Input:
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

Output:
[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Example
Input:
buildings = [[0,2,3],[2,5,3]]

Output:
[[0,3],[5,0]]
'''

import heapq


def getSkyline(buildings):
    # SWEEP LINE + MAX-HEAP of active building heights.
    # Build events at every x where the silhouette can change: a building's left edge
    # (height starts contributing) and its right edge (height stops contributing).
    #
    # Event encoding so a single sort gives the right tie-break order:
    #   start event: (L, -H, R)   negative height -> at the same x, TALLER starts first
    #   end event:   (R,  0, 0)   height 0 sorts AFTER any start at the same x, so a
    #                             building that ends exactly where another begins does
    #                             not emit a spurious drop-to-0.
    events = []
    for L, R, H in buildings:
        events.append((L, -H, R))   # start
        events.append((R, 0, 0))    # end
    events.sort()

    result = []
    # Max-heap (via negated heights) of (-height, right_edge) for buildings currently
    # covering the sweep position. We lazily delete: an entry is stale once the sweep x
    # has passed its right_edge, so we pop stale tops before reading the current max.
    live = [(0, float('inf'))]  # ground level always present -> max height 0 by default
    prev_max = 0

    for x, negH, R in events:
        # GREEDY local rule: the visible height at x is the tallest live building.
        # Drop any building whose right edge is <= current x (it no longer covers x).
        while live[0][1] <= x:
            heapq.heappop(live)

        if negH != 0:                       # a start event -> push the new building
            heapq.heappush(live, (negH, R))

        # Refresh: stale tops may remain if this x is only an end event.
        while live[0][1] <= x:
            heapq.heappop(live)

        cur_max = -live[0][0]
        # Emit a key point only when the visible max height actually changes.
        if cur_max != prev_max:
            result.append([x, cur_max])
            prev_max = cur_max

    return result


if __name__ == "__main__":
    print(getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # Expected: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(getSkyline([[0, 2, 3], [2, 5, 3]]))
    # Expected: [[0, 3], [5, 0]]

'''
Pattern
✅ Sweep line + max-heap of active heights (greedy "tallest visible wins")

Greedy rule & why it's safe
At any sweep position x the silhouette height is just the MAX height among buildings
that span x — a purely local choice. This is safe because the outer contour is, by
definition, the pointwise maximum of all building rectangles; no future building can
lower an already-decided segment, so taking the current tallest live building is always
optimal. We only need to recompute (and possibly emit a key point) at the discrete x
values where the live set changes — the building edges. The start/end tie-break
ordering (taller starts first; ends after starts at equal x) guarantees we never emit a
duplicate height or a false drop where buildings touch.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ Not asymptotically — sorting the 2n edge events dominates at O(n log n), and a
divide-and-conquer "merge two skylines" approach hits the same bound. The lazy-deletion
heap keeps the constant factor small versus a balanced-BST multiset.
'''
