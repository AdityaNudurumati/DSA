"""
133. Clone Graph (Medium)

Problem Statement:
Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node contains a value and a list of its neighbors.

Example:
    Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]   (1-indexed)
    Output: [[2,4],[1,3],[2,4],[1,3]]             (clone's reconstructed adjacency)
"""

from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    # BFS over the original; a dict maps original node -> its clone.
    if not node:
        return None
    clones = {node: Node(node.val)}
    q = deque([node])
    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei not in clones:
                clones[nei] = Node(nei.val)   # create clone on first sight
                q.append(nei)
            clones[cur].neighbors.append(clones[nei])  # wire the cloned edge
    return clones[node]


def build_graph(adj_list):
    # Build an undirected graph from a 1-indexed adjacency list.
    n = len(adj_list)
    nodes = [Node(i + 1) for i in range(n)]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0] if nodes else None


def to_adj_list(node):
    # Reconstruct a 1-indexed adjacency list from a graph via BFS.
    if not node:
        return []
    seen = {node.val: node}
    q = deque([node])
    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei.val not in seen:
                seen[nei.val] = nei
                q.append(nei)
    return [[nei.val for nei in seen[v].neighbors] for v in sorted(seen)]


if __name__ == "__main__":
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = clone_graph(original)
    print(to_adj_list(cloned))  # Expected: [[2, 4], [1, 3], [2, 4], [1, 3]]

"""
Pattern: Graph BFS with a visited/clone map.
Technique: traverse the original graph breadth-first; a hash map from original
node to clone both serves as the visited set and lets us reattach edges between
already-created clones.
Why: BFS guarantees each node is enqueued once; the map prevents infinite loops
in cyclic graphs and ensures shared neighbors map to the same clone instance.

| Metric | Value     |
|--------|-----------|
| Time   | O(V + E)  |
| Space  | O(V)      |

Better Possible?
No — every node and edge must be copied, so O(V + E) work is required. DFS is an
equally valid alternative with the same complexity.
"""
