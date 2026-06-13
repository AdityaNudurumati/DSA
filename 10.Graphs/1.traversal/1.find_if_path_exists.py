"""
1971. Find if Path Exists in Graph (Easy)

Problem Statement:
There is a bi-directional graph with n vertices labeled 0..n-1. The edges are
given as a list of pairs edges[i] = [u, v]. Given source and destination
vertices, return True if a valid path exists from source to destination.

Example:
    Input:  n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: True

    Input:  n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: False
"""

from collections import deque


def valid_path(n, edges, source, destination):
    # Build undirected adjacency list, then BFS from source looking for destination.
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    if source == destination:
        return True

    seen = {source}
    q = deque([source])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v == destination:
                return True
            if v not in seen:
                seen.add(v)
                q.append(v)
    return False


if __name__ == "__main__":
    print(valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2))               # Expected: True
    print(valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # Expected: False

"""
Pattern: Graph Traversal (reachability via BFS).
Technique: build an undirected adjacency list, then breadth-first search from the
source, marking nodes in a visited set; if we ever reach the destination a path
exists. Equivalent to checking source and destination share a connected component.
Why: traversal touches each reachable node once; reachability is symmetric in an
undirected graph so any spanning order (BFS or DFS) answers the question.

| Metric | Value         |
|--------|---------------|
| Time   | O(V + E)      |
| Space  | O(V + E)      |

Better Possible?
Not asymptotically for a single query — every edge may need inspection. For many
queries on a static graph, Union-Find precomputation gives near O(1) per query.
"""
