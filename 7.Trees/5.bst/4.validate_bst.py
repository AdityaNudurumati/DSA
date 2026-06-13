"""
98. Validate Binary Search Tree (Medium)

Problem Statement
-----------------
Given the root of a binary tree, determine if it is a valid binary search tree
(BST). A valid BST requires every node's left subtree to contain only values
strictly less than the node, and its right subtree only values strictly greater,
with both subtrees themselves being valid BSTs.

Example
-------
Input : root = [2,1,3]                  Output: True
Input : root = [5,1,4,None,None,3,6]    Output: False  (3 and 6 sit under 4 but
                                                          violate the root bound 5)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Build a tree from a LeetCode-style level-order list (None = missing)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


def inorder(root):
    """Return inorder traversal as a list (sorted order for a valid BST)."""
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res


def validate_bst(root):
    # Each node must lie strictly within (lo, hi); bounds tighten as we descend.
    def valid(node, lo=float("-inf"), hi=float("inf")):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return valid(node.left, lo, node.val) and valid(node.right, node.val, hi)
    return valid(root)


if __name__ == "__main__":
    print(validate_bst(build([2, 1, 3])))                     # Expected: True
    print(validate_bst(build([5, 1, 4, None, None, 3, 6])))   # Expected: False


"""
Pattern
-------
BST Validation via bounds propagation. A node is valid only if it falls inside an
open interval (lo, hi); descending left caps the upper bound at the node's value,
descending right raises the lower bound. This catches violations a naive
parent-only check misses (a deep descendant breaking an ancestor's bound).

| Metric | Value |
|--------|-------|
| Time   | O(n)  (visit every node once) |
| Space  | O(h)  (recursion stack) |

Better Possible?
No. Every node must be inspected to certify validity, so O(n) time is optimal.
An equivalent approach checks that an inorder traversal is strictly increasing.
"""
