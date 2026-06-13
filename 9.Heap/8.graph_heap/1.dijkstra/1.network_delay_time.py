"""
743. Network Delay Time (Medium)

Problem Statement
-----------------
You are given a network of n nodes, labeled 1..n, and a list of travel times as
directed edges times[i] = (u, v, w): a signal takes w time to go from u to v.
We send a signal from node k. Return the minimum time for ALL n nodes to receive
the signal. If it is impossible for every node to receive it, return -1.

Example
-------
Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
    (2->1 takes 1, 2->3 takes 1, 3->4 takes 2; max finalized dist = 2)

Input:  times = [[1,2,1]], n = 2, k = 1   -> Output: 1
Input:  times = [[1,2,1]], n = 2, k = 2   -> Output: -1  (node 1 unreachable)
"""

import heapq


def network_delay_time(times, n, k):
    # Build adjacency list: u -> list of (v, w)
    adj = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        adj[u].append((v, w))

    dist = {k: 0}            # finalized shortest distances from source k
    pq = [(0, k)]            # min-heap of (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue          # stale heap entry, skip
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    # All nodes must be reached; answer is the slowest arrival.
    if len(dist) < n:
        return -1
    return max(dist.values())


if __name__ == "__main__":
    print(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # Expected: 2
    print(network_delay_time([[1, 2, 1]], 2, 1))                        # Expected: 1
    print(network_delay_time([[1, 2, 1]], 2, 2))                        # Expected: -1


"""
Pattern
-------
Graph + Heap -> Dijkstra. Single source, non-negative weights. A min-heap always
pops the globally closest unfinalized node, so the first time we pop a node its
distance is final. We relax outgoing edges and push improved distances. Network
Delay Time = run Dijkstra from k, then the time for all nodes to receive the
signal is the maximum finalized distance (the slowest path); -1 if any node is
unreachable.

| Metric | Value         |
|--------|---------------|
| Time   | O(E log V)    |
| Space  | O(V + E)      |

Better Possible?
----------------
For dense graphs an O(V^2) array-based Dijkstra can win, and Bellman-Ford handles
negative weights at O(V*E). For non-negative weights with sparse edges, this
heap-based Dijkstra is the standard optimal choice.
"""
