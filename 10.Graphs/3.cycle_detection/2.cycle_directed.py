'''
2. Detect Cycle in a Directed Graph (Medium)
Problem Statement

Given a directed graph with V vertices (labeled 0..V-1) and a list of directed
edges [u, v] meaning an edge u -> v, determine whether the graph contains a
cycle.

Return True if at least one directed cycle exists, otherwise False.

Example:
Input:
V = 4
edges = [[0,1],[1,2],[2,3],[3,1]]
Output:
True
Explanation:
1 -> 2 -> 3 -> 1 forms a directed cycle.
'''

from collections import defaultdict


def has_cycle_directed(V, edges):
    # Build a directed adjacency list (edge added one way only).
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    # 3-color DFS:
    #   WHITE = unvisited, GRAY = on the current recursion stack, BLACK = fully done.
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * V

    def dfs(node):
        color[node] = GRAY  # node enters the recursion stack
        for nei in adj[node]:
            if color[nei] == GRAY:
                return True  # back edge to a node still on the stack => cycle
            if color[nei] == WHITE and dfs(nei):
                return True
        color[node] = BLACK  # node fully explored, leaves the stack
        return False

    # Graph may be disconnected; start DFS from every white vertex.
    for v in range(V):
        if color[v] == WHITE:
            if dfs(v):
                return True
    return False


if __name__ == "__main__":
    # Example 1: directed cycle 1 -> 2 -> 3 -> 1
    V1 = 4
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 1]]
    print(has_cycle_directed(V1, edges1))  # Expected: True

    # Example 2: directed chain 0 -> 1 -> 2, no cycle
    V2 = 3
    edges2 = [[0, 1], [1, 2]]
    print(has_cycle_directed(V2, edges2))  # Expected: False


'''
Pattern
✅ Directed Cycle Detection via 3-color DFS.
A GRAY node is currently on the recursion stack. Encountering an edge to a GRAY
node is a back edge, which proves a directed cycle. BLACK nodes are finished and
can be revisited safely (cross/forward edges are not cycles in a directed graph).

| Metric | Value      |
| ------ | ---------- |
| Time   | O(V + E)   |
| Space  | O(V + E)   |

Better Possible?
❌ Not asymptotically. Every vertex and edge is visited once -> O(V+E) optimal.
Kahn's algorithm (BFS topological sort) is an equivalent alternative: if the
topo order omits any vertex, a cycle exists.
'''
