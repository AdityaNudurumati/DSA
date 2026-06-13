'''
1976. Number of Ways to Arrive at Destination (Medium)
Problem Statement

You are in a city of n intersections (labelled 0..n-1) connected by bi-directional
roads. roads[i] = [u, v, time] means a road between u and v takes `time` minutes.
You start at intersection 0 and want to reach intersection n-1 in the SHORTEST amount
of time. Return the number of distinct ways you can travel from 0 to n-1 in that
minimum time. Because the answer may be large, return it modulo 1e9 + 7.

Example 1:
Input:  n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],
                        [6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest time from 0 to 6 is 7 minutes. Four distinct paths reach
6 in 7 minutes: 0->6, 0->4->6, 0->1->2->5->6, 0->1->3->5->6.

Example 2:
Input:  n = 2, roads = [[1,0,10]]
Output: 1
Explanation: Only one road / one way: 0 -> 1 in 10 minutes.
'''

import heapq
from collections import defaultdict

MOD = 10**9 + 7
INF = float('inf')


def count_paths(n, roads):
    # Build undirected weighted adjacency list.
    adj = defaultdict(list)
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = [INF] * n        # shortest time from 0 to each node
    ways = [0] * n          # number of shortest-time paths to each node
    dist[0] = 0
    ways[0] = 1

    # Dijkstra carrying a path count alongside the distance.
    pq = [(0, 0)]           # (current_time, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:     # stale heap entry
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                # Found a strictly shorter path: reset count to u's count.
                dist[v] = nd
                ways[v] = ways[u]
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                # Another shortest path of equal length: accumulate.
                ways[v] = (ways[v] + ways[u]) % MOD

    return ways[n - 1] % MOD


if __name__ == "__main__":
    roads1 = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
              [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    print(count_paths(7, roads1))   # Expected: 4

    roads2 = [[1, 0, 10]]
    print(count_paths(2, roads2))   # Expected: 1


'''
Pattern
Dijkstra + path counting (advanced shortest path).
Standard Dijkstra finds the shortest distance; here we piggyback a `ways[]` array.
Because non-negative weights mean a node is finalized when first popped, every edge
relaxation falls into one of two cases: a STRICTLY shorter path overwrites both the
distance and resets the count to the predecessor's count; an EQUAL-length path adds
the predecessor's count (mod 1e9+7). This correctly tallies all minimum-time paths in
a single pass without enumerating them, and the modulo keeps the count bounded.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(E log V)    |
| Space  | O(V + E)      |

Better Possible?
O(E log V) is the standard Dijkstra bound and optimal for general non-negative graphs.
Counting adds only O(1) work per relaxation, so it does not change the complexity.
A DAG of shortest-path edges could be counted by a topological-order DP, but building
it still requires a shortest-path pass first, so this single Dijkstra is the cleanest.
'''
