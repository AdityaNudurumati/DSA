"""
2. Maximum Bipartite Matching (Medium)

Problem Statement:
Given a bipartite graph with a left set and a right set of vertices, and edges only
between the two sets, find the maximum matching: the largest set of edges such that
no two share an endpoint. Modeled as network flow with unit capacities (source ->
each left, each edge left->right, each right -> sink, all capacity 1); equivalently
solved directly by Kuhn's algorithm using augmenting paths.

Example:
    Input:  left = {0, 1, 2}, right vertices reachable via
            adj = {0: [0, 1], 1: [0], 2: [1, 2]}
    Output: 3
"""


def max_bipartite_matching(adj, num_right):
    # match_right[r] = left vertex currently matched to right vertex r, or -1.
    match_right = [-1] * num_right

    def try_augment(u, visited):
        # Attempt to find an augmenting path starting from left vertex u.
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            # v is free, or its current partner can be re-matched elsewhere.
            if match_right[v] == -1 or try_augment(match_right[v], visited):
                match_right[v] = u
                return True
        return False

    matching = 0
    for u in adj:
        visited = [False] * num_right
        if try_augment(u, visited):
            matching += 1
    return matching


if __name__ == "__main__":
    adj = {0: [0, 1], 1: [0], 2: [1, 2]}
    print(max_bipartite_matching(adj, 3))  # Expected: 3

"""
Pattern: Network Flow specialized to Bipartite Matching (Kuhn's algorithm).
Technique: for each left vertex, run a DFS that seeks an augmenting path through the
current matching. An edge to a free right vertex, or to one whose partner can be
shifted away recursively, increases the matching by one. This is exactly Ford-
Fulkerson on the unit-capacity flow network where flipping a matched edge corresponds
to traversing a residual (reverse) edge.
Why: by Konig/augmenting-path theory a matching is maximum iff no augmenting path
exists, so greedily augmenting from every left vertex yields the optimum.

| Metric | Value      |
|--------|------------|
| Time   | O(V * E)   |
| Space  | O(V + E)   |

Better Possible?
Yes. Hopcroft-Karp finds many shortest augmenting paths per BFS phase and runs in
O(E * sqrt(V)), the standard fast choice for large bipartite matching instances.
"""
