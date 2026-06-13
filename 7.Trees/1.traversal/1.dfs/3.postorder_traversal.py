'''
145. Binary Tree Postorder Traversal (Easy)
Problem Statement

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Postorder visits each node in the order: Left, Right, Root.

Example:
Input:  root = [1,None,2,3]   (level-order, LeetCode style)
Output: [3,2,1]
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


def postorderTraversal(root):
    # Recursive DFS: Left subtree, Right subtree, then Root last.
    out = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)         # Left
        dfs(node.right)        # Right
        out.append(node.val)   # Root

    dfs(root)
    return out


if __name__ == "__main__":
    root = build([1, None, 2, 3])
    print(postorderTraversal(root))  # Expected: [3, 2, 1]

    root2 = build([])
    print(postorderTraversal(root2))  # Expected: []

    root3 = build([1])
    print(postorderTraversal(root3))  # Expected: [1]


'''
Pattern
✅ DFS (Recursive Traversal)
Postorder = Left -> Right -> Root. Children are fully processed before the
parent, so it is the go-to order for bottom-up work: deleting/freeing a tree,
computing subtree heights, and most tree-DP problems.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(h)  |   (recursion stack; O(n) worst skewed)

Better Possible?
❌ Not asymptotically — each node visited once -> O(n) optimal.
A common iterative trick: do a modified preorder (Root, Right, Left) with a
stack and reverse the result; still O(n) time, O(h) space.
'''
