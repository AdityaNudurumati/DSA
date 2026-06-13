'''
1. Sum of Distances in Tree (Hard)
Problem Statement

There is an undirected, connected tree with n nodes labeled 0..n-1 and
n-1 edges. You are given the integer n and the list edges, where
edges[i] = [a, b] means there is an edge between nodes a and b.

For each node i, compute answer[i] = the sum of the distances between
node i and all other nodes in the tree.

Return the list answer.

Example
Input:
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

Output:
[8, 12, 6, 10, 10, 10]
Explanation:
The tree looks like:
        0
       / \
      1   2
         /|\
        3 4 5
answer[0] = dist(0,1)+dist(0,2)+dist(0,3)+dist(0,4)+dist(0,5)
          = 1 + 1 + 2 + 2 + 2 = 8
'''

from collections import defaultdict


def sumOfDistancesInTree(n, edges):

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    count = [1] * n   # count[i]  = number of nodes in subtree rooted at i
    answer = [0] * n  # answer[i] = sum of distances from i to its subtree

    # --- Pass 1: post-order DFS rooted at 0 ---------------------------------
    # State : (count[node], answer[node]) for the subtree of `node`.
    # Transition:
    #   count[node]  = 1 + sum(count[child])
    #   answer[node] = sum(answer[child] + count[child])
    #     (every node in a child's subtree is one edge further from `node`)
    # Base   : a leaf has count = 1 and answer = 0.
    def post(node, parent):
        for child in graph[node]:
            if child == parent:
                continue
            post(child, node)
            count[node] += count[child]
            answer[node] += answer[child] + count[child]

    # --- Pass 2: pre-order DFS = REROOTING ----------------------------------
    # Move the root from `node` to a `child`. n_child nodes get one step
    # closer, the other (n - n_child) nodes get one step farther:
    #   answer[child] = answer[node] - count[child] + (n - count[child])
    # Carrying the parent's already-rerooted answer down gives O(n) total.
    def pre(node, parent):
        for child in graph[node]:
            if child == parent:
                continue
            answer[child] = answer[node] - count[child] + (n - count[child])
            pre(child, node)

    post(0, -1)
    pre(0, -1)
    return answer


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(sumOfDistancesInTree(n, edges))  # Expected: [8, 12, 6, 10, 10, 10]

'''
Pattern
✅ Tree DP — Rerooting (two-pass DFS)

Which DP & why
A naive solution runs a BFS/DFS from every node: O(n^2). Rerooting reuses
the answer computed for a parent to derive each child's answer in O(1):
  - Pass 1 (post-order) builds subtree sizes `count` and the subtree-only
    distance sums `answer` for the chosen root.
  - Pass 2 (pre-order) propagates the global answer down by observing what
    happens to every distance when the root shifts to a neighbour.
This turns n independent O(n) computations into one linear sweep.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No
O(n) time is optimal — the output alone has n entries and the tree has n
nodes that must each be visited.
'''
