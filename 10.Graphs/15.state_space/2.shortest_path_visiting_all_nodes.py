"""
847. Shortest Path Visiting All Nodes (Hard)

Problem Statement
-----------------
You are given an undirected, connected graph of n nodes labeled 0..n-1, given as
an adjacency list `graph` where graph[i] lists the neighbors of node i. Return
the length of the shortest path that visits every node. You may start and stop at
any node, may revisit nodes, and may reuse edges.

Example
-------
Input:  [[1,2,3],[0],[0],[0]]
Output: 4            (e.g. 1 -> 0 -> 2 -> 0 -> 3)

Input:  [[1],[0,2,4],[1,3],[2],[1]]
Output: 5            (e.g. 0 -> 1 -> 4 -> 1 -> 2 -> 3, a 5-edge walk covering all)
"""

from collections import deque


def shortest_path_length(graph):
    n = len(graph)
    if n == 1:
        return 0

    full = (1 << n) - 1  # bitmask with all n nodes visited

    # State = (current node, bitmask of visited nodes). Start BFS from EVERY node
    # simultaneously, each with only itself marked visited.
    q = deque()
    seen = set()
    for i in range(n):
        state = (i, 1 << i)
        q.append((i, 1 << i, 0))
        seen.add(state)

    # Unit-cost edges -> BFS gives shortest number of steps to reach an all-visited mask.
    while q:
        node, mask, dist = q.popleft()
        if mask == full:
            return dist
        for nb in graph[node]:
            nmask = mask | (1 << nb)
            if (nb, nmask) not in seen:
                seen.add((nb, nmask))
                q.append((nb, nmask, dist + 1))
    return -1  # graph is guaranteed connected, so this is unreachable


if __name__ == "__main__":
    print(shortest_path_length([[1, 2, 3], [0], [0], [0]]))          # Expected: 4
    print(shortest_path_length([[1], [0, 2, 4], [1, 3], [2], [1]]))  # Expected: 5


"""
Pattern
-------
Bitmask BFS (TSP-style state search). A node in the search space is not just the
graph vertex but the pair (current vertex, set-of-visited-vertices). The visited
set is encoded as an n-bit mask, so the full state space has n * 2^n nodes. Since
we may start anywhere, we seed the BFS queue with all n single-node states at
once (a multi-source BFS). Every edge costs 1, so the first time any state whose
mask equals (1<<n)-1 is dequeued, its distance is the shortest walk covering all
nodes. Allowing revisits is automatic: the mask only ever gains bits, and we key
`seen` on (node, mask) so productive re-visits with new coverage stay explorable.

| Metric | Value          |
|--------|----------------|
| Time   | O(n^2 * 2^n)   |
| Space  | O(n * 2^n)     |

Better Possible?
This is the Travelling-Salesman-walk problem, which is NP-hard, so exponential
work in n is expected. The Held-Karp DP achieves the same O(n^2 * 2^n) bound;
BFS with a (node, mask) state is the cleanest formulation when all edges are unit
weight. No polynomial algorithm is known.
"""
