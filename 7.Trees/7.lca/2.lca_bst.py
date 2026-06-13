"""
235. Lowest Common Ancestor of a Binary Search Tree (Medium)

Problem Statement:
Given the root of a binary search tree (BST) and two nodes p and q, find their
lowest common ancestor (LCA). The LCA is the deepest node that has both p and q
as descendants (a node may be a descendant of itself). All values are unique and
both p and q exist in the tree.

Example:
    Input:  root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8
    Output: 6
    Input:  root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 4
    Output: 2   (2 is an ancestor of 4, so the LCA is 2 itself)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Level-order list (None = missing) -> root, LeetCode style.
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


def find(root, val):
    # Locate the actual node object for a given value (for test setup).
    node = root
    while node:
        if val < node.val:
            node = node.left
        elif val > node.val:
            node = node.right
        else:
            return node
    return None


def lca(root, p, q):
    # Exploit BST ordering: walk down from the root. If both targets are smaller
    # than the current node, the LCA must be in the left subtree; if both larger,
    # go right. The first node where they diverge (or equals one of them) is the
    # split point and therefore the LCA.
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node     # diverge here (or node is p / q) -> LCA
    return None


if __name__ == "__main__":
    root = build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

    p, q = find(root, 2), find(root, 8)
    print(lca(root, p, q).val)  # Expected: 6

    p, q = find(root, 2), find(root, 4)
    print(lca(root, p, q).val)  # Expected: 2

"""
Pattern: Lowest Common Ancestor — BST (ordered downward walk).
Technique: a BST guarantees left < node < right, so we never need to recurse into
both subtrees. Starting at the root, if both p and q lie on the same side we move
there; the moment they straddle the current node (one <=, one >=) — or the node IS
one of them — we have found the lowest node whose subtree contains both.
Why: the LCA is precisely the first value that sits between p and q on the path down.

| Metric | Value |
|--------|-------|
| Time   | O(h)  |
| Space  | O(1)  |

Better Possible?
No — we follow a single root-to-divergence path, O(h) time (O(log n) balanced,
O(n) skewed) with O(1) extra space, which is optimal for a single query. This beats
the generic binary-tree O(n) approach by using the sorted-order invariant.
"""
