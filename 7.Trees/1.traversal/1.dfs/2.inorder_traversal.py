'''
94. Binary Tree Inorder Traversal (Easy)
Problem Statement

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder visits each node in the order: Left, Root, Right.
For a Binary Search Tree this yields the values in sorted ascending order.

Example:
Input:  root = [1,None,2,3]   (level-order, LeetCode style)
Output: [1,3,2]
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Build a tree from a LEVEL-ORDER list (None = missing node).
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


def inorder(root):
    # Verification helper: returns inorder list of values.
    out = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        out.append(node.val)
        dfs(node.right)

    dfs(root)
    return out


def inorderTraversal(root):
    # Recursive DFS: Left subtree, then Root, then Right subtree.
    out = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)         # Left
        out.append(node.val)   # Root
        dfs(node.right)        # Right

    dfs(root)
    return out


if __name__ == "__main__":
    root = build([1, None, 2, 3])
    print(inorderTraversal(root))  # Expected: [1, 3, 2]

    root2 = build([])
    print(inorderTraversal(root2))  # Expected: []

    root3 = build([1])
    print(inorderTraversal(root3))  # Expected: [1]


'''
Pattern
✅ DFS (Recursive Traversal)
Inorder = Left -> Root -> Right. The defining property: on a BST it emits
values in sorted order, so it underpins BST validation, kth-smallest, etc.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(h)  |   (recursion stack; O(n) worst skewed)

Better Possible?
❌ Not asymptotically — must touch each node once -> O(n) optimal.
Morris inorder achieves O(1) extra space by threading; iterative stack
version keeps O(h) and avoids recursion-depth limits.
'''
