"""
236. Lowest Common Ancestor of a Binary Tree (Medium)

Problem Statement:
Given the root of a binary tree and two nodes p and q, find their lowest common
ancestor (LCA). The LCA is the deepest node that has both p and q as descendants
(a node is allowed to be a descendant of itself). All node values are unique and
both p and q exist in the tree.

Example:
    Input:  root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
    Output: 3
    Input:  root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
    Output: 5   (5 is an ancestor of 4, so the LCA is 5 itself)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Level-order list (None = missing) -> root, LeetCode style.
    if not values:
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


def find(root, val):
    # Locate the actual node object for a given value (for test setup).
    if not root:
        return None
    if root.val == val:
        return root
    return find(root.left, val) or find(root.right, val)


def lca(node, p, q):
    # Bottom-up: a node is the LCA when p and q are found in different subtrees,
    # or when the node itself is p or q (self-descendant rule).
    if node is None or node is p or node is q:
        return node
    left = lca(node.left, p, q)
    right = lca(node.right, p, q)
    if left and right:      # p and q split across this node -> this is the LCA
        return node
    return left or right    # both on one side (or none) -> bubble the answer up


if __name__ == "__main__":
    root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    p, q = find(root, 5), find(root, 1)
    print(lca(root, p, q).val)  # Expected: 3

    p, q = find(root, 5), find(root, 4)
    print(lca(root, p, q).val)  # Expected: 5

"""
Pattern: Lowest Common Ancestor — Binary Tree (bottom-up recursion).
Technique: post-order DFS returns "did this subtree contain p or q?". If the left
and right subtrees each report a hit, the current node is the split point and thus
the LCA. If only one side reports a hit, propagate that result upward. Matching p
or q at a node short-circuits, which naturally handles the self-ancestor case.
Why: the deepest node whose two subtrees each hold one target is exactly the LCA.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(h)  |

Better Possible?
No — without parent pointers or preprocessing we must inspect each node once, so
O(n) time is optimal. Space is the recursion depth O(h) (O(n) worst case skewed).
With parent pointers it becomes a two-path intersection; with many repeated queries,
binary lifting gives O(log n) per query after O(n log n) preprocessing.
"""
