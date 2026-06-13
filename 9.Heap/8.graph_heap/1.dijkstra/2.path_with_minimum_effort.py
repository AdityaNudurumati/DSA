"""
1631. Path With Minimum Effort (Medium)

Problem Statement
-----------------
You are a hiker on a grid of heights with R rows and C columns. From a cell you
may move up/down/left/right. A route's "effort" is the MAXIMUM absolute height
difference between two consecutive cells along that route. Starting at the
top-left cell and ending at the bottom-right cell, return the minimum effort
required (the smallest possible maximum step difference).

Example
-------
Input:  heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
    (route 1->3->5->3->5 has consecutive diffs <= 2; the 8 cell forces larger)

Input:  heights = [[1,2,3],[3,8,4],[5,3,5]]                         -> Output: 1
Input:  heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],
                   [1,2,1,2,1],[1,1,1,2,1]]                          -> Output: 0
"""

import heapq


def minimum_effort_path(heights):
    R, C = len(heights), len(heights[0])
    # effort[r][c] = minimum possible "max step difference" to reach (r, c)
    effort = [[float("inf")] * C for _ in range(R)]
    effort[0][0] = 0
    pq = [(0, 0, 0)]        # min-heap of (effort_so_far, row, col)

    while pq:
        e, r, c = heapq.heappop(pq)
        if (r, c) == (R - 1, C - 1):
            return e          # first time we pop the target -> answer is final
        if e > effort[r][c]:
            continue          # stale entry
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                # edge weight is the height diff; path cost is the MAX edge so far
                ne = max(e, abs(heights[nr][nc] - heights[r][c]))
                if ne < effort[nr][nc]:
                    effort[nr][nc] = ne
                    heapq.heappush(pq, (ne, nr, nc))
    return 0


if __name__ == "__main__":
    print(minimum_effort_path([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))        # Expected: 2
    print(minimum_effort_path([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))        # Expected: 1
    print(minimum_effort_path([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1],
                               [1, 2, 1, 2, 1], [1, 2, 1, 2, 1],
                               [1, 1, 1, 2, 1]]))                        # Expected: 0


"""
Pattern
-------
Graph + Heap -> Dijkstra on a "min-max" (bottleneck) objective. The grid is a
graph; each adjacency is an edge weighted by the height difference. Instead of
summing edge weights, a path's cost is the MAXIMUM edge on it, and we want the
path minimizing that maximum. Dijkstra still works because the bottleneck metric
is monotonic: extending a path can only keep or increase its max. We relax with
ne = max(effort_so_far, edge), and the first pop of the bottom-right cell is the
optimal answer.

| Metric | Value          |
|--------|----------------|
| Time   | O(R*C log(R*C))|
| Space  | O(R*C)         |

Better Possible?
----------------
Alternatives: binary search on the answer + BFS/DFS feasibility (O(R*C log(maxH)))
or a Union-Find over edges sorted by weight (near-linear after sorting). They are
comparable in practice; the heap-based Dijkstra here is clean and optimal-class.
"""
