"""
1. Binary Tree Left Side View (Medium)

Problem Statement:
Given the root of a binary tree, imagine yourself standing on the LEFT side of
it. Return the values of the nodes you can see ordered from top to bottom (the
first node encountered on each level).

Example:
    Input:  root = [1,2,3,None,5,None,4]
    Output: [1,2,5]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Level-order list (None = missing node, LeetCode style) -> root.
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for v in it:
        node = q[0]
        if node.left is None and v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        elif node.left is not None:
            # left slot filled; this value is the right child, then pop parent.
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
            q.popleft()
    return root


def level_order(root):
    # Helper: list of values level by level (for verification / debugging).
    res = []
    if not root:
        return res
    q = deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


def left_side_view(root):
    # BFS level by level; the FIRST node dequeued each level is the leftmost.
    result = []
    if not root:
        return result
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == 0:                 # first node of this level = visible from left
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
    root = build([1, 2, 3, None, 5, None, 4])
    print(left_side_view(root))  # Expected: [1, 2, 5]


"""
Pattern: Tree Views — Level Order / Tree BFS, keep the FIRST node per level.
Technique: standard level-order BFS; record the value of the first node processed
at each level (index 0).
Why: the leftmost node of every level is exactly what an observer on the left
sees; BFS visits left-to-right, so it is the first dequeued.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
No on time (must visit every node). A DFS (left child first) recording the first
node seen at each new depth uses O(h) stack instead of O(width), but time stays O(n).
"""
