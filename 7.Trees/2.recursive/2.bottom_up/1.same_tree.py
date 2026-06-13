'''
100. Same Tree (Easy)
Problem Statement

Given the roots of two binary trees p and q, write a function to check if they are
the same tree.

Two binary trees are the same if they are structurally identical and the nodes have
the same values.

Example:
Input:  p = [1,2,3], q = [1,2,3]
Output: True

Input:  p = [1,2], q = [1,null,2]
Output: False

Explanation:
[1,2,3] vs [1,2,3] are identical. [1,2] places its child on the left while
[1,null,2] places it on the right, so the structures differ.
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Build a tree from a LeetCode-style level-order list (None = missing node).
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):
            v = values[i]; i += 1
            if v is not None:
                node.left = TreeNode(v); q.append(node.left)
        if i < len(values):
            v = values[i]; i += 1
            if v is not None:
                node.right = TreeNode(v); q.append(node.right)
    return root


def inorder(root):
    # In-order traversal (helper for verification).
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def isSameTree(p, q):
    # BOTTOM-UP: children return whether their subtrees match; combine at the parent.
    if not p and not q:
        return True                       # base: both empty -> equal
    if not p or not q or p.val != q.val:
        return False                      # one empty or values differ -> not equal
    left = isSameTree(p.left, q.left)     # ask children for their verdicts
    right = isSameTree(p.right, q.right)
    return left and right                 # combine: both subtrees must match


if __name__ == "__main__":
    print(isSameTree(build([1, 2, 3]), build([1, 2, 3])))      # Expected: True

    print(isSameTree(build([1, 2]), build([1, None, 2])))      # Expected: False

    print(isSameTree(build([1, 2, 1]), build([1, 1, 2])))      # Expected: False


'''
Pattern
Bottom-Up recursion (children return values; combine at the parent).
Each call decides equality of two subtrees by first resolving the base cases
(empty / value mismatch), then combining the boolean verdicts returned by the left
and right children with AND. Information flows UP. This matches the
dfs(node) -> combine(left, right, node) template.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |  n = nodes in the smaller tree; we stop early on the first mismatch
| Space  | O(h)  |  recursion stack, h = height (O(n) worst case for a skewed tree)

Better Possible?
No. In the worst case (identical trees) every node must be compared, so O(n) time
is optimal. Space could be made O(1) extra only with an explicit iterative stack,
which does not change the asymptotic bound.
'''
