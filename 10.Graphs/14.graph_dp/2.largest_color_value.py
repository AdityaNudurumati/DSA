'''
1857. Largest Color Value in a Directed Graph (Hard)
Problem Statement

There is a directed graph of n colored nodes and m edges. The nodes are numbered from
0 to n - 1. You are given a string colors where colors[i] is a lowercase letter giving
the color of the i-th node, and a 2D array edges where edges[j] = [aj, bj] means there
is a directed edge from node aj to node bj.

A valid path is a sequence of nodes following directed edges. The "color value" of a
path is the number of nodes that are colored the most frequently along that path.

Return the largest color value of any valid path in the graph, or -1 if the graph
contains a cycle (in which case paths can be arbitrarily long).

Input:
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

Output:
3

Explanation:
The path 0 -> 2 -> 3 -> 4 contains 3 nodes colored "a" (nodes 0, 2, 4).
'''

from collections import deque, defaultdict


# Kahn topological sort while carrying a DP table count[node][color] = max number of
# nodes of that color over any path ENDING at `node`. Processing in topo order lets us
# relax each edge u->v: count[v][c] = max(count[v][c], count[u][c] (+1 if c==color[v])).
# If we cannot process all n nodes, a cycle exists -> return -1.

def largestPathValue(colors, edges):
    n = len(colors)
    adj = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    # count[node] is a list of 26 color tallies for best path ending at node.
    count = [[0] * 26 for _ in range(n)]
    queue = deque()
    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)
            count[node][ord(colors[node]) - ord('a')] = 1

    seen = 0       # number of nodes popped (topologically processed)
    answer = 0
    while queue:
        u = queue.popleft()
        seen += 1
        answer = max(answer, max(count[u]))

        for v in adj[u]:
            cv = ord(colors[v]) - ord('a')
            for c in range(26):
                # extend best-ending-at-u path into v, +1 for v's own color
                extended = count[u][c] + (1 if c == cv else 0)
                if extended > count[v][c]:
                    count[v][c] = extended
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # if some node never reached indegree 0, it sits on a cycle
    return answer if seen == n else -1


if __name__ == "__main__":
    colors1 = "abaca"
    edges1 = [[0, 1], [0, 2], [2, 3], [3, 4]]
    print(largestPathValue(colors1, edges1))  # Expected: 3

    colors2 = "a"
    edges2 = [[0, 0]]  # self-loop -> cycle
    print(largestPathValue(colors2, edges2))  # Expected: -1


'''
Pattern
✅ Graph DP on a DAG (topological sort + DP)
We need the most frequent color along any path; since contributions accumulate along
directed edges, we DP in topological (Kahn) order, keeping 26 color counts per node for
the best path ending there. The same topo sort detects cycles (fewer than n nodes
processed => cycle => answer is unbounded => -1).
| Metric | Value          |
| ------ | -------------- |
| Time   | O((n + m) * 26)|
| Space  | O(n * 26)      |
Better Possible?
❌ No
Every node and edge must be visited, and each node carries 26 color tallies; the 26
factor is the fixed alphabet size, so this is optimal for the general problem.
'''
