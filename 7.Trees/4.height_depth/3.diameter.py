"""
543. Diameter of Binary Tree (Easy)

Problem Statement:
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter is the length of the longest path between any two nodes in the
tree. This path may or may not pass through the root. The length of a path is
measured by the number of EDGES between the nodes.

Example:
    Input:  root = [1,2,3,4,5]
    Output: 3
    (longest path 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3, which is 3 edges)
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


def level_order(root):
    """Return values grouped per level (for verification)."""
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out


def diameter(root):
    best = 0  # longest path seen, in edges

    def height(node):
        # Returns height in EDGES; updates `best` with the path through `node`.
        nonlocal best
        if not node:
            return -1  # empty subtree contributes -1 so a leaf has height 0
        lh = height(node.left)
        rh = height(node.right)
        # Path through this node = edges down-left + edges down-right.
        best = max(best, (lh + 1) + (rh + 1))
        return 1 + max(lh, rh)

    height(root)
    return best


if __name__ == "__main__":
    print(diameter(build([1, 2, 3, 4, 5])))  # Expected: 3

    print(diameter(build([])))        # Expected: 0
    print(diameter(build([1])))       # Expected: 0
    print(diameter(build([1, 2])))    # Expected: 1


"""
Pattern: Height / Depth / Diameter.
Technique: single post-order traversal that computes each subtree's height
while simultaneously updating a shared best. The longest path that bends at a
given node equals (left height in edges + 1) + (right height in edges + 1).
Using -1 for the empty-subtree height lets a leaf naturally report height 0
and keeps the edge arithmetic clean. Computing diameter and height together
avoids the naive O(n^2) approach of recomputing height at every node.

| Metric | Value |
| Time   | O(n)  |  one post-order pass, each node once
| Space  | O(h)  |  recursion stack (O(n) worst, O(log n) balanced)

Better Possible?
No. The answer depends on heights of all subtrees, so every node must be
visited: O(n) is optimal. The naive recompute-height-per-node version is
O(n^2); the combined pass here is the standard improvement.
"""
