"""
1584. Min Cost to Connect All Points (Medium)

Problem Statement
-----------------
You are given an array of points on a 2D plane, points[i] = (xi, yi). The cost to
connect two points is their Manhattan distance |xi-xj| + |yi-yj|. Return the
minimum total cost to connect ALL points so that there is exactly one simple path
between any two points (i.e. build a Minimum Spanning Tree).

Example
-------
Input:  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Input:  points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""

import heapq


def min_cost_connect_points(points):
    n = len(points)
    if n <= 1:
        return 0

    def dist(i, j):
        # Manhattan distance between points i and j
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    in_mst = [False] * n        # whether a point is already in the tree
    total = 0
    count = 0                   # points added to the MST so far
    pq = [(0, 0)]               # min-heap of (edge_cost, point) — start at point 0

    while pq and count < n:
        cost, u = heapq.heappop(pq)
        if in_mst[u]:
            continue            # already connected via a cheaper crossing edge
        in_mst[u] = True        # add cheapest crossing edge to the tree
        total += cost
        count += 1
        # Push edges from u to every not-yet-connected point.
        for v in range(n):
            if not in_mst[v]:
                heapq.heappush(pq, (dist(u, v), v))

    return total


if __name__ == "__main__":
    print(min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # Expected: 20
    print(min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]]))                # Expected: 18


"""
Pattern
-------
Graph + Heap -> Prim's MST. The points form a complete graph weighted by
Manhattan distance. Prim's grows one tree from an arbitrary start, repeatedly
adding the cheapest edge that crosses from the tree to an outside vertex. A
min-heap supplies that cheapest crossing edge in log time; a stale entry is
skipped when its endpoint is already in the tree. Summing the chosen edges gives
the minimum total connection cost.

| Metric | Value        |
|--------|--------------|
| Time   | O(V^2 log V) |
| Space  | O(V^2)       |

Better Possible?
----------------
For this dense (complete) graph an O(V^2) Prim's with a plain distance array and
no heap is asymptotically better. Kruskal's with Union-Find is great for sparse
graphs but here would build all O(V^2) edges. The heap version cleanly fits the
"Graph + Heap" pattern.
"""
