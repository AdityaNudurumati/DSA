'''
1. Invert Binary Tree (Easy)
Problem Statement

Given the root of a binary tree, invert the tree (mirror it) and return its root.
Inverting means swapping the left and right child of every node.

Input:
root = [4,2,7,1,3,6,9]   (level-order, None = missing)

Output:
[4,7,2,9,6,3,1]          (level-order of the inverted tree)
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # level-order list (None = missing node, LeetCode style) -> root
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            lv = next(it)
        except StopIteration:
            break
        if lv is not None:
            node.left = TreeNode(lv)
            q.append(node.left)
        try:
            rv = next(it)
        except StopIteration:
            break
        if rv is not None:
            node.right = TreeNode(rv)
            q.append(node.right)
    return root


def level_order(root):
    # BFS values; trailing None are trimmed (LeetCode-style compact form)
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


def invertTree(node):
    # swap children at every node, recurse both sides
    if not node:
        return None
    node.left, node.right = invertTree(node.right), invertTree(node.left)
    return node


if __name__ == "__main__":
    root = build([4, 2, 7, 1, 3, 6, 9])
    print(level_order(invertTree(root)))  # Expected: [4, 7, 2, 9, 6, 3, 1]


'''
Pattern
Tree Modification — recursive swap (mirror).
Recurse to children first, then swap the two pointers on the way back up
(post-order style). Works because inverting a tree = inverting each subtree
then swapping them; the base case (None) returns nothing to swap.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(h)  |   (recursion stack, h = tree height)

Better Possible?
No on time — every node must be visited once, so O(n) is optimal.
Space can drop to O(1) extra with an iterative BFS/DFS using an explicit
queue/stack, but the recursion-stack O(h) is already fine and cleaner.
'''
