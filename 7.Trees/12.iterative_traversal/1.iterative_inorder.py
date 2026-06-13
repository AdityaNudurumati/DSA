"""
94. Binary Tree Inorder Traversal (Easy)

Problem Statement
-----------------
Given the root of a binary tree, return the inorder traversal of its nodes'
values. Solve it iteratively (without recursion) using an explicit stack.

Inorder = Left -> Node -> Right.

Example
-------
Input:  root = [1, None, 2, 3]
Output: [1, 3, 2]

Input:  root = [1, 2, 3, 4, 5]
Output: [4, 2, 5, 1, 3]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Level-order list (None = missing node, LeetCode style) -> root."""
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for v in it:
        node = q[0]
        if not hasattr(node, "_l"):           # fill left child first
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
            node._l = True
        else:                                 # then right child, then advance
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
            q.popleft()
    return root


def inorder(root):
    """Recursive inorder, used only to cross-check the iterative result."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def inorder_iterative(root):
    # Push all left children, pop a node (visit), then move to its right subtree.
    stack, cur, out = [], root, []
    while cur or stack:
        while cur:                # dive left, remembering the path
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()         # leftmost unvisited node
        out.append(cur.val)       # visit it
        cur = cur.right           # explore the right subtree next
    return out


if __name__ == "__main__":
    t1 = build([1, None, 2, 3])
    print(inorder_iterative(t1))           # Expected: [1, 3, 2]

    t2 = build([1, 2, 3, 4, 5])
    print(inorder_iterative(t2))           # Expected: [4, 2, 5, 1, 3]


"""
Pattern
-------
Iterative Inorder via explicit stack. The recursion's call stack is simulated
by a manual stack: we keep pushing left children, then pop to visit, then pivot
right. This avoids Python recursion-depth limits and makes the L->N->R ordering
explicit. Each node is pushed and popped exactly once.

| Metric        | Value |
| Time          | O(n)  |
| Space         | O(h)  |   (stack holds at most one root-to-leaf path)

Better Possible?
Time is already optimal at O(n) since every node must be visited. Space can be
reduced to O(1) with Morris inorder (see 3.morris_inorder.py), which threads the
tree instead of using an auxiliary stack.
"""
