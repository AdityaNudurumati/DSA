"""
684. Redundant Connection (Medium)

Problem Statement
A tree is an undirected graph that is connected and has no cycles. You are given
a graph that started as a tree with n nodes labeled 1..n, with one extra edge added.
The added edge has two different vertices and is not already present.

Return the edge that can be removed so the resulting graph is a tree of n nodes.
If there are multiple answers, return the edge that occurs LAST in the input.

Example:
    Input:  [[1,2],[1,3],[2,3]]
    Output: [2,3]

    Input:  [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]
"""


def find_redundant_connection(edges):
    n = len(edges)                       # n nodes, labeled 1..n
    parent = list(range(n + 1))          # 1-indexed
    rank = [0] * (n + 1)

    def find(x):
        # Path compression (halving)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False                 # already connected -> this edge closes a cycle
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    # First edge whose endpoints already share a root is the redundant one.
    # Scanning in input order means we naturally return the last such edge.
    for u, v in edges:
        if not union(u, v):
            return [u, v]
    return []                            # guaranteed not reached for valid input


if __name__ == "__main__":
    edges1 = [[1, 2], [1, 3], [2, 3]]
    print(find_redundant_connection(edges1))  # Expected: [2, 3]

    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(find_redundant_connection(edges2))  # Expected: [1, 4]


"""
Pattern: Union Find (DSU) — cycle detection in an undirected graph.
Process edges left to right; union(u, v) returns False when u and v already share
a root, meaning adding this edge would form a cycle. Because we scan in input
order, the first such failure is exactly the last edge of the input that creates
a cycle — the required answer. Path compression + union by rank give near-O(1) ops.

| Metric | Value          |
|--------|----------------|
| Time   | O(N * α(N))    |
| Space  | O(N)           |

Better Possible?
No. Every edge must be examined at least once, so O(N) is a lower bound; the
inverse-Ackermann α(N) factor is effectively constant. DFS/BFS cycle detection is
also O(N) but DSU is the cleanest fit for incremental edge processing.
"""
