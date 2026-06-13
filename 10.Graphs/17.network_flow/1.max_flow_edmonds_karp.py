"""
1. Maximum Flow via Edmonds-Karp (Hard)

Problem Statement:
Given a directed graph where each edge u->v has a non-negative integer capacity,
a source vertex s and a sink vertex t, find the maximum total flow that can be
pushed from s to t. Flow on each edge must not exceed its capacity, and at every
intermediate vertex flow in equals flow out (conservation).

Edmonds-Karp is Ford-Fulkerson where each augmenting path is the shortest (fewest
edges) path in the residual graph, found by BFS. This guarantees O(V*E^2) time.

Example:
    Input:  6-node network, capacities
            {0->1:16, 0->2:13, 1->2:10, 1->3:12, 2->1:4, 2->4:14,
             3->2:9, 3->5:20, 4->3:7, 4->5:4}, source = 0, sink = 5
    Output: 23
"""

from collections import deque


def max_flow_edmonds_karp(n, capacity, source, sink):
    # Residual capacity matrix; cap[u][v] is the remaining capacity of edge u->v.
    cap = [[0] * n for _ in range(n)]
    for (u, v), c in capacity.items():
        cap[u][v] += c

    def bfs_augmenting_path():
        # BFS from source; parent[v] records the predecessor on a shortest path.
        parent = [-1] * n
        parent[source] = source
        q = deque([source])
        while q:
            u = q.popleft()
            for v in range(n):
                # Unvisited and residual capacity left on edge u->v.
                if parent[v] == -1 and cap[u][v] > 0:
                    parent[v] = u
                    if v == sink:
                        return parent
                    q.append(v)
        return None

    total = 0
    while True:
        parent = bfs_augmenting_path()
        if parent is None:
            break  # no more augmenting paths -> flow is maximal

        # Bottleneck: minimum residual capacity along the path sink<-...<-source.
        bottleneck = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            bottleneck = min(bottleneck, cap[u][v])
            v = u

        # Push bottleneck flow: reduce forward edges, increase reverse (residual) edges.
        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= bottleneck
            cap[v][u] += bottleneck
            v = u

        total += bottleneck

    return total


if __name__ == "__main__":
    caps = {
        (0, 1): 16, (0, 2): 13, (1, 2): 10, (1, 3): 12, (2, 1): 4,
        (2, 4): 14, (3, 2): 9, (3, 5): 20, (4, 3): 7, (4, 5): 4,
    }
    print(max_flow_edmonds_karp(6, caps, 0, 5))  # Expected: 23

"""
Pattern: Network Flow (Edmonds-Karp augmenting paths).
Technique: maintain a residual graph as a capacity matrix. Repeatedly BFS for the
shortest source->sink path with spare capacity, compute its bottleneck, then push
that flow by decrementing forward residual edges and incrementing reverse edges.
Sum of bottlenecks is the maximum flow (= the minimum cut by max-flow min-cut).
Why BFS (not DFS): always choosing the shortest augmenting path bounds the number
of augmentations to O(V*E), independent of capacity magnitudes, avoiding the
pathological slow convergence plain Ford-Fulkerson can suffer with large capacities.

| Metric | Value      |
|--------|------------|
| Time   | O(V * E^2) |
| Space  | O(V^2)     |

Better Possible?
Yes. Dinic's algorithm (BFS level graph + blocking flow) runs in O(V^2 * E), and
O(E * sqrt(V)) on unit-capacity graphs. Push-relabel variants reach O(V^3) or
O(V^2 * sqrt(E)). Edmonds-Karp is chosen here for clarity on a small network.
"""
