'''
3. Shortest Path in a Weighted DAG (Medium)
Problem Statement

Given a weighted Directed Acyclic Graph with n nodes (0..n-1) as an edge list
edges = [(u, v, w), ...] and a source src, return the shortest distance from src to
every node. Unreachable nodes report infinity (-1 in the printed canonical form).
Edge weights may be negative; because the graph is a DAG there are no cycles, so a
single relaxation pass in topological order is both correct and optimal.

Example:
Input:  n = 6, src = 0,
        edges = [(0,1,2),(0,2,4),(1,2,1),(1,3,7),(2,4,3),(3,5,1),(4,3,2),(4,5,5)]
Output: [0, 2, 3, 8, 6, 9]
Explanation:
  d0=0
  d1=0->1 = 2
  d2=0->1->2 = 2+1 = 3 (better than 0->2 = 4)
  d4=0->1->2->4 = 3+3 = 6
  d3=0->1->2->4->3 = 6+2 = 8 (better than 0->1->3 = 9)
  d5=0->..->3->5 = 8+1 = 9 (better than 0->..->4->5 = 11)
'''

from collections import defaultdict, deque

INF = float('inf')


def dag_shortest_path(edges, n, src):
    adj = defaultdict(list)
    indeg = [0] * n
    for u, v, w in edges:
        adj[u].append((v, w))
        indeg[v] += 1

    # Kahn's topological sort.
    topo = []
    q = deque(i for i in range(n) if indeg[i] == 0)
    while q:
        u = q.popleft()
        topo.append(u)
        for v, _ in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # Relax edges once each, in topological order: when we process u its
    # distance is already final, so out-edges yield final distances downstream.
    dist = [INF] * n
    dist[src] = 0
    for u in topo:
        if dist[u] == INF:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


if __name__ == "__main__":
    edges = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7),
             (2, 4, 3), (3, 5, 1), (4, 3, 2), (4, 5, 5)]
    print(dag_shortest_path(edges, 6, 0))  # Expected: [0, 2, 3, 8, 6, 9]


'''
Pattern
DAG Shortest Path (topological order + single relax pass).
On a DAG there is a linear order in which every edge points "forward". Processing
nodes in that order guarantees a node's distance is finalized before its out-edges are
relaxed, so one pass over the edges suffices. This handles negative weights (no cycles
to exploit) and is faster than both Dijkstra and Bellman-Ford.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(V + E)   |
| Space  | O(V + E)   |

Better Possible?
No. Every node and edge must be examined at least once, so O(V + E) is optimal.
This is strictly better than Dijkstra (O(E log V)) and Bellman-Ford (O(VE)) and is the
algorithm of choice whenever the graph is acyclic.
'''
