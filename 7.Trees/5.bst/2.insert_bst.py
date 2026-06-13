"""
701. Insert into a Binary Search Tree (Medium)

Problem Statement
-----------------
You are given the root of a binary search tree (BST) and a value to insert into
the tree. Return the root of the BST after the insertion. It is guaranteed that
the new value does not exist in the original BST.

Example
-------
Input : root = [4,2,7,1,3], val = 5
Output: inorder after insertion -> [1, 2, 3, 4, 5, 7]
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


def insert_bst(root, val):
    # Empty tree: the new value becomes the root.
    if not root:
        return TreeNode(val)
    cur = root
    while True:
        if val < cur.val:               # belongs in the left subtree
            if cur.left is None:
                cur.left = TreeNode(val)
                return root
            cur = cur.left
        else:                           # belongs in the right subtree
            if cur.right is None:
                cur.right = TreeNode(val)
                return root
            cur = cur.right


if __name__ == "__main__":
    root = build([4, 2, 7, 1, 3])
    root = insert_bst(root, 5)
    print(inorder(root))  # Expected: [1, 2, 3, 4, 5, 7]


"""
Pattern
-------
BST Insert. Walk down using the ordering invariant until the correct empty slot
(a None child) is found, then attach a new leaf there. A new value is always
inserted as a leaf, so existing structure is untouched. Iterative => O(1) space.

| Metric | Value |
|--------|-------|
| Time   | O(h)  (h = height) |
| Space  | O(1)  (iterative) |

Better Possible?
No. Locating the insertion slot requires descending to a leaf, so O(h) is optimal.
Self-balancing trees keep h at O(log n) but the asymptotic descent cost is the same.
"""
