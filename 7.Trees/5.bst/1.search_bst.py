"""
700. Search in a Binary Search Tree (Easy)

Problem Statement
-----------------
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST whose value equals val and return the subtree rooted
at that node. If such a node does not exist, return None (an empty subtree).

Example
-------
Input : root = [4,2,7,1,3], val = 2
Output: inorder of returned subtree -> [1, 2, 3]

Input : root = [4,2,7,1,3], val = 5
Output: inorder of returned subtree -> []   (None / not found)
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


def search_bst(root, val):
    # Use the BST invariant: go left if target is smaller, right if larger.
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root  # node with matching val, or None if not found


if __name__ == "__main__":
    root = build([4, 2, 7, 1, 3])
    print(inorder(search_bst(root, 2)))  # Expected: [1, 2, 3]
    print(inorder(search_bst(root, 5)))  # Expected: []


"""
Pattern
-------
BST Search. Exploit the ordering invariant (left < node < right): at each node a
single comparison eliminates an entire subtree, so we walk one root-to-leaf path
instead of scanning every node. Iterative form uses O(1) extra space.

| Metric | Value |
|--------|-------|
| Time   | O(h)  (h = height; O(log n) balanced, O(n) skewed) |
| Space  | O(1)  (iterative) |

Better Possible?
No. Search must at least follow the path to the target, so O(h) is optimal for a
BST; balancing the tree (AVL/Red-Black) bounds h at O(log n).
"""
