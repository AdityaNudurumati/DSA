"""
450. Delete Node in a BST (Medium)

Problem Statement
-----------------
Given the root of a binary search tree (BST) and a key, delete the node with the
given key and return the root of the (possibly updated) tree. Deletion has three
cases: the node is a leaf, has one child, or has two children (replace with its
inorder successor).

Example
-------
Input : root = [5,3,6,2,4,None,7], key = 3
Output: inorder after deletion -> [2, 4, 5, 6, 7]
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


def delete_node_bst(root, key):
    if not root:
        return None
    if key < root.val:                       # search left
        root.left = delete_node_bst(root.left, key)
    elif key > root.val:                     # search right
        root.right = delete_node_bst(root.right, key)
    else:                                    # found the node to delete
        if not root.left:                    # 0 or 1 child -> splice in the other
            return root.right
        if not root.right:
            return root.left
        # Two children: find inorder successor (smallest in right subtree).
        succ = root.right
        while succ.left:
            succ = succ.left
        root.val = succ.val                  # copy successor value up
        root.right = delete_node_bst(root.right, succ.val)  # remove successor
    return root


if __name__ == "__main__":
    root = build([5, 3, 6, 2, 4, None, 7])
    root = delete_node_bst(root, 3)
    print(inorder(root))  # Expected: [2, 4, 5, 6, 7]


"""
Pattern
-------
BST Delete. Descend by comparison to locate the key, then resolve by case:
leaf -> remove; one child -> replace with that child; two children -> overwrite
with the inorder successor (leftmost node of the right subtree) and delete the
successor. The inorder-successor swap preserves the BST ordering invariant.

| Metric | Value |
|--------|-------|
| Time   | O(h)  (one descent to find key + one to find successor) |
| Space  | O(h)  (recursion stack) |

Better Possible?
No. Deletion needs the search path plus successor lookup, both O(h); this is
optimal for a BST. Self-balancing variants keep h at O(log n).
"""
