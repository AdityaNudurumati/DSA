"""
103. Binary Tree Zigzag Level Order Traversal (Medium)

Problem Statement:
Given the root of a binary tree, return the zigzag level order traversal of its
nodes' values. (i.e., from left to right, then right to left for the next level
and alternate between).

Example:
    Input:  root = [3,9,20,None,None,15,7]
    Output: [[3],[20,9],[15,7]]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    # Standard level-order BFS; reverse every odd-indexed level.
    result = []
    if not root:
        return result
    q = deque([root])
    left_to_right = True
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not left_to_right:
            level.reverse()         # flip direction for this level
        result.append(level)
        left_to_right = not left_to_right
    return result


if __name__ == "__main__":
    # Build tree [3,9,20,None,None,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print(zigzag_level_order(root))  # Expected: [[3], [20, 9], [15, 7]]

"""
Pattern: Level Order / Tree BFS with alternating direction.
Technique: collect each level normally, then reverse the list in place on
alternating levels using a boolean flag.
Why: traversal order is unchanged; only the output orientation toggles, so a
single reverse per odd level is the cleanest expression.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
No on time (each node visited once). The reverse adds at most O(width) per level
and could be avoided by appending to either end of a deque per level, but the
overall O(n) bound is unchanged.
"""
