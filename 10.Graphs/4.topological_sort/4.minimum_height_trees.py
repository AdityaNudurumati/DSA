'''
310. Minimum Height Trees (Medium)
Problem Statement

Given a tree of n nodes labeled 0..n-1 described by n-1 undirected edges, a
node may be chosen as root. Among all rootings, find every node that yields a
tree of minimum height.

Return the list of all such root labels (there are at most two).

Input:
n = 4
edges = [[1, 0], [1, 2], [1, 3]]

Output:
[1]

Explanation:
Rooting at node 1 gives height 1, the minimum.
'''

from collections import deque


def find_min_height_trees(n, edges):
    # A single node (or trivial graph) is its own center.
    if n <= 1:
        return [0]

    # Build undirected adjacency and degree counts.
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)

    # Topological leaf-peeling: repeatedly strip the current leaves.
    leaves = deque(u for u in range(n) if len(adj[u]) == 1)
    remaining = n
    while remaining > 2:
        size = len(leaves)
        remaining -= size
        for _ in range(size):
            leaf = leaves.popleft()
            nbr = adj[leaf].pop()       # leaf has exactly one neighbour
            adj[nbr].discard(leaf)
            if len(adj[nbr]) == 1:
                leaves.append(nbr)

    # The 1 or 2 survivors are the centroids = minimum-height roots.
    return sorted(leaves)


if __name__ == "__main__":
    print(find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]]))                       # Expected: [1]
    print(find_min_height_trees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))       # Expected: [3, 4]


'''
Pattern
✅ Topological Sort variant (leaf-peeling toward the centroid)
A minimum-height root is a center (centroid) of the tree, and a tree has at
most two centers. We peel leaves layer by layer (like Kahn's on degree-1
nodes) until 1 or 2 nodes remain - those are the answers. Sorting the result
makes the two-center output deterministic.

| Metric | Value |
| ------ | ----- |
| Time   | O(V)  |
| Space  | O(V)  |

(For a tree E = V - 1, so O(V + E) = O(V).)

Better Possible?
❌ No. Every node and edge is touched once during peeling, so O(V) is optimal.
'''
