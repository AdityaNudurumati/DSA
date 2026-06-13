'''
1. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
Problem Statement

Given two integer arrays preorder and inorder where preorder is the preorder
traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

All values are unique.

Input:
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

Output (level-order):
[3,9,20,None,None,15,7]

Explanation:
    3
   / \
  9  20
     / \
    15  7
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # level-order list (None = missing node) -> root
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


def level_order(root):
    # BFS that records None for missing children, trimming trailing Nones
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def buildTree(preorder, inorder):
    # First element of preorder is always the root. Its position in inorder
    # splits inorder into left subtree (before) and right subtree (after).
    idx = {v: i for i, v in enumerate(inorder)}   # O(1) root lookups
    pre = [0]                                      # mutable pointer into preorder

    def helper(lo, hi):
        if lo > hi:
            return None
        root = TreeNode(preorder[pre[0]])
        pre[0] += 1
        mid = idx[root.val]
        root.left = helper(lo, mid - 1)            # left consumes preorder first
        root.right = helper(mid + 1, hi)
        return root

    return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    print(level_order(root))  # Expected: [3, 9, 20, None, None, 15, 7]


'''
Pattern
Tree Construction — Divide & Conquer on traversal slices.
Preorder gives the root order (root first); inorder locates the root to partition
left vs right subtrees. A hash map of value->inorder index makes each split O(1),
and a single shared preorder pointer avoids re-slicing arrays.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |  (hash map + recursion stack)

Better Possible?
No. Every node must be created once, so O(n) is optimal. Naive index-based array
slicing would be O(n^2) time and O(n^2) space; the index map keeps it linear.
'''
