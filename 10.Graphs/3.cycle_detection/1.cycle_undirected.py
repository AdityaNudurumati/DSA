'''
1. Detect Cycle in an Undirected Graph (Medium)
Problem Statement

Given an undirected graph with V vertices (labeled 0..V-1) and a list of
undirected edges, determine whether the graph contains a cycle.

Return True if at least one cycle exists, otherwise False.

Example:
Input:
V = 4
edges = [[0,1],[1,2],[2,3],[3,1]]
Output:
True
Explanation:
1 -> 2 -> 3 -> 1 forms a cycle.
'''

from collections import defaultdict


def has_cycle_undirected(V, edges):
    # Build an undirected adjacency list (each edge added both ways).
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * V

    # DFS that remembers the parent we came from.
    # If we reach a visited node that is NOT our parent, that is a back edge -> cycle.
    def dfs(node, parent):
        visited[node] = True
        for nei in adj[node]:
            if not visited[nei]:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True  # visited non-parent neighbor => cycle
        return False

    # Graph may be disconnected, so launch DFS from every unvisited vertex.
    for v in range(V):
        if not visited[v]:
            if dfs(v, -1):
                return True
    return False


if __name__ == "__main__":
    # Example 1: contains a cycle 1-2-3-1
    V1 = 4
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 1]]
    print(has_cycle_undirected(V1, edges1))  # Expected: True

    # Example 2: a simple path, no cycle
    V2 = 3
    edges2 = [[0, 1], [1, 2]]
    print(has_cycle_undirected(V2, edges2))  # Expected: False


'''
Pattern
✅ Undirected Cycle Detection via DFS with parent tracking.
In an undirected graph every edge is bidirectional, so the edge back to the
node we just came from is not a cycle. We track the parent and only flag a
cycle when we meet an already-visited neighbor that is not that parent.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(V + E)   |
| Space  | O(V + E)   |

Better Possible?
❌ Not asymptotically. We must inspect every vertex and edge once, so O(V+E)
is optimal. Union-Find achieves the same bound and is an alternative when the
graph is given purely as an edge list.
'''
