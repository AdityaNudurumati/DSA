'''
2. Construct Binary Tree from Inorder and Postorder Traversal (Medium)
Problem Statement

Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the same
tree, construct and return the binary tree.

All values are unique.

Input:
inorder   = [9,3,15,20,7]
postorder = [9,15,7,20,3]

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


def buildTree(inorder, postorder):
    # Last element of postorder is always the root. Its position in inorder
    # splits inorder into left/right subtrees. Consume postorder from the BACK,
    # and build the RIGHT subtree before the LEFT (mirror of preorder+inorder).
    idx = {v: i for i, v in enumerate(inorder)}
    post = [len(postorder) - 1]                    # mutable pointer, moving backward

    def helper(lo, hi):
        if lo > hi:
            return None
        root = TreeNode(postorder[post[0]])
        post[0] -= 1
        mid = idx[root.val]
        root.right = helper(mid + 1, hi)           # right consumed first from back
        root.left = helper(lo, mid - 1)
        return root

    return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = buildTree(inorder, postorder)
    print(level_order(root))  # Expected: [3, 9, 20, None, None, 15, 7]


'''
Pattern
Tree Construction — Divide & Conquer on traversal slices.
Postorder visits the root LAST, so reading postorder back-to-front yields roots in
root-right-left order. Inorder locates each root to split left vs right. Because we
take from the back, the right subtree must be built before the left so the pointer
lands on the correct values.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |  (hash map + recursion stack)

Better Possible?
No. Each node is created exactly once -> O(n) is optimal. The inorder index map
replaces O(n) searches/slicing, keeping it linear instead of O(n^2).
'''
