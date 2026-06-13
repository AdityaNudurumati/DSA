"""
1. Strongly Connected Components - Kosaraju (Medium)

Problem Statement:
Given a directed graph as an adjacency list, count the number of strongly
connected components (SCCs). An SCC is a maximal set of vertices such that
every vertex is reachable from every other vertex within the set.

Use Kosaraju's two-pass algorithm.

Example:
    Input:  n = 5, adj = {0:[1], 1:[2], 2:[0,3], 3:[4], 4:[]}
    Output: 3        # SCCs are {0,1,2}, {3}, {4}
"""


def kosaraju_scc_count(n, adj):
    # Pass 1: DFS on original graph, pushing vertices onto a stack by finish time.
    visited = [False] * n
    order = []

    def dfs1(start):
        # Iterative DFS; record vertex after its whole subtree is explored.
        stack = [(start, iter(adj[start]))]
        visited[start] = True
        while stack:
            node, it = stack[-1]
            advanced = False
            for v in it:
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, iter(adj[v])))
                    advanced = True
                    break
            if not advanced:
                order.append(node)  # finished -> post-order
                stack.pop()

    for u in range(n):
        if not visited[u]:
            dfs1(u)

    # Build transpose (reverse every edge).
    radj = {i: [] for i in range(n)}
    for u in range(n):
        for v in adj[u]:
            radj[v].append(u)

    # Pass 2: DFS on transpose in reverse finish order; each tree is one SCC.
    visited = [False] * n
    count = 0

    def dfs2(start):
        stack = [start]
        visited[start] = True
        while stack:
            node = stack.pop()
            for v in radj[node]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

    for u in reversed(order):
        if not visited[u]:
            count += 1
            dfs2(u)

    return count


if __name__ == "__main__":
    adj1 = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: []}
    print(kosaraju_scc_count(5, adj1))                       # Expected: 3

    # Fully cyclic graph 0->1->2->0 collapses into a single SCC.
    adj2 = {0: [1], 1: [2], 2: [0]}
    print(kosaraju_scc_count(3, adj2))                       # Expected: 1

    # Disjoint pieces: cycle {0,1} and self-contained singletons 2, 3.
    adj3 = {0: [1], 1: [0], 2: [3], 3: []}
    print(kosaraju_scc_count(4, adj3))                       # Expected: 3

"""
Pattern: Strongly Connected Components via Kosaraju (two-pass DFS).
Technique: (1) DFS the graph pushing each vertex onto a stack when it finishes,
giving a reverse-topological order of the condensation. (2) Reverse every edge
and run DFS popping vertices in that order; each DFS tree on the transpose is
exactly one SCC. Reversing edges keeps SCCs intact but cuts the cross-component
links so a single tree cannot leak into another component.
Why: finishing order guarantees we start pass 2 from a "sink" SCC of the
condensation DAG, so each traversal stays confined to one component.

| Metric | Value     |
|--------|-----------|
| Time   | O(V + E)  |
| Space  | O(V + E)  |

Better Possible?
No better asymptotic bound exists; SCCs need every edge examined, so O(V+E) is
optimal. Tarjan's algorithm matches the bound in a single DFS pass (smaller
constant, no transpose), which is the only practical improvement.
"""
