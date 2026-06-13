"""
104. Maximum Depth of Binary Tree (Easy)

Problem Statement:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Example:
    Input:  root = [3,9,20,None,None,15,7]
    Output: 3
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Build a tree from a LeetCode-style level-order list (None = missing)."""
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


def level_order(root):
    """Return values grouped per level (for verification)."""
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out


def max_depth(root):
    # Bottom-up: depth of a node = 1 + deeper of its two subtrees.
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    root = build([3, 9, 20, None, None, 15, 7])
    print(max_depth(root))  # Expected: 3

    print(max_depth(build([])))     # Expected: 0
    print(max_depth(build([1])))    # Expected: 1


"""
Pattern: Height / Depth / Diameter.
Technique: classic bottom-up recursion. Each call returns the height of its
subtree; the answer for a node is 1 + max(child heights). Why it works: the
longest root-to-leaf path through a node must descend into its deeper child,
so taking the max of the two subtree depths is optimal.

| Metric | Value |
| Time   | O(n)  |  each node visited once
| Space  | O(h)  |  recursion stack, h = tree height (O(n) worst, O(log n) balanced)

Better Possible?
No. Every node must be inspected to know the deepest leaf, so O(n) time is a
lower bound. An iterative BFS/DFS achieves the same time but can flatten the
stack to an explicit queue if recursion depth is a concern.
"""
