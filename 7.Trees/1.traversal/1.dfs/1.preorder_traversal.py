'''
144. Binary Tree Preorder Traversal (Easy)
Problem Statement

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Preorder visits each node in the order: Root, Left, Right.

Example:
Input:  root = [1,None,2,3]   (level-order, LeetCode style)
Output: [1,2,3]
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


def level_order(root):
    # Verification helper: BFS list of values (skips Nones).
    out, q = [], deque([root] if root else [])
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


def preorderTraversal(root):
    # Recursive DFS: visit Root, then Left subtree, then Right subtree.
    out = []

    def dfs(node):
        if not node:
            return
        out.append(node.val)   # Root
        dfs(node.left)         # Left
        dfs(node.right)        # Right

    dfs(root)
    return out


if __name__ == "__main__":
    root = build([1, None, 2, 3])
    print(preorderTraversal(root))  # Expected: [1, 2, 3]

    root2 = build([])
    print(preorderTraversal(root2))  # Expected: []

    root3 = build([1])
    print(preorderTraversal(root3))  # Expected: [1]


'''
Pattern
✅ DFS (Recursive Traversal)
Preorder = Root -> Left -> Right. Process the node BEFORE descending,
which makes it the natural choice for copying/serializing a tree top-down.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(h)  |   (recursion stack; h = tree height, O(n) worst skewed)

Better Possible?
❌ Not asymptotically — every node must be visited once -> O(n) is optimal.
Space can drop to O(1) extra via Morris traversal, but it mutates pointers
temporarily; an explicit-stack iterative version keeps O(h) without recursion.
'''
