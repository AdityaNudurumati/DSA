"""
437. Path Sum III (Medium)

Problem Statement:
Given the root of a binary tree and an integer targetSum, return the number of
paths where the sum of the values along the path equals targetSum. The path
does NOT need to start or end at the root or a leaf, but it must go DOWNWARDS
(travelling only from parent nodes to child nodes).

Example:
    Input:  root = [10,5,-3,3,2,None,11,3,-2,None,1], targetSum = 8
    Output: 3           (5->3, 5->2->1, -3->11)
"""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Level-order list (None = missing node, LeetCode style) -> root."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1
    return root


def path_sum_iii(root, target):
    # Prefix-sum count along the current root->node chain.
    # A downward path ending at `node` sums to target iff some ancestor prefix
    # equals (running - target). Mirrors the subarray-sum-equals-k trick.
    prefix = defaultdict(int)
    prefix[0] = 1                      # empty prefix -> path starting at root

    def dfs(node, running):
        if not node:
            return 0
        running += node.val
        count = prefix[running - target]
        prefix[running] += 1
        count += dfs(node.left, running) + dfs(node.right, running)
        prefix[running] -= 1           # backtrack: leave this chain
        return count

    return dfs(root, 0)


if __name__ == "__main__":
    t = build([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    print(path_sum_iii(t, 8))   # Expected: 3


"""
Pattern: PATH-BASED (Any downward path, count)
Technique: prefix sums on tree paths. Carry the running root->node sum and a
hashmap of prefix-sum frequencies seen along the CURRENT chain. The number of
downward paths ending at a node with sum == target equals freq[running-target].
Increment the map descending, decrement on the way back up (backtracking) so
counts reflect only the active ancestor chain.

| Metric | Value |
| Time   | O(n)  — each node visited once, O(1) map work per node |
| Space  | O(h)  — recursion stack + prefix map keyed by chain prefixes |

Better Possible?
The naive "start DFS at every node" is O(n^2) / O(n*h); the prefix-sum map cuts
it to O(n), which is optimal since each node must be inspected at least once.
"""
