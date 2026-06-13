"""
1584. Min Cost to Connect All Points (Medium)

Problem Statement
You are given an array points representing integer coordinates of some points on a
2D plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the Manhattan distance
between them: |xi - xj| + |yi - yj|.

Return the minimum cost to make all points connected. All points are connected if
there is exactly one simple path between any two points.

Example:
    Input:  [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20

    Input:  [[3,12],[-2,5],[-4,1]]
    Output: 18
"""


def min_cost_connect_points(points):
    n = len(points)
    if n <= 1:
        return 0

    # Build every candidate edge (i, j) with its Manhattan weight.
    # The complete graph has n*(n-1)/2 edges; Kruskal sorts them and adds the
    # cheapest that joins two distinct components (a DSU forest).
    edges = []  # (weight, u, v)
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            w = abs(xi - xj) + abs(yi - yj)
            edges.append((w, i, j))
    edges.sort()  # sort by weight ascending — Kruskal's core step

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        # Path compression (halving)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False                 # already connected -> skip, would form a cycle
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    total = 0
    used = 0
    # Greedily add cheapest edges that connect new components until the tree
    # spans all n points (exactly n-1 edges form a spanning tree).
    for w, u, v in edges:
        if union(u, v):
            total += w
            used += 1
            if used == n - 1:
                break
    return total


if __name__ == "__main__":
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(min_cost_connect_points(points1))  # Expected: 20

    points2 = [[3, 12], [-2, 5], [-4, 1]]
    print(min_cost_connect_points(points2))  # Expected: 18


"""
Pattern: Minimum Spanning Tree — Kruskal + DSU (Union Find).
We treat the points as a complete weighted graph (every pair connected by its
Manhattan distance). Kruskal sorts all edges ascending and walks them, adding an
edge only when its endpoints lie in different DSU components — this never creates
a cycle and always picks the globally cheapest safe edge. After n-1 successful
unions every point is connected with provably minimum total weight. Path
compression + union by rank keep each DSU operation near-constant.

| Metric | Value                |
|--------|----------------------|
| Time   | O(E log E) = O(N^2 log N) |
| Space  | O(E) = O(N^2)        |

Better Possible?
For this dense complete graph (E ~ N^2), Prim's with an adjacency-scan runs in
O(N^2) and avoids materializing/sorting all edges — asymptotically better here,
so the heap/Prim version belongs in the Heap pattern folder. Kruskal shines on
sparse graphs where E << N^2. The MST weight itself cannot be beaten; only the
construction cost differs.
"""
