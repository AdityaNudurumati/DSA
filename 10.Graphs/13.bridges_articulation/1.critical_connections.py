'''
1. Critical Connections in a Network (Medium)  (LC1192)
Problem Statement

There are n servers numbered from 0 to n-1 connected by undirected
connections forming a network, where connections[i] = [a, b] represents a
connection between servers a and b. Any server can reach any other server
directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some
servers unable to reach some other server. Return all critical connections
in the network in any order.

A critical connection is exactly a BRIDGE of the graph.

Input:
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

Output:
[[1,3]]

Explanation:
0-1-2 form a cycle, so none of those edges are critical. Removing edge 1-3
disconnects server 3 from the rest, so [1,3] is the only bridge.
'''

from collections import defaultdict


def criticalConnections(n, connections):
    # Build undirected adjacency list.
    adj = defaultdict(list)
    for a, b in connections:
        adj[a].append(b)
        adj[b].append(a)

    disc = [-1] * n   # discovery time of each node (-1 = unvisited)
    low = [0] * n     # lowest disc reachable from subtree of the node
    bridges = []
    timer = [0]       # mutable counter shared across recursion

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in adj[u]:
            if v == parent:
                continue          # skip the edge we came from
            if disc[v] == -1:     # tree edge: v not yet visited
                dfs(v, u)
                low[u] = min(low[u], low[v])
                # No back edge from v's subtree reaches u or above -> bridge.
                if low[v] > disc[u]:
                    bridges.append([u, v])
            else:                 # back edge
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return bridges


def canonical(edges):
    # Sort each edge's endpoints and the overall list for deterministic output.
    return sorted([sorted(e) for e in edges])


if __name__ == "__main__":
    n1 = 4
    connections1 = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(canonical(criticalConnections(n1, connections1)))  # Expected: [[1, 3]]

    # Extra: a line graph 0-1-2-3 -> every edge is a bridge.
    n2 = 4
    connections2 = [[0, 1], [1, 2], [2, 3]]
    print(canonical(criticalConnections(n2, connections2)))  # Expected: [[0, 1], [1, 2], [2, 3]]


'''
Pattern
✅ Bridges via Tarjan's low-link (DFS)
A back edge from v's subtree that reaches u or an ancestor means edge (u,v)
lies on a cycle and is NOT critical. Tracking low[v] (earliest disc reachable)
lets us test low[v] > disc[u] in a single DFS pass.
| Metric | Value      |
| ------ | ---------- |
| Time   | O(V + E)   |
| Space  | O(V + E)   |
Better Possible?
❌ No
Every vertex and edge must be examined to know the graph's structure, so
O(V + E) is optimal for finding all bridges.
'''
