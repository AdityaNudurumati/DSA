"""
2. Depth First Search (Easy)

Problem Statement:
Given an undirected graph as an adjacency list and a source vertex, return the
order in which vertices are first visited by a depth-first traversal. Neighbors
are explored in the order they appear in each adjacency list.

Example:
    Input:  adj = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}, source = 0
    Output: [0, 1, 3, 2]
"""


def dfs_order(adj, source):
    # Recursive DFS: record a node on first visit, then recurse into its
    # unvisited neighbors in list order.
    visited = set()
    order = []

    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                dfs(v)

    dfs(source)
    return order


if __name__ == "__main__":
    adj = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    print(dfs_order(adj, 0))  # Expected: [0, 1, 3, 2]

"""
Pattern: Graph Traversal (Depth First Search).
Technique: recurse from the source, marking each node visited and appending it to
the order on first sight, then diving into the first unvisited neighbor before
backtracking. From 0 we go 0->1 (1's first unvisited neighbor)->3->2, then unwind.
Why: DFS goes as deep as possible along one branch before backtracking, which
naturally produces a pre-order listing of the spanning tree.

| Metric | Value         |
|--------|---------------|
| Time   | O(V + E)      |
| Space  | O(V)          |

Better Possible?
No — every vertex and edge is examined exactly once, which is optimal for a full
traversal. The recursion stack can be swapped for an explicit stack to avoid deep
recursion limits, but the complexity is unchanged.
"""
