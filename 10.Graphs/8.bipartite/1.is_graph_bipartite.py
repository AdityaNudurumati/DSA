'''
785. Is Graph Bipartite? (Medium)
Problem Statement

There is an undirected graph with n nodes, where each node is numbered between
0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes
that node u is adjacent to.

A graph is bipartite if the nodes can be split into two independent sets A and B
such that every edge connects a node in A and a node in B.

Return True if and only if the graph is bipartite.

Example:
Input:
graph = [[1,3],[0,2],[1,3],[0,2]]
Output:
True

Input:
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output:
False
'''

from collections import deque


def isBipartite(graph):
    n = len(graph)
    color = {}                       # node -> 0/1; absence = uncolored

    for start in range(n):
        if start in color:
            continue                 # already handled in another component
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in color:
                    color[v] = color[u] ^ 1   # paint neighbour opposite colour
                    q.append(v)
                elif color[v] == color[u]:
                    return False              # same colour on both ends => odd cycle
    return True


if __name__ == "__main__":
    graph1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(isBipartite(graph1))  # Expected: True

    graph2 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(isBipartite(graph2))  # Expected: False


'''
Pattern
✅ Bipartite Graph - BFS 2-coloring
Paint each node, then paint every neighbour the opposite colour. If an edge ever
joins two equal colours, an odd-length cycle exists and the graph is NOT bipartite.
Looping over all start nodes covers disconnected components.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(V + E)   |
| Space  | O(V)       |

Better Possible?
❌ No
Every node and edge must be examined at least once to certify colouring.
Union-Find gives the same O(V + E) bound; BFS/DFS coloring is optimal.
'''
