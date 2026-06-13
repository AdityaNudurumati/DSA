"""
230. Kth Smallest Element in a BST (Medium)

Problem Statement
-----------------
Given the root of a binary search tree (BST) and an integer k, return the value
of the kth smallest element (1-indexed) in the tree.

Example
-------
Input : root = [3,1,4,None,2], k = 1                Output: 1
Input : root = [5,3,6,2,4,None,None,1], k = 3       Output: 3
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


def kth_smallest_bst(root, k):
    # Inorder traversal visits values in ascending order; the kth pop is the answer.
    stack = []
    cur = root
    while stack or cur:
        while cur:               # dive to the leftmost unvisited node
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()        # smallest unvisited value
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right          # then explore the right subtree
    return -1                    # k out of range (not expected per constraints)


if __name__ == "__main__":
    print(kth_smallest_bst(build([3, 1, 4, None, 2]), 1))              # Expected: 1
    print(kth_smallest_bst(build([5, 3, 6, 2, 4, None, None, 1]), 3))  # Expected: 3


"""
Pattern
-------
Kth Smallest via iterative inorder. An inorder walk of a BST yields sorted order,
so we stream values left-to-right and stop after emitting k of them. The explicit
stack lets us halt early instead of materializing the whole traversal.

| Metric | Value |
|--------|-------|
| Time   | O(h + k)  (descend left spine, then pop k nodes) |
| Space  | O(h)      (stack) |

Better Possible?
For many queries on a static tree, augment each node with its subtree size to
answer in O(h) per query. For a single query, O(h + k) is already optimal.
"""
