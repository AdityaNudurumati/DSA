'''
2. Maximum-Weight Independent Set on a Tree (Medium)
Problem Statement

Given an undirected tree where each node has a weight, choose a subset of
nodes such that no two chosen nodes are adjacent (connected by an edge) and
the total weight of the chosen nodes is as large as possible.

Return that maximum total weight.

Example
Input:
A tree of 7 nodes (rooted at 0):

            0(weight 10)
           /            \
        1(5)            2(8)
       /    \              \
     3(1)   4(7)          5(3)
                            |
                          6(9)

weights = [10, 5, 8, 1, 7, 3, 9]
edges   = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6]]

Output:
27
Explanation:
Choose nodes {0, 3, 4, 6}. None are adjacent:
  0 touches 1 and 2 (both unchosen); 3 and 4 touch only 1; 6 touches only 5.
Total weight = 10 + 1 + 7 + 9 = 27, which is the maximum achievable.
'''

from collections import defaultdict


def maxWeightIndependentSet(weights, edges):

    n = len(weights)
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Tree DP with include / exclude (post-order DFS).
    # State : dfs(node) -> (incl, excl)
    #   incl = best weight for node's subtree WHEN node is chosen
    #   excl = best weight for node's subtree WHEN node is NOT chosen
    # Transition (children c):
    #   incl = weight[node] + sum( excl_c )      # children must be excluded
    #   excl = sum( max(incl_c, excl_c) )        # children free to choose
    # Base  : a leaf -> incl = weight[leaf], excl = 0
    def dfs(node, parent):
        incl = weights[node]
        excl = 0
        for child in graph[node]:
            if child == parent:
                continue
            ci, ce = dfs(child, node)
            incl += ce
            excl += max(ci, ce)
        return incl, excl

    return max(dfs(0, -1))


if __name__ == "__main__":
    weights = [10, 5, 8, 1, 7, 3, 9]
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6]]
    print(maxWeightIndependentSet(weights, edges))  # Expected: 27

    # Sanity check: a simple path 0-1-2 with weights [3,5,2].
    # Best independent set is {1} = 5 (cannot take both 0 and 2 with 1).
    print(maxWeightIndependentSet([3, 5, 2], [[0, 1], [1, 2]]))  # Expected: 5

'''
Pattern
✅ Tree DP — Include / Exclude (rooted post-order DFS)

Which DP & why
Each node carries two states: the best subtree weight if the node is taken
(forcing all its children to be excluded) and the best if it is skipped
(each child independently takes its better option). Computing both values
bottom-up means every node and edge is touched once, and the global answer
is max(incl, excl) at the root. The adjacency constraint is enforced purely
by the include-branch forcing its children into their exclude option.

For the example tree the optimum is 27, realized by the set {0, 3, 4, 6}:
taking root 0(10) blocks 1 and 2, so the left branch contributes its leaves
3(1)+4(7)=8 and the right branch (with 2 blocked) contributes 6(9)=9, for
10+8+9 = 27. The path sanity check (weights [3,5,2]) returns 5: picking the
middle node 5 beats picking the two ends 3+2.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No
Linear time is optimal: every node must be inspected, and the recursion
visits each exactly once with O(1) work per edge.
'''
