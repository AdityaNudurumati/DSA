'''
2. Number of Connected Components in an Undirected Graph (Medium) [LC323]
Problem Statement

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n
and a list of edges where edges[i] = [a, b] indicates an undirected edge between
nodes a and b.

Return the number of connected components in the graph.

Example:
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input:  n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
'''

from collections import defaultdict


def countComponents(n, edges):
    # build undirected adjacency list from the edge list
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for nxt in adj[node]:
            if not visited[nxt]:
                dfs(nxt)

    components = 0
    for node in range(n):
        if not visited[node]:
            components += 1     # one DFS launch == one component
            dfs(node)
    return components


if __name__ == "__main__":
    print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))            # Expected: 2
    print(countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))    # Expected: 1


'''
Pattern
✅ Connected Components (DFS over an adjacency list)
Convert the edge list to an adjacency list, then count how many times we must
launch a DFS to cover every node. Each launch reaches exactly one component.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(V + E)   |
| Space  | O(V + E)   |

We touch each vertex and edge a constant number of times; space holds the
adjacency list plus visited array and recursion stack.

Better Possible?
❌ O(V + E) is optimal since every node/edge must be examined at least once.
Union-Find is an alternative with the same complexity (near-O(E*alpha)).
'''
