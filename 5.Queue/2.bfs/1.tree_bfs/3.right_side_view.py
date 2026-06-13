"""
199. Binary Tree Right Side View (Medium)

Problem Statement:
Given the root of a binary tree, imagine yourself standing on the right side of
it. Return the values of the nodes you can see ordered from top to bottom.

Example:
    Input:  root = [1,2,3,None,5,None,4]
    Output: [1,3,4]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    # BFS level by level; the LAST node dequeued in each level is the rightmost.
    result = []
    if not root:
        return result
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == level_size - 1:   # last node of this level = visible from right
                result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result


if __name__ == "__main__":
    # Build tree [1,2,3,None,5,None,4]
    #         1
    #        / \
    #       2   3
    #        \    \
    #         5    4
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(4))

    print(right_side_view(root))  # Expected: [1, 3, 4]

"""
Pattern: Level Order / Tree BFS, keep the last node per level.
Technique: run standard level-order BFS and record the value of the final node
processed at each level (index level_size - 1).
Why: the rightmost node of every level is exactly what an observer on the right
sees; BFS visits left-to-right, so it is the last dequeued.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
No on time. A DFS (right child first) recording the first node seen at each new
depth uses O(h) stack instead of O(width), but time stays O(n).
"""
