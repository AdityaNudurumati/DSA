"""
261. Graph Valid Tree (Medium)

Problem Statement
You have n nodes labeled 0..n-1 and a list of undirected edges. Determine whether
these edges form a valid tree.

A graph is a valid tree iff it is:
  1. Connected   (all nodes reachable), and
  2. Acyclic     (no cycle).
Equivalently: connected AND exactly n-1 edges.

Example:
    Input:  n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: True

    Input:  n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: False   (edge [1,3] closes a cycle)
"""


def valid_tree(n, edges):
    # A tree on n nodes has exactly n-1 edges. Wrong count -> cannot be a tree.
    if len(edges) != n - 1:
        return False

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False                 # cycle: endpoints already connected
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    # With exactly n-1 edges, if no union ever fails (no cycle) the graph must be
    # connected as a single component -> valid tree.
    for u, v in edges:
        if not union(u, v):
            return False
    return True


if __name__ == "__main__":
    print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))            # Expected: True
    print(valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))   # Expected: False


"""
Pattern: Union Find (DSU) — connectivity + cycle detection together.
Key insight: a graph is a tree iff it has exactly n-1 edges AND is acyclic. We first
reject any edge count != n-1 in O(1). Then we union every edge; if union ever finds
both endpoints already share a root, a cycle exists -> not a tree. Surviving the scan
with n-1 acyclic edges forces a single connected component, so it is a valid tree.
Path compression + union by rank give near-O(1) per operation.

| Metric | Value          |
|--------|----------------|
| Time   | O(N * α(N))    |
| Space  | O(N)           |

Better Possible?
No. Reading every edge is required, so O(N) is optimal; α(N) is effectively constant.
A DFS/BFS that checks "n-1 edges + fully reachable from node 0" runs in the same
O(N) time — DSU is just the most direct expression for edge-by-edge merging.
"""
