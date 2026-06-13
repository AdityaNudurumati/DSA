'''
886. Possible Bipartition (Medium)
Problem Statement

We want to split a group of n people (labeled from 1 to n) into two groups of
any size. Each person may dislike some other people, and they should not go into
the same group.

Given the integer n and the array dislikes where dislikes[i] = [a, b] indicates
that the person labeled a does not like the person labeled b, return True if it
is possible to split everyone into two groups in this way.

This is exactly "Is Graph Bipartite?": build an undirected graph where a dislike
edge means the two people must be in different groups, then 2-color it.

Example:
Input:
n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output:
True

Input:
n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output:
False
'''

from collections import deque, defaultdict


def possibleBipartition(n, dislikes):
    adj = defaultdict(list)          # build undirected graph from dislike pairs
    for a, b in dislikes:
        adj[a].append(b)
        adj[b].append(a)

    color = {}                       # person -> 0/1 group
    for start in range(1, n + 1):    # people are labeled 1..n
        if start in color:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in color:
                    color[v] = color[u] ^ 1   # opposite group
                    q.append(v)
                elif color[v] == color[u]:
                    return False              # conflict => can't split
    return True


if __name__ == "__main__":
    n1, dislikes1 = 4, [[1, 2], [1, 3], [2, 4]]
    print(possibleBipartition(n1, dislikes1))  # Expected: True

    n2, dislikes2 = 3, [[1, 2], [1, 3], [2, 3]]
    print(possibleBipartition(n2, dislikes2))  # Expected: False


'''
Pattern
✅ Bipartite Graph - BFS 2-coloring
A "dislike" forces two people into different groups, i.e. opposite colours. The
group assignment is feasible iff the dislike graph is bipartite (no odd cycle).
Build the adjacency list, then colour each component with alternating groups.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(V + E)       |
| Space  | O(V + E)       |

Better Possible?
❌ No
Must inspect every person and every dislike edge once. Union-Find achieves the
same complexity; BFS coloring is the optimal, intended approach for this folder.
'''
