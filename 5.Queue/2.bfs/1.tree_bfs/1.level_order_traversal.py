"""
102. Binary Tree Level Order Traversal (Medium)

Problem Statement:
Given the root of a binary tree, return the level order traversal of its
nodes' values (i.e., from left to right, level by level).

Example:
    Input:  root = [3,9,20,None,None,15,7]
    Output: [[3],[9,20],[15,7]]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    # Classic BFS: process one full level per outer iteration.
    result = []
    if not root:
        return result
    q = deque([root])
    while q:
        level_size = len(q)        # snapshot count for THIS level
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    # Build tree [3,9,20,None,None,15,7]
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print(level_order(root))  # Expected: [[3], [9, 20], [15, 7]]

"""
Pattern: Level Order / Tree BFS.
Technique: a deque holds the current frontier; we record len(q) before draining
so each inner loop consumes exactly one level, then enqueue children for the next.
Why: a FIFO queue yields nodes in left-to-right, top-to-bottom order naturally.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
No — every node must be visited once, so O(n) time is optimal. Space is the
maximum width of the tree (worst case O(n) for the last level).
"""
