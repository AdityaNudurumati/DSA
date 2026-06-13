"""
94. Binary Tree Inorder Traversal — Morris Method (Medium)

Problem Statement
-----------------
Return the inorder traversal of a binary tree using O(1) extra space (no stack
and no recursion). Morris traversal achieves this by temporarily threading each
node's inorder predecessor's right pointer back to the node, then undoing the
thread once that subtree is consumed.

Inorder = Left -> Node -> Right.

Example
-------
Input:  root = [1, None, 2, 3]
Output: [1, 3, 2]

Input:  root = [4, 2, 6, 1, 3, 5, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
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
        if not hasattr(node, "_l"):
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
            node._l = True
        else:
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
            q.popleft()
    return root


def inorder(root):
    """Recursive inorder, used only to cross-check the Morris result."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def morris_inorder(root):
    out, cur = [], root
    while cur:
        if not cur.left:
            # No left subtree: visit and step right (a real edge or a thread).
            out.append(cur.val)
            cur = cur.right
        else:
            # Find the inorder predecessor: rightmost node of the left subtree.
            pred = cur.left
            while pred.right and pred.right is not cur:
                pred = pred.right
            if pred.right is None:
                # First visit: thread predecessor back to cur, descend left.
                pred.right = cur
                cur = cur.left
            else:
                # Thread already exists: left subtree done. Remove thread,
                # visit cur, move right.
                pred.right = None
                out.append(cur.val)
                cur = cur.right
    return out


if __name__ == "__main__":
    t1 = build([1, None, 2, 3])
    print(morris_inorder(t1))              # Expected: [1, 3, 2]

    t2 = build([4, 2, 6, 1, 3, 5, 7])
    print(morris_inorder(t2))              # Expected: [1, 2, 3, 4, 5, 6, 7]


"""
Pattern
-------
Morris Inorder Traversal. Instead of a stack, we temporarily reuse the spare
right pointers of leaves: for each node with a left child we link its inorder
predecessor's right pointer to the node itself (a "thread"). Following that
thread later lets us climb back up without any auxiliary memory, and we erase
the thread on the way back so the tree is restored to its original shape.

| Metric        | Value |
| Time          | O(n)  |   (each edge is traversed at most a constant number of times)
| Space         | O(1)  |   (only a few pointers; no stack, no recursion)

Better Possible?
This is the space-optimal solution: O(1) auxiliary space with O(n) time, which
is the best achievable since all n nodes must be visited. The trade-off is that
the tree is mutated mid-traversal (then restored), so it is unsafe under
concurrent reads. When O(h) stack space is acceptable, the iterative-stack
version in 1.iterative_inorder.py is simpler and non-mutating.
"""
