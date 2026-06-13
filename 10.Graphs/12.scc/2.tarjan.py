"""
2. Strongly Connected Components - Tarjan (Medium)

Problem Statement:
Given a directed graph as an adjacency list, count the number of strongly
connected components (SCCs) using Tarjan's low-link algorithm in a single DFS.
An SCC is a maximal set of mutually reachable vertices.

Example:
    Input:  n = 5, adj = {0:[1], 1:[2], 2:[0,3], 3:[4], 4:[]}
    Output: 3        # SCCs are {0,1,2}, {3}, {4}

    Input:  n = 3, adj = {0:[1], 1:[2], 2:[0]}
    Output: 1        # one big cycle -> single SCC
"""


def tarjan_scc_count(n, adj):
    disc = [-1] * n          # discovery time of each vertex (-1 = unvisited)
    low = [0] * n            # lowest disc reachable from the subtree (+ back edges)
    on_stack = [False] * n   # is vertex currently on the SCC stack
    stack = []               # vertices of the current in-progress SCC
    timer = [0]              # mutable counter usable inside nested helper
    count = [0]              # number of SCCs found

    def dfs(start):
        # Iterative DFS carrying an index over each node's neighbor list.
        call = [(start, 0)]
        while call:
            u, i = call[-1]
            if i == 0:
                # First visit to u: assign discovery + low, push on stack.
                disc[u] = low[u] = timer[0]
                timer[0] += 1
                stack.append(u)
                on_stack[u] = True

            if i < len(adj[u]):
                # Advance neighbor pointer for u before processing neighbor v.
                call[-1] = (u, i + 1)
                v = adj[u][i]
                if disc[v] == -1:
                    call.append((v, 0))      # recurse into unvisited child
                elif on_stack[v]:
                    low[u] = min(low[u], disc[v])  # back edge to active SCC
            else:
                # All neighbors processed: u is a root if low[u] == disc[u].
                if low[u] == disc[u]:
                    count[0] += 1
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        if w == u:
                            break
                call.pop()
                if call:
                    parent = call[-1][0]
                    low[parent] = min(low[parent], low[u])  # propagate low up

    for u in range(n):
        if disc[u] == -1:
            dfs(u)

    return count[0]


if __name__ == "__main__":
    adj1 = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: []}
    print(tarjan_scc_count(5, adj1))                         # Expected: 3

    adj2 = {0: [1], 1: [2], 2: [0]}
    print(tarjan_scc_count(3, adj2))                         # Expected: 1

    # Two separate cycles joined by a one-way edge -> 2 SCCs.
    adj3 = {0: [1], 1: [0, 2], 2: [3], 3: [2]}
    print(tarjan_scc_count(4, adj3))                         # Expected: 2

"""
Pattern: Strongly Connected Components via Tarjan (single-pass low-link DFS).
Technique: one DFS assigns each vertex a discovery time disc[u] and a low-link
low[u] = the smallest disc reachable using tree edges plus one back edge into a
vertex still on the active stack. When low[u] == disc[u], u is the root of an
SCC and we pop the stack down to u to emit that component. The "on stack" check
distinguishes back/cross edges so only edges staying inside the current SCC
lower the low-link.
Why: low-link captures the highest ancestor a subtree loops back to; equality
with disc[u] means nothing below u escapes upward, so u closes a component.

| Metric | Value     |
|--------|-----------|
| Time   | O(V + E)  |
| Space  | O(V + E)  |

Better Possible?
No; like Kosaraju this is linear and optimal. Tarjan needs only one DFS and no
graph transpose, so it is typically the preferred constant-factor choice.
"""
