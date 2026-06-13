"""
3. Breadth First Search (Easy)

Problem Statement:
Given an undirected graph as an adjacency list and a source vertex, return the
order in which vertices are first visited by a breadth-first traversal. Neighbors
are explored in the order they appear in each adjacency list.

Example:
    Input:  adj = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}, source = 0
    Output: [0, 1, 2, 3]
"""

from collections import deque


def bfs_order(adj, source):
    # Queue-based BFS: enqueue the source, then repeatedly dequeue a node and
    # enqueue its unvisited neighbors, recording each on first sight.
    seen = {source}
    order = []
    q = deque([source])
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return order


if __name__ == "__main__":
    adj = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    print(bfs_order(adj, 0))  # Expected: [0, 1, 2, 3]

"""
Pattern: Graph Traversal (Breadth First Search).
Technique: use a FIFO queue and a visited set. Start from the source, dequeue a
node, append it to the order, and enqueue each unvisited neighbor. From 0 we
visit its neighbors 1 and 2 before descending to 3, giving level-by-level order.
Why: BFS expands outward by distance, so nodes are listed in non-decreasing
distance from the source -- the basis for shortest paths on unweighted graphs.

| Metric | Value         |
|--------|---------------|
| Time   | O(V + E)      |
| Space  | O(V)          |

Better Possible?
No -- a full traversal must inspect every vertex and edge once, so O(V + E) time
is optimal. The visited set keeps memory at O(V).
"""
