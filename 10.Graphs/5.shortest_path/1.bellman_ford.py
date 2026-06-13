'''
1. Bellman-Ford Single-Source Shortest Path (Medium)
Problem Statement

Given a weighted directed graph with n nodes (labelled 0..n-1) described as an edge
list edges = [(u, v, w), ...] and a source src, compute the shortest distance from
src to every node. Edge weights MAY be negative. If the graph contains a negative
cycle reachable from src (a cycle whose total weight is < 0), report it because no
finite shortest path is well defined.

Example 1:
Input:  edges = [(0,1,4),(0,2,5),(1,2,-3),(2,3,4)], n = 4, src = 0
Output: [0, 4, 1, 5]
Explanation: 0->1 = 4, 0->1->2 = 4 + (-3) = 1 (better than 0->2 = 5), 0->..->2->3 = 5.

Example 2:
Input:  edges = [(0,1,1),(1,2,-1),(2,3,-1),(3,1,-1)], n = 4, src = 0
Output: "negative cycle"
Explanation: 1->2->3->1 sums to -3 (< 0); distances can be driven to -inf.
'''

INF = float('inf')


def bellman_ford(edges, n, src):
    # dist[v] = best known distance from src to v.
    dist = [INF] * n
    dist[src] = 0

    # Relax all E edges (n-1) times: any shortest path uses <= n-1 edges.
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:           # early exit: converged
            break

    # One extra pass: if anything still relaxes, a negative cycle is reachable.
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return "negative cycle"

    return dist


if __name__ == "__main__":
    edges1 = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 4)]
    print(bellman_ford(edges1, 4, 0))  # Expected: [0, 4, 1, 5]

    edges2 = [(0, 1, 1), (1, 2, -1), (2, 3, -1), (3, 1, -1)]
    print(bellman_ford(edges2, 4, 0))  # Expected: negative cycle


'''
Pattern
Bellman-Ford (dynamic-programming edge relaxation).
Unlike Dijkstra it tolerates negative edges because it does not commit greedily to a
node; it relaxes EVERY edge (n-1) times so a shortest path of at most n-1 edges is
guaranteed to settle. An n-th relaxing pass that still improves a distance proves a
reachable negative cycle, which Dijkstra cannot detect.

| Metric | Value    |
| ------ | -------- |
| Time   | O(V * E) |
| Space  | O(V)     |

Better Possible?
For single-source with negative edges, Bellman-Ford O(VE) is the standard bound.
If all weights are non-negative, Dijkstra with a heap is faster: O(E log V).
On a DAG, a topological-order relax is O(V + E) (see 3.dag_shortest_path.py).
'''
