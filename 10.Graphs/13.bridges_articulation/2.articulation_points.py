'''
2. Articulation Points (Medium)
Problem Statement

Given an undirected connected graph with n vertices (numbered 0 to n-1) and
an edge list, find all articulation points (cut vertices).

A vertex is an articulation point if removing it (and its incident edges)
increases the number of connected components of the graph.

Return the articulation points sorted in ascending order.

Input:
n = 5
edges = [[0,1],[1,2],[2,0],[1,3],[3,4]]

Output:
[1, 3]

Explanation:
0-1-2 form a cycle. Removing vertex 1 disconnects {3,4} from the cycle.
Removing vertex 3 disconnects vertex 4. Vertices 0, 2, 4 are not critical.
'''

from collections import defaultdict


def articulationPoints(n, edges):
    # Build undirected adjacency list.
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    disc = [-1] * n        # discovery times (-1 = unvisited)
    low = [0] * n          # low-link values
    is_ap = [False] * n    # marks articulation points
    timer = [0]

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        children = 0       # number of DFS-tree children of u
        for v in adj[u]:
            if v == parent:
                continue
            if disc[v] == -1:          # tree edge
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                # Non-root u is a cut vertex if a child's subtree cannot
                # reach above u via a back edge.
                if parent != -1 and low[v] >= disc[u]:
                    is_ap[u] = True
            else:                       # back edge
                low[u] = min(low[u], disc[v])
        # Root is a cut vertex iff it has 2+ DFS-tree children.
        if parent == -1 and children > 1:
            is_ap[u] = True

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return sorted([i for i in range(n) if is_ap[i]])


if __name__ == "__main__":
    n1 = 5
    edges1 = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
    print(articulationPoints(n1, edges1))  # Expected: [1, 3]

    # Extra: a star 0 connected to 1,2,3 -> center 0 is the only cut vertex.
    n2 = 4
    edges2 = [[0, 1], [0, 2], [0, 3]]
    print(articulationPoints(n2, edges2))  # Expected: [0]


'''
Pattern
✅ Cut vertices via Tarjan's low-link (DFS)
Same disc/low machinery as bridges, but the test differs: a non-root u is an
articulation point when some child v satisfies low[v] >= disc[u] (its subtree
cannot escape above u). The DFS root is special: it is a cut vertex only when
it has two or more DFS-tree children.
| Metric | Value      |
| ------ | ---------- |
| Time   | O(V + E)   |
| Space  | O(V + E)   |
Better Possible?
❌ No
All vertices and edges must be inspected, so O(V + E) is optimal.
'''
