"""
110. Balanced Binary Tree (Easy)

Problem Statement:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is one in which, for EVERY node, the heights of
the left and right subtrees differ by at most 1.

Example:
    Input:  root = [3,9,20,None,None,15,7]
    Output: True
    Input:  root = [1,2,2,3,3,None,None,4,4]
    Output: False
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


def is_balanced(root):
    # Bottom-up: each call returns subtree height, or -1 if already unbalanced.
    def height(node):
        if not node:
            return 0
        lh = height(node.left)
        if lh == -1:
            return -1  # short-circuit: left subtree already unbalanced
        rh = height(node.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1  # this node violates the balance condition
        return 1 + max(lh, rh)

    return height(root) != -1


if __name__ == "__main__":
    print(is_balanced(build([3, 9, 20, None, None, 15, 7])))     # Expected: True
    print(is_balanced(build([1, 2, 2, 3, 3, None, None, 4, 4]))) # Expected: False

    print(is_balanced(build([])))   # Expected: True
    print(is_balanced(build([1])))  # Expected: True


"""
Pattern: Height / Depth / Diameter.
Technique: bottom-up recursion with a sentinel. height() returns the real
subtree height, but the moment any subtree is found unbalanced it returns -1,
which propagates straight up and stops further work. This folds the balance
check INTO the height computation, so the whole tree is judged in one pass
rather than recomputing height at every node (the naive O(n^2) approach).

| Metric | Value |
| Time   | O(n)  |  each node visited once, early exit on imbalance
| Space  | O(h)  |  recursion stack (O(n) worst, O(log n) balanced)

Better Possible?
No. Balance depends on every subtree's height, so all nodes must be examined:
O(n) is optimal. The top-down version that calls a separate height() per node
is O(n^2); the sentinel-based single pass here is the standard optimization.
"""
