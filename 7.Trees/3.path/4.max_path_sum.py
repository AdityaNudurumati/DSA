"""
124. Binary Tree Maximum Path Sum (Hard)

Problem Statement:
A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes has an edge connecting them; a node appears at most once and the path
need NOT pass through the root. The path sum is the sum of the node values.
Given the root of a binary tree, return the maximum path sum of any non-empty
path.

Example:
    Input:  root = [1,2,3]
    Output: 6           (2 -> 1 -> 3)

    Input:  root = [-10,9,20,None,None,15,7]
    Output: 42          (15 -> 20 -> 7)
"""

from collections import deque


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


def max_path_sum(root):
    best = float("-inf")

    # gain(node) = max sum of a path that STARTS at node and goes downward.
    def gain(node):
        nonlocal best
        if not node:
            return 0
        # Clamp negative gains to 0: ignoring a branch beats subtracting it.
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        # Best path THROUGH node bends left+node+right (cannot be passed up).
        best = max(best, node.val + left + right)
        # Upward we may keep only one straight branch.
        return node.val + max(left, right)

    gain(root)
    return best


if __name__ == "__main__":
    print(max_path_sum(build([1, 2, 3])))                          # Expected: 6
    print(max_path_sum(build([-10, 9, 20, None, None, 15, 7])))    # Expected: 42


"""
Pattern: PATH-BASED (Any Node -> Any Node, max path sum)
Technique: bottom-up DFS with a global best. At each node we compute the best
downward gain of each child (clamped at 0), update a global maximum with the
"bent" path left+node+right that turns at this node, and return only a single
straight branch (node + best child) for the parent to extend.

| Metric | Value |
| Time   | O(n)  — each node processed once |
| Space  | O(h)  — recursion stack |

Better Possible?
O(n) is optimal — the maximum can hinge on any node, so all must be examined.
The single global pass already avoids recomputation; nothing meaningful to cut.
"""
